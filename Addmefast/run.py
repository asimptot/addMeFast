import os
import random

#array = ['python YoutubeSubscribe.py', 'python tiktokLike.py', 'python tiktokFollow.py', 'python soundcloudFollow.py',
         #'python soundcloudLike.py']

'''
for i in range(120):
    j = random.choice(array)
    os.system(j)
'''

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

array = [YoutubeSubscribe, TiktokFollow, TiktokLike, SoundCloudFollow, SoundCloudLike]

for i in range(120):
    random.choice(array)()

#random.choice(array)

