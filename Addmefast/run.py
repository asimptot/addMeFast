import os
import random

array = ['python instaFollow.py', 'python instaLike.py', 'python YoutubeSubscribe.py',
        'python tiktokLike.py', 'python tiktokFollow.py', 'python telegram.py',
        'python soundcloudFollow.py', 'python soundcloudLike.py', 'python facebookLike.py',
         'python facebookFollowers.py', 'python facebookPost.py']

for i in range(90):
    j = random.choice(array)
    os.system(j)
