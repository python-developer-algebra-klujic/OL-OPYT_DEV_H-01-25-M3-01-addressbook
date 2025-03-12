from contacts.models import Contact
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
        contact = Contact(id=contact_starting_id, first_name=first_name, last_name=last_name)

        contact_services.create_contact(contact)

        contact_starting_id += 1

        id = 10
        contact_from_file = contact_services.get_contact(id)
        if contact_from_file != None:
            print('Contact from file:', contact_from_file)
        else:
            print(f'Ne postoji kontakt u bazi s {id} ID')

        print()
        next_contact = input('Zelite li dodati novi kontatk? (da/ne): ')
        if next_contact.lower() != 'da':
            break


if __name__ == '__main__':
    main()
