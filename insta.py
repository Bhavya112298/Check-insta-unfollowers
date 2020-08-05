import instaloader

ig = instaloader.Instaloader()


# Login into instagram

ig.login('@myusername', 'mypassword')



# Obtain profile metadata
# mention the account name whose unfollowers are to be checked. eg: it is same as username without '@'
person = 'myusername'
profile = instaloader.Profile.from_username(ig.context, person)


   

# list of followers
my_followers = []
for follower in profile.get_followers():
    username = follower.username
    my_followers.append(username)


#list of following
my_following = []
for followee in profile.get_followees():
    username = followee.username
    my_following.append(username)




for followee in my_following:
    if followee not in my_followers:
        print(followee)

            


