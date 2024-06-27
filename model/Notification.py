from NotificationStatus import NotificationStatus as status


class Notification:

    def __int__(self, coin: str, curr_price: float, trade_vol: int, high_price: float, market_cap: int):
        self.coin = coin
        self.curr_price = curr_price
        self.trade_vol = trade_vol
        self.high_price = high_price
        self.market_cap = market_cap
        self.curr_status = status.get_failed_status()

    def update_status(self, new_status: status):
        self.curr_status = new_status
        self.show()

    def show(self):
        print(f"Update: Coin: {self.coin}, price: {self.curr_price}, high_price: {self.high_price}, market_cap: {self.market_cap}")
