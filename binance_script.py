from binance.spot import Spot #as Client


client = Spot()


class Start_interface():


    def __init__(self, cryptoname):
        self.id = id
        self.cryptoname = cryptoname


    def check(self):
        self.stakan = client.depth(self.cryptoname, limit=10)
        stakan_list = []
        stakan_list.append(self.stakan['asks'][0][0])
        stakan_list.append(self.stakan['asks'][0][1])
        stakan_list.append(self.stakan['bids'][0][0])
        stakan_list.append(self.stakan['bids'][0][1])
        return stakan_list