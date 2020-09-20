import datetime as dt
import json
import logging

import pandas as pd
import requests

# get historical data
date_start = dt.date(2002,1,2)
date_end = dt.date(2020,9,11)

def get_goldprice(date_start, date_end, limit=367):
    ''''''
    start = pd.Timestamp(date_start).date()
    end = pd.Timestamp(date_end).date()
    period = pd.date_range(start, end, freq='D')
    df = pd.DataFrame(index=period)
    query_date = end
    while query_date > start:
        try:
            r = requests.get(f'http://api.nbp.pl/api/cenyzlota/{query_date-dt.timedelta(days=limit)}/{query_date}/?format=json')
            r.raise_for_status()
            for x in r.json():
                date = x['data']
                price = x['cena']
                df.loc[date, 'cena'] = price
        except Exception as e:
            logging.error(e)
        query_date -= dt.timedelta(days=limit)

    df.dropna(inplace=True)
    return df


def get_currencies(date_start, date_end, limit=93):
    ''''''
    start = pd.Timestamp(date_start).date()
    end = pd.Timestamp(date_end).date()
    period = pd.date_range(start, end, freq='D')

    res = []
    query_date = end
    while query_date > start:
        try:
            r = requests.get(f'http://api.nbp.pl/api/exchangerates/tables/C/{query_date-dt.timedelta(days=limit)}/{query_date}/?format=json')
            r.raise_for_status()
            for x in r.json():
                date = x['tradingDate']
                for rate in x['rates']:
                    dicti = {'date': date,
                            'currency': rate['currency'].encode("utf-8"),
                            'code':rate['code'],
                            'bid':rate['bid'],
                            'ask': rate['ask']}
                    res.append(dicti)
        except Exception as e:
            logging.error(e)
        query_date -= dt.timedelta(days=limit)

    df = pd.DataFrame(res)
    df.dropna(inplace=True)
    return df


df = pd.read_csv("curr_and_gold.csv")

date_start = max(df['date'])
date_end = dt.date.today()
new_df = get_currencies(date_start, date_end)

df = pd.concat([df, new_df])
df.date = pd.to_datetime(df.date)
df.to_csv("curr_and_gold.csv")
