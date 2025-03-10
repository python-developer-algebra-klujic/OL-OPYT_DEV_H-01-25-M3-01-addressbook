from contacts.models import Contact
from contacts.services import save_contact


def main():
    my_contacts = []

    while True:
        first_name = input('Upisite ime kontakt: ')
        last_name = input('Upisite prezime kontakt: ')
        contact = Contact(first_name, last_name)

        my_contacts.append(contact)

        # TODO Ispravno pozvati ovu funkciju
        save_contact()

        print(my_contacts)

        print()
        next_contact = input('Zelite li dodati novi kontatk? (da/ne): ')
        if next_contact.lower() != 'da':
            break


if __name__ == '__main__':
    main()
