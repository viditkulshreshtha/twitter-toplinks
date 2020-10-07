import tweepy 

consumer_key = "uvMdKjXtlnQ2s1G55ut12WffM" 
consumer_secret = "nEqQf3dYZMn6cpYSurXxDAZ99WY2DOxgNBdQh2n3c95Fcer5de" 
access_token = "1151939110690406400-vybKYIf94efxmHVIyaCorznauEAboj" 
access_token_secret = "CLiG11VawIeV1qFERCA1v7D0F4VrxRq9Ryski8fW4p433" 

def get_followers_list(twitter_username):



    #set up the API
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
    
    auth.set_access_token(access_token, access_token_secret) 
    
    api = tweepy.API(auth) 
    
    #method to fetch the followers of the user
    screen_name = str(twitter_username)
    followers_list=[]
    for follower in api.followers(screen_name): 
        print(follower.screen_name)
        followers_list.append(follower.screen_name)
    return followers_list


def get_user_timeline(twitter_username):
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
    
    auth.set_access_token(access_token, access_token_secret) 
    
    api = tweepy.API(auth) 
    
    #method to get the timeline of the user
    screen_name = str(twitter_username)
    statuses = api.user_timeline(screen_name, count = 50) 
    return statuses
    
    