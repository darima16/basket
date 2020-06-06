class Good:

    def __init__(self, prod):
        self.num = prod['num']
        self.name = prod['name']
        self.art = prod['art']
        self.price = prod['price']
        self.color = prod['color']
        self.made = prod['made']
        self.country = Good.made(self.made)

    @staticmethod
    def made(ean):
        with open('ean.txt', encoding='utf-8') as f:
            for i in f.readlines():
                if i[:3] == ean:
                    country = i[4:]
                    return country


    def __str__(self):
        return '|{:^5}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|'.format(self.num,

                                                                   self.name, self.art,
                                                                      self.price, self.color,
                                                                      self.country)

    def get_num(self):
        return self.num

    def __repr__(self):
        return self.__str__()


class Basket:

    def __init__(self, basket, buyer, date, total):
        self.count = basket[0]
        self.good = basket[1]
        self.cost = basket[2]
        self.buyer = buyer
        self.date = date
        self.total = total

    def buy(self):
        self.total += float(self.cost)
        return self.total

    def _disc(self):
        self.new_total = self.total * 0.9
        return self.new_total

    def down(self):
        return self._disc()

    def _up(self):
        self.new_total = self.total * 1.1
        return self.new_total

    def pr_up(self):
        return self._up()

    def __str__(self):
        return '|{:^5}|{:^25}|{:^15}|{:^25}|{:^10}|'.format(self.count, self.buyer, self.date, self.good, self.cost)

    def __repr__(self):
        return self.__str__()