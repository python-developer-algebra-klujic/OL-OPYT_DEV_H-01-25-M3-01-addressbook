import json
from features.contacts.models.models import Contact


class ContactMapper:
    def from_json(self, contact_json: str) -> Contact:
        if isinstance(contact_json, dict):
            return Contact(
                name = contact_json['name'],
                username = contact_json['username'],
                email = contact_json['email'],
                phone = contact_json['phone'],
                website = contact_json['website']
            )
        else:
            return None

    def to_json(self, contact: Contact) -> str:
        return json.dumps(contact.__dict__)
