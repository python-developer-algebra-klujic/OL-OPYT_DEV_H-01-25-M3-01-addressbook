import json
from typing import List
from features.contacts.models import Contact
from repositories.file_repository import FileRepository


class ContactServices:
    def __init__(self,
                 data_source: str = 'file',
                 contacts: List[Contact] = []):
        self.data_source = data_source
        self.contacts = contacts

        self.get_all_contacts()

    def create_contact(self, contact: Contact) -> None:
        self.contacts.append(contact)
        if self.data_source == 'file':
            file_repo = FileRepository()
            file_repo.write_to_file(self.contacts)

        else:
            try:
                print('Potrebno je implementirati snimanje u bazu!!!')
                # TODO snimi u bazu
                pass
            except Exception as ex:
                print(f'Dogodila se greska u ContactServices.create_contact() snimanje u bazu. {ex}.')

    def get_contact(self, contact_id: int) -> Contact:
        for contact_from_list in self.contacts:
            if contact_from_list.id == contact_id:
                return contact_from_list
        return None

    def get_all_contacts(self) -> List[Contact]:
        if self.data_source == 'file':
            try:
                with open('files/contacts.json', 'r') as file_reader:
                    contacts_from_file = json.load(file_reader)
                    self.contacts = list(map(lambda contact_dict: self._map_dict_to_contact(contact_dict),
                                             contacts_from_file))
            except Exception as ex:
                print(f'Dogodila se greska u ContactServices.get_all_contacts() citanje iz filea. {ex}.')
        else:
            try:
                pass
            except Exception as ex:
                print(f'Dogodila se greska u ContactServices.get_all_contacts() citanje iz baze. {ex}.')

        return self.contacts

    def update_contact(self, contact: Contact):
        pass

    def delete_contact(self, contact_id: int):
        for index, contact in enumerate(self.contacts):
            if contact.id == contact_id:
                del self.contacts[index]

        # Commit
        if self.data_source == 'file':
            try:
                with open('files/contacts.json', 'w') as file_writer:
                    # contacts_dict = []
                    # for contact in self.contacts:
                    #     contacts_dict.append(contact.__dict__)
                    contacts_dict = list(map(lambda contact: contact.__dict__, self.contacts))
                    json.dump(contacts_dict, file_writer, indent=4)

            except Exception as ex:
                print(f'Dogodila se greska u ContactServices.create_contact() snimanje u file. {ex}.')
        else:
            try:
                print('Potrebno je implementirati snimanje u bazu!!!')
                # TODO snimi u bazu
                pass
            except Exception as ex:
                print(f'Dogodila se greska u ContactServices.create_contact() snimanje u bazu. {ex}.')
        # TODO
        # Izdvojiti u zasebnu metodu
        # contact_to_delete.is_deleted = True
        # contact_to_delete.deleted_at = datetime.now()



    def _map_dict_to_contact(self, contact_dict) -> Contact:
        temp_contact = Contact(
            id = contact_dict['id'],
            first_name = contact_dict['first_name'],
            last_name = contact_dict['last_name'],
            email = contact_dict['email'],
            phone = contact_dict['phone'],
            web_profile = contact_dict['web_profile']
        )

        return temp_contact


class ContactApiServices:
    pass


class ContactDbServices:
    pass


class ContactFileServices:
    pass
