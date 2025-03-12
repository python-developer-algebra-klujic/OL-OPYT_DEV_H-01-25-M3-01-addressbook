from contacts.models import Contact
from contacts.services import create_contact


def main():
    while True:
        first_name = input('Upisite ime kontakt: ')
        last_name = input('Upisite prezime kontakt: ')
        contact = Contact(first_name, last_name)

        # TODO Ispravno pozvati ovu funkciju
        create_contact(contact)

        print()
        next_contact = input('Zelite li dodati novi kontatk? (da/ne): ')
        if next_contact.lower() != 'da':
            break


if __name__ == '__main__':
    main()
