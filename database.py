class IntNode:
    # def __init__(self, value):
    #     self.value = value
    #     self.next = None

    def __init__(self, value, next):
        self.value = value
        self.next = next

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_value(self, value):
        self.value = value

    def set_next(self, next):
        self.next = next


max = 0
som = 0
count = 0
first = None
for i in range(4, 0, -1):
    first = IntNode(i, first)
temp = first
while temp != None:
    print(temp.get_value())
    if temp.get_value() > max:
        max = temp.get_value()
    count += 1
    som += temp.get_value()
    temp = temp.get_next()

print(f"som:{som}")
print(f"count:{count}")
print(f"max:{max}")


# pass
# first = None
# first = IntNode(3, first)
# first = IntNode(2, first)
# first = IntNode(4, first)
# first = IntNode(2, first)
# first = IntNode(5, first)


# 5
def count_number(first, num):
    counter = 0
    while first != None:
        if num == first.get_value():
            counter += 1
        first = first.get_next()
    return counter


count_number(first, 2)


# 6
def avg(first):
    counter = 0
    total = 0
    while first != None:
        counter += 1
        total += first.get_value()
        first = first.get_next()
    average = total / counter
    return average


# 7
def max_index(first):
    location = 0
    while first != None:
        location += 1
        first = first.get_next()
    return location


# 8
def first_index_num(first, num):
    location = 0
    while first != None:
        location += 1
        if num == first.get_value():
            return location
        first = first.get_next()


# 9
def last_index(first, num):
    location = 0
    last_location = 0
    while first != None:
        location += 1
        if num == first.get_value():
            last_location = location
        first = first.get_next()
    return last_location


#  10
def add_ten(first):
    while first != None:
        first.set_value(first.get_value() + 10)
        first = first.get_next()
    return first


#  11
def div_two(first):
    while first != None:
        first.set_value(first.get_value() / 2)
        first = first.get_next()
    return first


# 12
def add_val(first, val):
    while first != None:
        first.set_value(first.get_value() + val)
        first = first.get_next()
    return first


# 13

def check_update_val(first, val):
    while first != None:
        if val <= first.get_value():
            first.set_value(first.get_value() * 2)
        else:
            first.set_value(first.get_value() / 2)
            first = first.get_next()
    return first
