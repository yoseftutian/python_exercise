class Beverage:
    def __init__(self, name="unknown name", alcohol=-1, components="unknown components", price=-1.0):
        self.__name = name
        if 0 <= alcohol <= 100:
            self.__alcohol = alcohol
        else:
            self.__alcohol = -1  # it's not my fault...
        self.__components = components
        self.__price = price

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_alcohol(self):
        return self.__alcohol

    def set_alcohol(self, alcohol):
        if 0 <= alcohol <= 100:
            self.__alcohol = alcohol
        else:
            print("Illegal value! updating to -1")

    def get_components(self):
        return self.__components

    def set_components(self, components):
        self.__components = components

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def display(self):
        print(f"\nName: {self.__name}\nAlcohol: {self.__alcohol}\nComponents: {self.__components}\nPrice: {self.__price}")


def display_higher_alcohol(b1, b2):
    print("the drink with the higher alcohol amount is: ", end="")
    if b1.get_alcohol() > b2.get_alcohol():
        b1.display()
    else:
        b2.display()


def set_new_price(b):
    if b.get_alcohol() < 1:  # an annoying person walks into a bar...
        b.set_price(b.get_price() * 1.05)


def display_components(b):
    components = b.get_components()
    for component in components.split(','):
        print(component + ", ", end="")


if __name__ == "__main__":
    # b1 = Beverage("Beer", 0, "water, bread", 10)
    # print("Price, for normal people: ")
    # print(b1.get_price())

    # set_new_price(b1)
    # print("Price, after: ")
    # print(b1.get_price())

    b2 = Beverage("Cobra", -10, "rum, tequila, vodka, cola", 12)
    # display_higher_alcohol(b1, b2)
    # print(b2.get_price())
    # set_new_price(b2)
    # print(b2.get_price())
    b2.set_alcohol(-5)
    print(b2.display())
