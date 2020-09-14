import os
import random

array = ['python instaFollow.py', 'python instaLike.py', 'python YoutubeSubscribe.py',
        'python tiktokLike.py', 'python tiktokFollow.py', 'telegram.py', 'soundcloudFollow.py', 'soundcloudLike.py']

for i in range(90):
    j = random.choice(array)
    os.system(j)
