from typing import List
from contacts.models import Contact


class ContactServices:
    def __init__(self,
                 data_source: str = 'file',
                 contacts: List[Contact] = []):
        self.contacts = contacts
        self.data_source = data_source

    def create_contact(self, contact: Contact) -> None:
        self.contacts.append(contact)
        # slijedeci korak
        # Provjera data_source: ako je file snimamo u file, a ako je db snimamo u bazu
        if self.data_source == 'file':
            try:
                pass
            except Exception as ex:
                print(f'Dogodila se greska u ContactServices.create_contact() snimanje u file. {ex}.')
        else:
            try:
                print('Potrebno je implementirati snimanje u bazu!!!')
                # TODO snimi u bazu
                pass
            except Exception as ex:
                print(f'Dogodila se greska u ContactServices.create_contact() snimanje u bazu. {ex}.')































def get_contact(contact_id: int) -> Contact:
    # Dohvati mi iz datoteke kontakt koji ima identican Id kao i contact_id.
    pass


def get_all_contacts() -> List[Contact]:
    # Dohvati mi sve kontakte iz datoteke bez obzira koji Id imaju.
    pass


def update_contact(contact: Contact):
    pass


def delete_contact(contact_id: int):
    # Dohvati mi iz datoteke kontakt koji ima identican Id kao i contact_id.
    # Izbrisi taj kontakt iz datoteke tako da promijenimo:
    #       is_deleted = True
    #       deleted_at = datetime.now()
    pass
