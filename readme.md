# Описание проекта #


## Состав проекта и основные компоненты ##

*random_data_api.py* - загрузка данных методом append с сохраннениемисторичности

*random_data_api_v2.py* - загрузка с заменой по id (оставляем только обновленные записи)

*ddl_random_cannabis.sql* - определение таблицы


## Подключение крона ##

`chmod a+x /opt/py/random_data_api.py`

`chmod a+x /opt/py/random_data_api_v2.py`

`crontab -e`

`0 0/12 * * * /opt/py/random_data_api_v2.py > /tmp/random_data_api_v2_cron.log 2>&1`
