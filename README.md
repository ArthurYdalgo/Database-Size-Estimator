# Database Size Estimator

This project is intented to give a **rough** estimate of a database size.

Do not use this as a definitive answer, because some operations might be done under the hood by each database implementation might vary.

The average calculation is a simple arithmetic average, so don't expect much.

The `main.py` file gives you a simple example on how to use it, which will be listed below.

Some column types' sizes are already set, so you won't have to define them by yourself. These value **are in bytes**, and were taken from the MySQL/Laravel documentation page. If you're using a different database with different value, make sure to change these values.

The `min_size` and `max_size` of each column can be changed when declaring them. If they are not send, the values in the `default_type_sizes` will be considered both `min_size` and `max_size`. In case the type is not set, and no size was defined, it's going to be considered `0`. 

The units can be `GB`, `MB` or `KB`.

If the `raw` parameter is set as `True` when a calculation is called, the result will be returned in an `int` in bytes


```
default_type_sizes = {
            'text' : 65535,
            'longText': 4294967295,
            'tinyInteger': 1,
            'string' : 255,
            'timestamp' : 19,
            'timestamps' : 19 * 2,
            'json' : 4294967295,
            'increments' : 4,
            'id' : 8,
            'foreignId': 8,
            'bool': 1,
            'boolean': 1,
            'enum': 255,
            'softDeletes': 19,
            'rememberToken': 100,
            'dateTime': 19
        }
```

## Example

```
from columns import Column
from scheemas import Scheema
from tables import Table

# Companies

# - Columns
id_col = Column('id', 'id')
ts_col = Column('timestamps', 'timestamps')
json_col = Column('data', 'json', 200, 500)
company_text_col = Column('company_text', 'text')
warranty_text_col = Column('warranty_text', 'text')

company_columns = [id_col, ts_col, json_col,
                   company_text_col, warranty_text_col]

companies_table = Table('companies', 0, 1000, company_columns)

print(companies_table.calculateMaxSize(unit='MB', raw=False))

# Domains
# - Columns
inc_col = Column('id', 'increments')
domain_col = Column('domain', 'string')
company_id_col = Column('company_id', 'string')
ts_col = Column('timestamps', 'timestamps')

domains_columns = [inc_col, domain_col, company_id_col, ts_col]

domain_table = Table('domains', 0, 1000, domains_columns)
print(domain_table.calculateMaxSize(unit='MB'))

# Scheema with all tables
scheema_tables = [companies_table, domain_table]

scheema = Scheema('laravel',scheema_tables)
print(scheema.calculateMaxSize('GB'))

```

The output should be 
```
companies -> 125.519 MB
domains -> 0.526 MB
Tables
companies -> 0.123 GB
domains -> 0.001 GB
=======
laravel -> 0.123 GB
```

