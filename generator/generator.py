import random

from data.data import Person, Color, Date

from faker import Faker

faker_en = Faker('en_Us')


def generated_person():
    yield Person(
        full_name=f'{faker_en.first_name()} {faker_en.last_name()}',
        firstname=faker_en.first_name(),
        lastname=faker_en.last_name(),
        date_of_birth=random.choice(['29 Jun 1990', '02 Jun 2000']),
        gender=random.randint(0, 2),
        hobbies=random.randint(0, 2),
        mobile_number=f'38093{"".join(str(random.randint(0, 9)) for _ in range(5))}',
        age=random.randint(10, 80),
        salary=random.randint(10000, 50000),
        department=random.choice(['department1', 'department2', 'department3', 'department4', 'department5']),
        email=faker_en.email(),
        current_address=faker_en.address(),
        permanent_address=faker_en.address()
    )


def generated_file():
    path = rf'D:\Test-Framework-for-web\filetest{random.randint(1,999)}'
    file = open(path, 'w')
    file.write('Test Test')
    file.close()
    return path.split('\\')[-1], path


def generate_subject_list():
    subjects = ["Hindi", "English", "Maths", "Physics", "Chemistry", "Biology", "Computer Science", "Commerce",
                "Accounting", "Economics", "Arts", "Social Studies", "History", "Civics"]
    return [random.choice(subjects) for _ in range(3)]


def generate_color():
    yield Color(
        color_name=['Green', 'Blue', 'Black', 'Red', 'Aqua', 'Magenta', 'Indigo', 'Voilet', 'White', 'Purple', 'Yellow']
    )


def generate_date():
    yield Date(
        year=faker_en.year(),
        month=faker_en.month_name(),
        day=faker_en.day_of_month(),
        time=random.choice(['07:15', '09:30', '12:00', '23:45'])
    )

