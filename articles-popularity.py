#!/usr/bin/env python

import redis

#r = redis.Redis(host='localhost',)

# You can configure the Redis client to automatically convert responses from bytes obj to strings
# NOTE: it just does this for print output it doesn't actually change the byte obj into a string!!!
r = redis.Redis(host='localhost', charset="utf-8", decode_responses=True)

def upVote(id):
    key = "article:" + id + ":votes"
    r.incr(key)

def downVote(id):
    key = "article:" + id + ":votes"
    r.decr(key)

def showResults(id):
    headlineKey = "article:" + id + ":headline"
    voteKey = "article:" + id + ":votes"
    #for headline, vote in r.mget([headlineKey, voteKey]):
    for headline, vote in r.mget(headlineKey, voteKey):
        print('The article ' + str(headline,'utf-8') + ' has ' + str(vote,'utf-8') + 'votes')

if __name__ == "__main__":

    showResults('12345')
