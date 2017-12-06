#!/usr/bin/env python

import redis
r = redis.Redis(host='localhost',)

r.set("my_key", "Hello World using Python and Redis")
r.get("my_key")


