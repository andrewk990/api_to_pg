import requests
import pandas as pd
import sqlalchemy as sa
import creds
from datetime import datetime


engine = creds.get_connection()
get_tablename = sa.inspect(engine)
current_datetime = datetime.now()
table_name = 'random_cannabis_tmp'
target_table = 'random_cannabis'

insert_query = sa.text(
            """
            DELETE FROM public.random_cannabis
                WHERE id IN (
                    SELECT id FROM public.random_cannabis_tmp
                );
                
            INSERT INTO public.random_cannabis
                select distinct on (id) *
                    from random_cannabis_tmp
                order by id, date_add;

            ANALYZE public.random_cannabis;
            
            DROP TABLE IF EXISTS public.random_cannabis_tmp;
            """
)

create_query = sa.text(
            """
            CREATE TABLE IF NOT EXISTS public.random_cannabis as (
                select distinct on (id) *
                    from public.random_cannabis_tmp
                order by date_actual;

            ANALYZE public.random_cannabis;

            DROP TABLE IF EXISTS public.random_cannabis_tmp;
            )
            """
)

try:

    # max result 100 items
    api_responce = requests.get(url='https://random-data-api.com/api/cannabis/random_cannabis?size=100')
    datafr = pd.DataFrame(api_responce.json())
    datafr['date_add'] = current_datetime

    con = engine.connect()

    datafr.to_sql(table_name
                    , con
                    , if_exists='append'
                    , index=False
                    , index_label=None
                    )
    con.close()

    print("tmp table is success created!")

    con = engine.connect()

    if target_table in get_tablename.get_table_names():

        con.execute(insert_query)
        con.commit()

        print("insert into target success!")

    else:

        con.execute(create_query)
        con.commit()

        print("create target success!")

    con.close()

    print("success!")

except Exception as error:
    print(error)
