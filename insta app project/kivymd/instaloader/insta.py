import instaloader as insta

loader = insta.Instaloader()

##user = input("Enter user id : ")

# mod.download_profile(user,profile_pic_only=True)


# Login using the credentials
# loader.login(USER, PASSWORD)

# Use Profile class to access metadata of account
profile = loader.Profile.from_username(loader.context,
                                       '__rizwan_13')


