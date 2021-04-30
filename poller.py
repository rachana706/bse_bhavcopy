import csv
import http.client
import logging
import os
import redis
from zipfile import ZipFile
import schedule
import time





def get_bhavcopy():
    conn = http.client.HTTPSConnection("www.bseindia.com")
    payload = ''
    headers = {}
    try:
        conn.request("GET", "/download/BhavCopy/Equity/EQ290421_CSV.ZIP",
                     payload,
                     headers)
        res = conn.getresponse()
        data = res.read()
        with open('bhavcopy.zip', 'wb') as fd:
            fd.write(data)
        zf = ZipFile("./bhavcopy.zip")
        zf.extractall(path='extraction_bhavcopy')
        zf.close()
    except:
        return False
    return True

def poll():
    print('polling started')
    if get_bhavcopy():
        conn = redis.Redis('localhost')
        try:
            for (dirpath, dirnames, filenames) in os.walk(
                    'extraction_bhavcopy'):

                if filenames:
                    with open("/".join([dirpath, filenames[0]]),
                              mode='r') as infile:

                        for line in csv.DictReader(infile):
                            conn.hset("zerodha" + dict(line)['SC_NAME'].strip(),

                                      mapping=dict(line))


        except Exception as e:
            logging.exception(e)


if __name__ == '__main__':

    schedule.every().day.at("17:30").do(poll, 'It is 17:30')

    while True:
        schedule.run_pending()
        time.sleep(60*60)  # wait one minute