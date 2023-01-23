#!/usr/bin/env python
# coding: utf-8

import InstagramAPI
import time
import random
from instaloader import Post


#Set user, password and shortcode
#Shortcode is like this https://www.instagram.com/p/Cl3nnL2oVrT/

#Yo only neeed tu put the final part --> Cl3nnL2oVrT


user = "XXXXXXX"
password = "XXXXXXXX"
media_id = Post.shortcode_to_mediaid("XXXXXXX")
print(media_id)


#Function to send messages based on the number of mentions, media_id, user and password
def auto_sorteo(menciones, media_id, user, password):
    
    #log into instagram, may be the first time you need to battle with a instagram challange
    api = InstagramAPI.InstagramAPI(user, password)
    api.login()
    
    #Get the followers of your user
    followers = api.getTotalFollowers(api.username_id)
    photo_id = media_id
    
    #Set a vanilla counter and list to apply the number of mentions
    count = 0
    lista = []
    try:
        for follower in followers:
            #Send message if the number of followers in the list is the same as the initial mentions
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
                lista.append(follower["username"])
            #If not, add the follower to the list
            else:
                lista.append(follower["username"])
                count += 1
            #Send the final list of followers
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

