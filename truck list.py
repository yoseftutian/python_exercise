
class Truck:
    def __init__(self, truck_id, driver_name, num_storage):
        self._truck_id = truck_id
        self.driver_name = driver_name
        self._num_storage = num_storage
        self._is_free = True  # default arg.

    def get_is_free(self):
        return self._is_free

    def set_is_free(self, is_free):
        self._is_free = is_free

    def get_num_storage(self):
        return self._num_storage

    def set_num_storage(self, num_storage):
        self._num_storage = num_storage

    def get_truck_id(self):
        return self._truck_id


def print_free_truck_and_drivers(trucks):
    for truck in trucks:
        if truck.is_free and truck.num_storage >= 7:
            print(truck.driver_name)


def get_free_truck_with_max_storage(trucks):
    max_storage_truck = None
    max_storage = 0

    for truck in trucks:
        if truck.get_is_free() and truck.get_num_storage() >= max_storage:
            max_storage_truck = truck
            max_storage = truck.get_num_storage()

    if max_storage_truck is not None:
        return max_storage_truck.get_truck_id()
    else:
        print("No free truck with storage available.")
        return None


# Example
truck_01 = Truck("truck_1", "chaim", 8)
truck_02 = Truck("truck_2", "Yossi", 9)
truck_03 = Truck("truck_3", "Yoel", 20)

truck_station_list = [truck_01, truck_02, truck_03]
# for t in truck_station_list:
#     t.set_is_free(False)

result = get_free_truck_with_max_storage(truck_station_list)
print(result)
