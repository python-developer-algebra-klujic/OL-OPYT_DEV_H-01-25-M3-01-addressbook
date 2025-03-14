import json



class FileRepository:
    def __init__(self,
                 file_path: str = 'files/contacts.json'):
        self.file_path = file_path

    def write_to_file(self, content, to_json: bool=True):
        if to_json:
            try:
                with open(self.file_path, 'w') as file_writer:
                    contacts_dict = list(map(lambda content_item: content_item.__dict__, content))
                    json.dump(contacts_dict, file_writer, indent=4)

            except Exception as ex:
                print(f'Dogodila se greska u FileRepository.write_to_file() snimanje u file. {ex}.')
        else:
            pass
