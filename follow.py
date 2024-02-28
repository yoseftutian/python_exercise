class User:
    def __init__(self, userID, username):
        self.id = userID
        self.username = username
        # default values
        self.followers = 0
        self.following = 0

    def follow(self, whats_his_name):
        self.following += 1
        whats_his_name.followers += 1


user_1_chaim = User("1234", "Chaim")
user_2_ben = User("5678", "Beneath")
user_3_yosef = User("1959", "yosef")
user_4_ally = User("5767","ally")

user_4_ally.follow(user_3_yosef)
user_2_ben.follow(user_1_chaim)
print(user_2_ben.following)
print(user_1_chaim.followers)
print(user_4_ally.following)
print(user_3_yosef.followers)

