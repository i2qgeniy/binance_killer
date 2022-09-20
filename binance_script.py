from binance.spot import Spot #as Client
import sqlite3 as sq


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
