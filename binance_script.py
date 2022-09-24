from binance.spot import Spot#as Client
import sqlite3 as sq
import time
import datetime


client = Spot()
r = open('text.txt', 'w')
class User():


    def __init__(self, id):
        self.id = id


    def init_api(self, key_api):
        self.private_client = Spot(key=key_api[0], secret=key_api[1])
        key = str(key_api[0])
        secret = str(key_api[1])
        user = str(self.id)
        with sq.connect("users.db") as con:
           # cur.execute("""DROP TABLE IF EXISTS users""")
            sql = ("""INSERT INTO users (user_id, key, secret) VALUES(?,?,?)""")
            cur = con.cursor()
            cur.execute(sql, (user, key, secret))
            con.commit()
            #cur.execute("""CREATE TABLE IF NOT EXISTS users (
            #user_id TEXT,
            #key TEXT,
            #secret TEXT
            #)""")
        print('DB update')


    def check_user(self):
        with sq.connect("users.db") as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM users")
            for id in cur:
                if int(id[0])==int(self.id):
                    print('id совпало')
                    return '1'
        print('id не совпало')
        return '0'


    def user_info(self):
        self.info = client.user_asset()
class Start_interface():


    def __init__(self, id, cryptoname):
        self.id = id
        self.cryptoname = cryptoname


    def check(self):
        self.stakan = client.depth(self.cryptoname, limit=500)
        stakan_list = []
        stakan_list.append(self.stakan['asks'][0][0])
        stakan_list.append(self.stakan['asks'][0][1])
        stakan_list.append(self.stakan['bids'][0][0])
        stakan_list.append(self.stakan['bids'][0][1])
        print(self.stakan)
        return stakan_list


    def init_api(self, key_api, seret_api):
        self.private_client = Spot(key = key_api, secret = seret_api)


    def info(self):
        return client.exchange_info(self.cryptoname)


    def get_volume(self, bids_or_asks='bids', lim=100):
        '''
        возвращает объем стакана взависимости от параметра
        :param bids_or_asks:
        :param lim:
        :return:
        '''
        self.depth_btc = client.depth(self.cryptoname, limit=lim)
        if str(bids_or_asks) == '2':
            m = len(self.depth_btc['bids'])
            n = len(self.depth_btc['asks'])
            i = 0
            summ = 0
            ans = []
            while i < m:
                summ += float(self.depth_btc['bids'][i][1])
                i += 1
            ans.append(int(summ))
            i = 0
            summ = 0
            while i < n:
                summ += float(self.depth_btc['asks'][i][1])
                i += 1
            ans.append(int(summ))
            return ans
        else:
            m = len(self.depth_btc[bids_or_asks])
            i = 0
            summ = 0
            while i < m:
                summ += float(self.depth_btc[bids_or_asks][i][1])
                i += 1
            return summ

    def add_volume_graph(self, min):
        i = 0
        while i < min:
            time.sleep(60)
            asks_bids = self.get_volume('2', 5000)
            dt = datetime.datetime.now()
            with sq.connect("users.db") as con:
                sql = ("""INSERT INTO volume_grafick (cryptoname, time, volume_asks, volume_bids) VALUES(?,?,?,?)""")
                cur = con.cursor()
                cur.execute(sql, (self.cryptoname, str(dt.strftime("%H:%M:%S")), asks_bids[1], asks_bids[0]))
                con.commit()
            print('DB update')
            i+=1

