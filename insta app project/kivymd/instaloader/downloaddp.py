import instaloader

dp = instaloader.Instaloader()

username = input("Enter username : ")

dp.download_profile(username,profile_pic_only=True)