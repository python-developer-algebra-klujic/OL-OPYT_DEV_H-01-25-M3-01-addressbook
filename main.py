from contacts.models import Contact
from contacts.services import ContactServices


def main():
    contact_starting_id = 1
    contact_services = ContactServices()

    while True:
        first_name = input('Upisite ime kontakta: ')
        last_name = input('Upisite prezime kontakta: ')
        contact = Contact(id=contact_starting_id, first_name=first_name, last_name=last_name)

        contact_services.create_contact(contact)

        contact_starting_id += 1

        print()
        next_contact = input('Zelite li dodati novi kontatk? (da/ne): ')
        if next_contact.lower() != 'da':
            break


if __name__ == '__main__':
    main()
