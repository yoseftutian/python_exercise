class Clock:
    def __init__(self, hour, min):
        self.hour = hour
        self.min = min


def get_interval(time):
    return (24 - time.hour) * 60 + time.min


def compare_landings(flight_1, flight_2):
    interval1 = get_interval(flight_1)
    interval2 = get_interval(flight_2)

    if interval1 < interval2:
        return f"Flight 1 is scheduled to land later than Flight 2."
    elif interval2 < interval1:
        return f"Flight 2 is scheduled to land later than Flight 1."
    else:
        return "Both flights are scheduled to land at the same time."


flight_1 = Clock(19, 50)
flight_2 = Clock(21, 30)
result = compare_landings(flight_1, flight_2)
print(result)

class Petek:
    def __init__(self, party_char, party_name):
        self._party_char = party_char
        self._party_name = party_name

    def get_party_char(self):
        return self._party_char

    def set_party_char(self, party_char):
        if party_char in ['A', 'B', 'L', 'Y']:
            self._party_char = party_char
        else:
            print("Invalid party character. Please choose from A, B, L, or Y.")

    def get_party_name(self):
        return self._party_name

    def set_party_name(self, party_name):
        self._party_name = party_name


# Example usage
petek_instance = Petek('B', 'Blue Party')
print(f"Party character: {petek_instance.get_party_char()}")
print(f"Party name: {petek_instance.get_party_name()}")
