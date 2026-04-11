from faker import Faker

fake = Faker(locale='ru_Ru')

for _ in range(5):
    print(fake.name())
    print(fake.address())
    print(fake.text())