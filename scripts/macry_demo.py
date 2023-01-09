from macry.connects import FireStore

from scripts.petcare_model import (
    Pet, Address, Appointment,
    Medication, Owner, Person, Veterinarian
)

from macry.fields import FireMap, FireArray

from datetime import datetime


fs = FireStore('petcare')

p = Pet()

p.color = 'red-brown-black'
p.sex = 'male'
p.birthdate = datetime(year=2022, month=2, day=26)
p.bread = 'German Shepherd'
p.family = 'Dog'
p.name = 'Musk'

owner = Owner()
owner.first_name = 'Chuck'
owner.last_name = 'Norris'
owner.person_id = '111111111111'
owner.address = Address(city='Telavi', country='Georgia', street='Rustaveli Av.')

p.owner = owner

appint = Appointment()
appint.date = datetime.now()
appint.description = 'Infected with parasites'
appint.medications = FireArray()

appint.medications = FireArray()


appint.medications = FireArray()

appint.medications.append(Medication(name='caniverm', description='Antiparasite'))

p.appointments = FireArray()

p.appointments.append(appint)

p.appointments.append(appint)

p.appointments = FireArray()
p.appointments.append(appint)

appint.veterinarian = Veterinarian(
    first_name='Zaur',
    last_name='Ujmajuridze',
    person_id='1919191911',
    address=Address(city='Tbilisi',
                    country='Georgia',
                    street='Tsereteli Av. N132'))

p.appointments[0] = appint

fs['musk'] = p

# fs.update()
