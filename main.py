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