class Coffee:
    def __init__(self, name, kind, strength, price):
        self.name = name
        self.kind = kind
        self.strength = strength
        self.price = price


def same_products(crr):
    same = crr[0].name
    for one in crr:
        if one.name != same:
            return False
    return True


def weak_sorts(crr, num):
    new_list = []
    for one in crr:
        if one.strength < num:
            new_list.append(one.kind)
    return new_list


def most_expensive(crr):
    big_price = 0
    for one in crr:
        if one.price > big_price:
            big_price = one.price
    for one in crr:
        if one.price == big_price:
            print(f"name: {one.name}\n"
                  f"kind: {one.kind}\n"
                  f"strength: {one.strength}\n"
                  f"price: {one.price}")


a = Coffee("aa", "aaaa", 1, 1)
b = Coffee("bb", "bbbb", 2, 2)
c = Coffee("cc", "cccc", 4, 4)
d = Coffee("dd", "dddd", 5, 0)

crr = [a, b, c, d]
most_expensive(crr)
print(weak_sorts(crr,3))
