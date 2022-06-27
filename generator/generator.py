import random

from data.data import Person

from faker import Faker

faker_en = Faker('en_Us')


def generated_person():
    yield Person(
        full_name=f'{faker_en.first_name()} {faker_en.last_name()}',
        firstname=faker_en.first_name(),
        lastname=faker_en.last_name(),
        age=random.randint(10, 80),
        salary=random.randint(10000, 50000),
        department=random.choice(['department1', 'department2', 'department3', 'department4', 'department5']),
        email=faker_en.email(),
        current_address=faker_en.address(),
        permanent_address=faker_en.address()
    )
