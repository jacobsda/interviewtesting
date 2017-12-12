import redis
import dhjqueue

r = redis.Redis(host='localhost',)

logsQueue  = dhjqueue.Queue('logs', r)
MAX = 5
for i in range(1,MAX+1):
    logsQueue.push("Hello World %s" % str(i))

print("Created %s logs"%str(MAX))

