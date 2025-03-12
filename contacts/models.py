


class Contact:
    def __init__(self,
                 id: int,
                 first_name: str,
                 last_name: str,
                 email: str = '',
                 phone: str = '',
                 web_profile = ''):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.web_profile = web_profile

    def __repr__(self):
        return f'{self.first_name} {self.last_name}'
