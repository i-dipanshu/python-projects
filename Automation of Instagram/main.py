from instabot import Bot

bot = Bot()

usr = input("Enter your username: ")
psd = input("Enter your password: ")

bot.login(username="usr", password="psd")

tofollow = input("Enter the username of the account to follow: ")

followers = bot.get_user_followers(usr)
for follower in followers:
    print(follower)
    
user = usr

bot.send_message("You are Done !!! ", [user])