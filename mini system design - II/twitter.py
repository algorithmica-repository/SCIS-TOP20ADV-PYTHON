import sys
import random

class Tweet():
    def __init__(self, text, ts):
        self.text = text
        self.ts = ts
    def __repr__(self):
        return "(" + self.text + "," + str(self.ts) + ")"
        
class MiniTwitter():
    def __init__(self):
        self.tweets = {}
        self.followers = {}
        self.followees = {}
    
    def postTweet(self, user_id, tweet_text, ts):
        user_tweets = self.tweets.get(user_id)
        if(user_tweets == None):
            user_tweets = []
            self.tweets[user_id] = user_tweets
        user_tweets.append(Tweet(tweet_text, ts))
    
    def follow(self, follower_id, followee_id):
        user_followers = self.followers.get(followee_id)
        if(user_followers == None):
            user_followers = set()
            self.followers[followee_id] = user_followers
        user_followers.add(follower_id)
    
        user_followees = self.followees.get(follower_id)
        if(user_followees == None):
            user_followees = set()
            self.followees[follower_id] = user_followees
        user_followees.add(followee_id)
        
    def unfollow(self, follower_id, followee_id):
        user_followers = self.followers.get(followee_id)
        if(user_followers != None):
            user_followers.remove(follower_id)
            
        user_followees = self.followees.get(follower_id)
        if(user_followees != None):
            user_followees.remove(followee_id)
            
    def timeline(self, user_id):
        user_tweets = self.tweets.get(user_id)
        if(user_tweets == None):
            return None
        
        res = []
        n = len(user_tweets)
        ntweets = min(10, n)
        for i in range(ntweets):
            res.append(user_tweets[n-1-i])
        return res
        
    def newsfeed(self, user_id):
        #get the feed of given user
        feed = self.timeline(user_id)
        if(feed == None):
           feed = []
           
        #get the feed of followees 
        followees = self.followees.get(user_id)
        for followee in followees:
             tmp = self.timeline(followee)
             for t in tmp:
                 feed.append(t)
        
        #sort the complete feed by timestamp
        feed = sorted(feed, key=lambda t:t.ts, reverse=True)
        
        res = []
        n = len(feed)
        ntweets = min(10, n)
        for i in range(ntweets):
            res.append(feed[i])
        return res

def main():
    twitter = MiniTwitter()
    n_users = 5
    for ts in range(100):
        rid = random.randint(0,4)
        twitter.postTweet("user"+str(rid), "tweet"+str(rid)+"_"+str(ts), ts)
    for i in range(n_users):
        print("user"+str(i), twitter.timeline("user"+str(i)))
    twitter.follow("user0", "user1")
    twitter.follow("user1", "user2")
    twitter.follow("user0", "user2")
    print(twitter.newsfeed("user0"))
    
if __name__=="__main__":
    main()
