from piston.steem import Steem

# vote by tag:

steem = Steem(wif = "wif posting key here")
tagsOrAuthors = ["introduction", "introduceyourself", "introducemyself"]
voteWeight = 0.05

for p in steem.stream_comments():
        for tag in tags:
            try:
                if tag in p["tags"] and p.is_main_post():
                    vote = p.upvote(weight = +voteWeight, voter = "username here")
                    print("Upvoted post by @"+vote["operations"][0][1]["author"]+" using account @"+vote["operations"][0][1]["voter"]+"!")
            except:
                print("Failed to vote on post.")


                
# vote by author:

steem = Steem(wif = "wif posting key here")
tagsOrAuthors = ["zcgolf16", "jesta", "lukestokes"]
voteWeight = 0.05

for p in steem.stream_comments():
        for tag in tags:
            try:
                if tag in p["author"] and p.is_main_post():
                    vote = p.upvote(weight = +voteWeight, voter = "username here")
                    print("Upvoted post by @"+vote["operations"][0][1]["author"]+" using account @"+vote["operations"][0][1]["voter"]+"!")
            except:
                print("Failed to vote on post.")
