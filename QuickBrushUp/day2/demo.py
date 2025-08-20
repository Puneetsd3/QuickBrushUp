from models import UserDAO, PostDAO

user = UserDAO.create("newuser")
print("Created:", user)

fetched = UserDAO.fetch(user.id)
print("Fetched:", fetched)

users = UserDAO.list()
print("All users:", users)

post = PostDAO.create(user.id, "Hello day2!")

print("Created Post:", post)

postfetched = PostDAO.fetch(post.id)
print("Fetched Post:", postfetched)

posts = PostDAO.list()
print("All posts:", posts)

