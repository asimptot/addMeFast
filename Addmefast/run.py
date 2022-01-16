import os
import random

def YoutubeSubscribe():
    os.system('D:')
    os.chdir(r'D:\\Projects\\Sosyal\\Addmefast\\Youtube')
    os.system('python YoutubeSubscribe.py')

def YoutubeWatch():
    os.system('D:')
    os.chdir(r'D:\\Projects\\Sosyal\\Addmefast\\Youtube')
    os.system('python YoutubeWatch.py')

def TiktokLike():
    os.system('D:')
    os.chdir(r'D:\\Projects\\Sosyal\\Addmefast\\Tiktok')
    os.system('python tiktokLike.py')

def TiktokFollow():
    os.system('D:')
    os.chdir(r'D:\\Projects\\Sosyal\\Addmefast\\Tiktok')
    os.system('python tiktokFollow.py')

def SoundCloudLike():
    os.system('D:')
    os.chdir(r'D:\\Projects\\Sosyal\\Addmefast\\Soundcloud')
    os.system('python soundcloudLike.py')

def SoundCloudFollow():
    os.system('D:')
    os.chdir(r'D:\\Projects\\Sosyal\\Addmefast\\Soundcloud')
    os.system('python soundcloudFollow.py')

def InstaLike():
    os.system('D:')
    os.chdir(r'D:\\Projects\\Sosyal\\Addmefast\\Instagram')
    os.system('python instaLike.py')

def InstaFollow():
    os.system('D:')
    os.chdir(r'D:\\Projects\\Sosyal\\Addmefast\\Instagram')
    os.system('python instaFollow.py')

def FacebookFollow():
    os.system('D:')
    os.chdir(r'D:\\Projects\\Sosyal\\Addmefast\\Facebook')
    os.system('python facebookFollowers.py')

def FacebookLike():
    os.system('D:')
    os.chdir(r'D:\\Projects\\Sosyal\\Addmefast\\Facebook')
    os.system('python facebookLike.py')

def TwitchFollow():
    os.system('D:')
    os.chdir(r'D:\\Projects\\Sosyal\\Addmefast\\Twitch')
    os.system('python twitch.py')

def PinterestSave():
    os.system('D:')
    os.chdir(r'D:\\Projects\\Sosyal\\Addmefast\\Pinterest')
    os.system('python pinterestSave.py')

def TweetFollow():
    os.system('D:')
    os.chdir(r'D:\\Projects\\Sosyal\\Addmefast\\Twitter')
    os.system('python tweetFollow.py')

def TweetLike():
    os.system('D:')
    os.chdir(r'D:\\Projects\\Sosyal\\Addmefast\\Twitter')
    os.system('python tweetLike.py')

def RedditMembers():
    os.system('D:')
    os.chdir(r'D:\\Projects\\Sosyal\\Addmefast\\Reddit')
    os.system('python RedditMembers.py')

def RedditUpvote():
    os.system('D:')
    os.chdir(r'D:\\Projects\\Sosyal\\Addmefast\\Reddit')
    os.system('python RedditUpvote.py')

array = [YoutubeSubscribe, TiktokFollow, TiktokLike, SoundCloudFollow, SoundCloudLike, InstaFollow, InstaLike,
         FacebookFollow, FacebookLike, PinterestSave, TweetFollow, TweetLike, RedditMembers]

#array = [YoutubeSubscribe, TiktokFollow, TiktokLike, SoundCloudFollow, SoundCloudLike, InstaFollow, InstaLike,
#         PinterestSave, TweetFollow, TweetLike, RedditMembers]

for i in range(240):
    random.choice(array)()