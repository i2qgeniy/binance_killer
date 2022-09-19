from binance.spot import Spot #as Client


client = Spot()
r = open('text.txt', 'w')
class User():


    def __init__(self, id):
        self.id = id


    def init_api(self, key_api, secret_api):
        self.private_client = Spot(key=key_api, secret=secret_api)
        data = {'User_id':self.id, 'Key':key_api, 'Secret':secret_api}
        r = open('Data_base.txt', 'r')
        for id in r['User_id']:
            if id == self.id:
                r.close()
                break
        r.close()
        r = open('Data_base.txt', 'a')
        r.write(str(data))
        r.close()



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
