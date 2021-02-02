import discord
from discord.ext import commands
import praw, random


#session start
f_reddit = praw.Reddit(client_id="YTqKRRXLGfUHLg",
                     client_secret="uUYUKgp9wSPuMf-ge8Oy2ax8F1M",
                     password="Aidenscummins123",
                     user_agent="fortnite1",
                     username="freindlyman1")

print('Reddit logged in as %s' % (f_reddit.user.me()))


#posting function
def post(subreddit:str, title:str, contents:str):
    f_reddit.subreddit(subreddit).submit(title=title, selftext=contents)

#getting urls from a subreddit function
def geturl(subreddit:str, num:int):
    global posts_url
    posts_url = []
    for submission in f_reddit.subreddit(subreddit).new(limit=num):
        posts_url.append(submission.url)


class reddit(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def redditpost(self, ctx, subreddit, title, *, contents):
        "posts to a subreddit"
        post(subreddit=subreddit, title=title, contents=contents)


    @commands.command()
    async def redditread(self, ctx, sub, num:int):
        "reads x num of posts from a subreddit"
        geturl(subreddit=sub, num=num)
        for x in range(0, len(posts_url)):
            await ctx.send(posts_url[x])

def setup(client):
    client.add_cog(reddit(client))