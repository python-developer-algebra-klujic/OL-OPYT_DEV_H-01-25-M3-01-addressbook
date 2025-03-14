


class Person:
    def __init__(self,
                 id: int,
                 vat_id: str = '',
                 email: str = '',
                 phone: str = '',
                 website: str = ''):
        self.id = id
        self.vat_id = vat_id
        self.email = email
        self.phone = phone
        self.website = website

        self.check_cro_vat_id()

    def check_cro_vat_id(self):
        if len(self.vat_id) != 11:
            print(f'!!! OIB mora imati 11 brojki. Vi ste unijeli: {len(self.vat_id)}.')



class Contact(Person):
    def __init__(self,
                 first_name: str,
                 last_name: str,

                 id: int,
                 vat_id: str = '',
                 email: str = '',
                 phone: str = '',
                 website = ''):
        super().__init__(id=id,
                         vat_id=vat_id,
                         email=email,
                         phone=phone,
                         website=website)

        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f'{self.first_name} {self.last_name}'


class Company(Person):
    def __init__(self,
                 name:str,
                 headquarter: str,

                 id: int,
                 vat_id: str = '',
                 email: str = '',
                 phone: str = '',
                 website: str = ''):
        super().__init__(id, vat_id, email, phone, website)

        self.name = name
        self.headquarter = headquarter

    def __repr__(self):
        return f'{self.name} ({self.headquarter})'
