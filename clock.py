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


