# class Taxi:
#     def __init__(self, taxi_ld, driver_name, num_pass=4):
#         self._taxi_ld = taxi_ld
#         self._driver_name = driver_name
#         self._num_pass = num_pass
#         self._available = True
#
#     def get_id(self):
#         return self._taxi_ld
#
#     def set_id(self, taxi_ld):
#         self._taxi_ld = taxi_ld
#
#     def get_name(self):
#         return self._driver_name
#
#     def set_name(self, driver_name):
#         self._driver_name = driver_name
#
#     def get_num_pass(self):
#         return self._num_pass
#
#     def set_num_pass(self, num_pass):
#         self._num_pass = num_pass
#
#     def is_available(self):
#         return self._available
#
#     def set_available(self, available):
#         self._available = available
#
#     def taxi_busy(self):
#         self._available = False
#
#
# class Taxi_station:
#     def __init__(self, name_station):
#         self.name_station = name_station
#         self.num_taxis = 0
#         self.taxis = []
#
#     def add_taxi(self, driver_name, taxi_id, num_pass):
#         if self.num_taxis < 80:
#             self.taxis.append(Taxi(driver_name, taxi_id, num_pass))
#             self.num_taxis += 1
#         else:
#             print("Taxi station is full.")
#
#     def get_taxi(self, num_passengers):
#         for taxi in self.taxis:
#             if taxi.is_available() and (taxi.get_num_pass() - num_passengers) >= 0:
#                 taxi.taxi_busy()
#             else:
#                 continue
#             return taxi
#         return None  # no taxi found
#
#
# if __name__ == "__main__":
#     station = Taxi_station("Central Station")
#     station.add_taxi("Yoel", "2626", 4)
#     station.add_taxi("Haim", "2000", 8)
#     station.add_taxi("Baruch", "88-88", 2)
#
#     number_of_people = int(input("Enter number of people >>> "))
#     taxi = station.get_taxi(number_of_people)
#
#     if taxi:
#         print("Taxi found: ")
#         print("ID: ", taxi.get_id())
#         print("Driver: ", taxi.get_name())
#         print("Capacity: ", taxi.get_num_pass())
#     else:
#         print("No taxi available")
#


import sys


# print(sys.maxsize) = 2^63-1

class Taxi:
    def __init__(self, driver_name, taxi_id, num_pass=4):
        self.__taxi_id = taxi_id
        self.__driver_name = driver_name
        self.__num_pass = num_pass
        self.__available = True

    @property
    def id(self):
        return self.__taxi_id

    @property
    def name(self):
        return self.__driver_name

    @property
    def num_pass(self):
        return self.__num_pass

    @property
    def available(self):
        return self.__available

    def taxi_busy(self):
        self.__available = False


class TaxiStation:
    def __init__(self, station_name):
        self.__station_name = station_name
        self.__num_taxies = 0
        self.__taxies = []

    @property
    def station_name(self):
        return self.__station_name

    @property
    def num_taxies(self):
        return self.__num_taxies

    def add_taxi(self, driver_name, taxi_id, num_pass):
        if self.__num_taxies < 80:
            self.__taxies.append(Taxi(driver_name, taxi_id, num_pass))  # anonymous
            self.__num_taxies += 1
        else:
            print("Taxi station is full.")

    def get_taxi(self, num_passengers):
        closest_taxi = None
        min_difference = sys.maxsize  # int max size in Python

        # finding the closest taxi available with similar capacity to user's request
        for taxi in self.__taxies:
            if taxi.available and taxi.num_pass >= num_passengers:
                difference = abs(taxi.num_pass - num_passengers)
                if difference < min_difference:
                    closest_taxi = taxi
                    min_difference = difference

        if closest_taxi:  # does such a taxi exist?
            closest_taxi.taxi_busy()
            return closest_taxi
        else:
            return None


if __name__ == "__main__":
    station = TaxiStation("Central Station")
    station.add_taxi("Rabi", "00-11002-2", 4)
    station.add_taxi("M-M", "11-22-33", 18)
    station.add_taxi("Rahman and sons", "99-999-99", 7)

    number_of_people = int(input("Enter number of passengers >>> "))
    taxi = station.get_taxi(number_of_people)

    if taxi:
        print("\nA taxi for you is on its way!")
        print("\nTaxi Details: ")
        print("\tID:", taxi._Taxi__taxi_id)  # name_mangling !!!!!!!!
        print("\tDriver's name:", taxi.name)  # property
        print("\tCapacity:", taxi.num_pass)  # property
    else:
        print("Sorry, no taxi available at this time.")
