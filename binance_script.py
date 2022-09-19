from binance.spot import Spot #as Client


client = Spot()
r = open('text.txt', 'w')
class User():


    def __init__(self, id):
        self.id = id


    def init_api(self, key_api):
        self.private_client = Spot(key=key_api[0], secret=key_api[1])
        data = {'User_id': self.id, 'Key': key_api[0], 'Secret': key_api[1]}
        r = open('Data_base.txt', 'a')
        r.write(str(data))
        r.close()

    def check_user(self):
        r = open('Data_base.txt', 'r')
        for id in r:
            if id['User_id'] == self.id:
                r.close()
                return '1'
        r.close()
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
