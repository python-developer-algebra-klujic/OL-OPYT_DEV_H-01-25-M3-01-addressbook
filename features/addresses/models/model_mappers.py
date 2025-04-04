import json
from features.addresses.models import Address


class AddressMapper:
    def from_json(self, address_json: str) -> Address:
        if isinstance(address_json, dict):
            return Address(
                street = address_json['street'],
                suite = address_json['suite'],
                city = address_json['city'],
                zip_code = address_json['zipcode']
            )
        else:
            return None

    def to_json(self, address: Address) -> str:
        return json.dumps(address.__dict__)
