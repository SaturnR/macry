import pytest
from google.api_core.datetime_helpers import DatetimeWithNanoseconds
import datetime


@pytest.fixture
def pets_fixture():
    return {'musk1': {
        'owner': {
            'address': {
                'country': 'Georgia',
                'street': 'Rustaveli Av.',
                'city': 'Telavi'
            },
            'last_name': 'Norris',
            'person_id': '20001018299',
            'first_name': 'Chuck'
        },
        'family': 'Dog',
        'name': 'Musk1',
        'bread': 'German Shepherd',
        'color': 'red-brown-black',
        'appointments': [{
            'veterinarian': {
                'address': {
                    'country': 'Georgia',
                    'street': 'Tsereteli Av. N132',
                    'city': 'Tbilisi'
                },
                'last_name': 'Ujmajuridze',
                'person_id': '1919191911',
                'first_name': 'Zaur'
            },
            'description': 'Infected with parasites',
            'medications': [{
                'name': 'caniverm',
                'description': 'Antiparasite'
            }],
            'date': DatetimeWithNanoseconds(2023, 1, 6, 23, 42, 21, 168692, tzinfo=datetime.timezone.utc)
        }],
        'sex': 'male',
        'birthdate': DatetimeWithNanoseconds(2022, 2, 26, 0, 0, tzinfo=datetime.timezone.utc)
    }, 'bukaki': {
        'owner': {
            'address': {
                'country': 'Geogia',
                'street': 'Batumi St. N14',
                'city': 'Poti'
            },
            'last_name': 'Reeves',
            'person_id': '20001218223',
            'first_name': 'Keanu'
        },
        'family': 'Cat',
        'name': 'Bukaki',
        'bread': 'Metis Cat',
        'color': 'Black',
        'appointments': [{
            'veterinarian': {
                'address': {
                    'country': 'Georgia',
                    'street': 'Tsereteli Av. N132',
                    'city': 'Tbilisi'
                },
                'last_name': 'Ujmajuridze',
                'person_id': '1919191911',
                'first_name': 'Zaur'
            },
            'description': 'Infected with parasites',
            'medications': [{
                'name': 'caniverm',
                'description': 'Antiparasite'
            }],
            'date': DatetimeWithNanoseconds(2022, 10, 3, 2, 42, 21, 1682, tzinfo=datetime.timezone.utc)
        }],
        'sex': 'female',
        'birthdate': DatetimeWithNanoseconds(2022, 4, 21, 0, 0, tzinfo=datetime.timezone.utc)
    }}
