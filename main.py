#!/usr/bin/env python
# coding: utf-8

import InstagramAPI
import time
import random
from instaloader import Post

user = "XXXXXXX"
password = "XXXXXXXX"
media_id = Post.shortcode_to_mediaid("XXXXXXX")
print(media_id)

def auto_sorteo(menciones, media_id, user, password):
    api = InstagramAPI.InstagramAPI(user, password)
    api.login()

    followers = api.getTotalFollowers(api.username_id)
    photo_id = media_id

    count = 0
    lista = []
    try:
        for follower in followers:

            if count == menciones:
                #print("Mandando comentario al sorteo")
                #print(lista)


                comment_text =""
                for x in range (0, len(lista)):
                    comment_text += "@" + lista[x] + " "
                    
                api.comment(photo_id, comment_text)
                print("Mandado comentario al sorteo")
                print(comment_text)
                count = 1
                lista = []
                lista.append(follower)
            else:
                lista.append(follower["username"])
                count += 1

            if followers.index(follower) == (len(followers)-1):
                comment_text =""
                for x in range (0, len(lista)):
                    comment_text += "@" + lista[x] + " "
                api.comment(photo_id, comment_text)
                print("Mandado comentario al sorteo")
                print(comment_text)
            time.sleep(random.randint(1,3))
    except Exception as e:
        print(e)
    return print("Proceso finalizado")

