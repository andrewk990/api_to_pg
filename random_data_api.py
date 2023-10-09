# https://random-data-api.com/api/cannabis/random_cannabis?size=10

import requests
import pandas as pd
import datetime
import sqlalchemy as sa
from datetime import datetime


engine = sa.create_engine('postgresql://postgres:123456@localhost:5432/postgres')
get_tablename = sa.inspect(engine)
current_datetime = datetime.now()
table_name = 'random_cannabis'

try:

    api_responce = requests.get(url='https://random-data-api.com/api/cannabis/random_cannabis?size=10')
    datafr = pd.DataFrame(api_responce.json())
    datafr['date_add'] = current_datetime

    con = engine.connect()

    if table_name in get_tablename.get_table_names():
        datafr.to_sql(table_name
                      , con
                      , if_exists='append'
                      , index=False
                      , index_label=None
                      )
    else:
        datafr.to_sql(table_name
                      , con
                      , if_exists='append'
                      , index=False
                      , index_label=None
                      )

    con.close()

    print("success!")

except Exception as error:
    print(error)