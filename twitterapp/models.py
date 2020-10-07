from django.db import models



class model_tweet(models.Model): 
    user_name = models.CharField(max_length = 200) 
    tweet_link = models.CharField(max_length = 200)
    tweet_text = models.CharField(max_length = 500)
    

    
