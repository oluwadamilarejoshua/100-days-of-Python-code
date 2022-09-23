class User:

    def __init__(self, user_id, username, gender):
        self.id = user_id
        self.username = username
        self.gender = gender
        self.follower = 0
        self.following = 0

    def follow(self, user):
        user.follower += 1
        self.following += 1


user_1 = User("001", "Timmy", "male")
user_2 = User("002", "Tommy", "female")
print(f"{user_1.username}'s gender is {user_1.gender}")
print(f"{user_2.username}'s gender is {user_2.gender}")

user_1.follow(user_2)
print(f"{user_1.username} follows {user_1.following} other user(s)")
print(f"{user_2.username} has {user_2.follower} follower(s)")
