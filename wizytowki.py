from faker import Faker

faker = Faker("pl_PL")


class BaseContact:
    def __init__(self, name = faker.name(), phone_number = faker.phone_number(), mail = faker.email()):
        self.name = name
        self.phone_number = phone_number
        self.mail = mail

    def __str__(self):
        return f'{self.name}, {self.phone_number}, {self.mail}' 

    def contact(self):
        return f"Wybieram numer {self.phone_number} i dzwonię do {self.name}"

    @property
    def label_length(self):
        return int(len(self.name))

class BusinessContact(BaseContact):
    def __init__(self, job = faker.job(), company = faker.company(), business_phone = faker.phone_number(), *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.job = job
        self.company = company
        self.business_phone = business_phone
   
    def __str__(self):
        return f'{self.job}, {self.company}, {self.business_phone}'

    def contact(self):
        return f"Wybieram numer {self.business_phone} i dzwonię do {self.name}"    

private_contact = BaseContact()
business_card = BusinessContact()

def create_contacts(card_type, n=10):
    output = []
    for i in range(n):
        if card_type == "Base":
            output.append (str(BaseContact(name=faker.name(), phone_number=faker.phone_number(), mail= faker.email())))
            return (output)
        elif card_type == "Business":
            output.append (str(BusinessContact(name=faker.name(), job=faker.job(), company=faker.company(), business_phone=faker.phone_number())))
            return (output)
    else:
        print("Zły wybór, proszę spróbuj ponownie")
        exit    


contacts = create_contacts(input("Wybierz rodzaj wizytówki, wpisując 'Base' lub 'Business': "))

print('\n')
print(private_contact.contact())
print(business_card.contact())
print('\n')
print(private_contact.label_length)

print(contacts)











        