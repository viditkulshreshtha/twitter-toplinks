from django.shortcuts import render,redirect
from .models import model_tweet
from .external_scripts.tweet import get_followers_list,get_user_timeline
from django.views.decorators.csrf import csrf_exempt


def homeview(request):
    return render(request,"index.html",{})



def usernamereq(request):
    if request.method=="POST":

        #retrive username from request.POST method

        username=str(request.POST['username'])
        print(request.POST['username'])


        #get twitter followers list of the given user
        user_follower_list=get_followers_list(username)
        print(user_follower_list)
        len_follower_list=len(user_follower_list)
        request.session['username']=username
        context={}
        context['length']=len_follower_list
        context['followers']=user_follower_list

    return render(request,"friends.html",context)

@csrf_exempt
def friendstweet(request):
    print(request.POST.get('username'))
    friend_username=str(request.POST.get('username'))
    statuses=get_user_timeline(friend_username)
    context={}
    context['tweets']=statuses
    return render(request,"data_table.html",context)



def tweets(request):
    statuses=get_user_timeline(request.session['username'])
    context={}
    context['tweets']=statuses
    for status in statuses:
        tweetlink=str("https://twitter.com/"+str(status.user.screen_name)+"/status/"+str(status.id))
        db_object=model_tweet(user_name=status.user.screen_name,tweet_text=status.text,tweet_link=tweetlink)
        db_object.save()
    return render(request,"data_table.html",context)



    

    



