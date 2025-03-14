from contacts.models import Company, Contact
from contacts.services import ContactServices


def main():
    contact_services = ContactServices()
    if len(contact_services.contacts) > 0:
        contact_starting_id = contact_services.contacts[-1].id + 1
    else:
        contact_starting_id = 1

    while True:
        first_name = input('Upisite ime kontakta: ')
        last_name = input('Upisite prezime kontakta: ')
        contact = Contact(id=contact_starting_id,
                          first_name=first_name,
                          last_name=last_name,
                          vat_id='123456')
        print(contact)
        print(contact.vat_id)

        contact_starting_id += 1

        name = input('Upisite naziv firme: ')
        headquarter = input('Upisite grad sjedista firme: ')
        company = Company(id=contact_starting_id,
                          name=name,
                          headquarter=headquarter,
                          vat_id='9876543215256897458')
        print(company)
        print(company.vat_id)

        contact_services.create_contact(contact)
        contact_services.create_contact(company)

        contact_starting_id += 1

        # id = 1
        # contact_from_file = contact_services.get_contact(id)
        # if contact_from_file != None:
        #     print('Contact from file:', contact_from_file)
        # else:
        #     print(f'Ne postoji kontakt u bazi s {id} ID')

        # contact_services.delete_contact(3)

        print()
        next_contact = input('Zelite li dodati novi kontatk? (da/ne): ')
        if next_contact.lower() != 'da':
            break


if __name__ == '__main__':
    main()
