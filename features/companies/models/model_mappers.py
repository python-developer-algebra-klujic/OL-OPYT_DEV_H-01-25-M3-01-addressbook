import json
from features.companies.models.models import Company


class CompanyMapper:
    def from_json(self, company_json: str) -> Company:
        if isinstance(company_json, dict):
            return Company(
                name = company_json['name'],
                catch_phrase = company_json['catchPhrase'],
                best_sell = company_json['bs']
            )
        else:
            return None

    def to_json(self, company: Company) -> str:
        return json.dumps(company.__dict__)
