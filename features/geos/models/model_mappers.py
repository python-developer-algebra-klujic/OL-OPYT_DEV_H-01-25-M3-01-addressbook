import json
from features.geos.models import Geo


class GeoMapper:
    def from_json(self, geo_json: str) -> Geo:
        if isinstance(geo_json, dict):
            return Geo(
                latitude = geo_json['lat'],
                longitude = geo_json['lng']
            )
        else:
            return None

    def to_json(self, geo: Geo) -> str:
        return json.dumps(geo.__dict__)