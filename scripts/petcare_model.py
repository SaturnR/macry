from macry import fields
from macry.builder import FireModel

from datetime import datetime


class Address(FireModel):
    __object_name__ = 'address'

    street = fields.FireString()
    city = fields.FireString()
    country = fields.FireString()

    @staticmethod
    def from_dict(source):
        if not source:
            return None
        a = Address()
        a.street = source.get('street')
        a.city = source.get('city')
        a.country = source.get('country')
        return a


class Person(FireModel):

    first_name = fields.FireString()
    last_name = fields.FireString()
    person_id = fields.FireString()
    address = fields.FireMap(entity=Address)

    @classmethod
    def from_dict(cls, source):
        if not source:
            return None
        p = cls()
        p.first_name = source.get('first_name')
        p.last_name = source.get('last_name')
        p.person_id = source.get('person_id')
        p.address = Address.from_dict(source.get('address'))
        return p


class Owner(Person):
    __object_name__ = 'owner'


class Veterinarian(Person):
    __object_name__ = 'veterinarian'


class Medication(FireModel):
    __object_name__ = 'medication'
    name = fields.FireString()
    description = fields.FireString()

    @staticmethod
    def from_dict(source):
        if not source:
            return None
        m = Medication()
        m.name = source.get('name')
        m.description = source.get('description')
        return m


class Appointment(FireModel):
    __object_name__ = 'appointment'

    date = fields.FireTimeStamp()
    veterinarian = fields.FireMap(entity=Veterinarian)
    medications = fields.FireArray(entity=Medication)
    description = fields.FireString()

    @staticmethod
    def from_dict(source):
        if not source:
            return None
        a = Appointment()
        a.date = source.get('date')
        a.veterinarian = Veterinarian.from_dict(source.get('veterinarian'))
        a.medications = fields.FireArray()
        for medication_dict in source.get('medications'):
            a.medications.append(Medication.from_dict(medication_dict))
        a.description = source.get('description')
        return a


class Pet(FireModel):
    __object_name__ = ''
    __root_object__ = True

    name = fields.FireString()
    family = fields.FireString()
    bread = fields.FireString()
    sex = fields.FireString()
    birthdate = fields.FireTimeStamp()
    color = fields.FireString()
    owner = fields.FireMap(entity=Owner)
    appointments = fields.FireArray(entity=Appointment)

    @staticmethod
    def from_dict(source):
        if not source:
            return None
        p = Pet()
        p.name = source.get('name')
        p.family = source.get('family')
        p.bread = source.get('bread')
        p.sex = source.get('sex')
        p.birthdate = source.get('birthdate')
        p.color = source.get('color')
        p.owner = Owner.from_dict(source.get('owner'))

        p.appointments = fields.FireArray()
        for apo in source.get('appointments', []):
            p.appointments.append(
                Appointment.from_dict(apo)
            )
        return p
