class User:
    def __init__(self,user_id,username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    
    def follow(self,user):
        user.followers += 1
        self.following += 1
        
    def unfollow(self,user):
        user.followers -= 1
        self.following -= 1

user_1 = User(user_id="001",username="angela")
user_2 = User(user_id="002",username="alp")

user_1.follow(user_2)

print(f"user_1 followers: {user_1.followers}")
print(f"user_1 following: {user_1.following}")
print(f"user_2 followers: {user_2.followers}")
print(f"user_2 following: {user_2.following}")