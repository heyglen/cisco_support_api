
from cisco_api.records.eox_migration import EoxMigration

attribute_map = {
    'MigrationInformation': 'information',
    'MigrationOption': 'option',
    'MigrationProductId': 'product_id',
    'MigrationProductInfoURL': 'product_information_url',
    'MigrationProductName': 'product_name',
    'MigrationStrategy': 'strategy',
    'PIDActiveFlag': 'pid_active_flag',
}

deafult_clean = lambda x: x.strip() if isinstance(x, str) else None

attribute_type_map = {
    'PIDActiveFlag': lambda x: x == 'Y',
}

class EoxMigrationFactory:

    @classmethod
    def build(cls, migration):
        eox_migration = EoxMigration()
        for key, attribute in attribute_map.items():
            value = record[key]
            if key in attribute_type_map:
                value = attribute_type_map[key](value)
            else:
                value = default_clean(value)
            setattr(eox_migration, attribute, value)
        return eox_migration