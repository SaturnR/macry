import pytest
from macry.fields import FireMap, FireArray
from macry.connects import FireStore
from scripts.petcare_model import Pet, Address, Appointment, Medication, Owner, Person, Veterinarian

fs = FireStore('petcare')


def test_create(pets_fixture):
    for key in pets_fixture:
        fs[key] = Pet.from_dict(pets_fixture[key])
    fs.update()
    pets = fs.read_all(Pet)
    # test fs models for equality
    for key in pets_fixture:
        assert pets[key].to_dict() == pets_fixture[key]


def test_read():
    pets = fs.read_all(Pet)
    assert len(pets) > 0


def test_update(pets_fixture):
    pets = fs.read_all(Pet)
    # pets_fixture.keys()[0]].


def test_delete(pets_fixture):
    pets = fs.read_all(Pet)
    dkey = list(pets_fixture.keys())[0]
    fs.delete(dkey)
    pets = fs.read_all(Pet)
    assert dkey not in pets
