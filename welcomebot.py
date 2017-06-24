from piston.steem import Steem
import time
from piston.post import Post
import os
import json

steem = Steem(wif = "private key here")
tags = ["introduction", "introduceyourself", "introducemyself"]
past_authors = []



for p in steem.stream_comments():
    for x in tags:
        try:
            if x in p["tags"] and p.is_opening_post() and p["author"] not in past_authors:
                print(p.get_comments())
                print(p["author"])
                post = p.reply(body = "message here", author = "username here")
                p.upvote(weight=+0.01, voter = "username here")
                print(post)
                past_authors.append(post['operations'][0][1]['parent_author'])
                time.sleep(20)
                print(past_authors)

        except:
            print("Failed to comment on post.")
