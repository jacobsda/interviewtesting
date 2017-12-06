import redis

#redisClient = redis.Redis(host='localhost', charset="utf-8", decode_responses=True)

class Queue(object):

    def __init__(self, queueName, redisClient ):
        self.qn = queueName
        #print(self.qn)

        """The default connection parameters are: host='localhost' """
        #self.r =  redis.Redis(**redis_kwargs)
        self.r = redisClient
        self.queueKey = '%s:%s' %('queue',self.qn)
        self.timeout = 0


    def size(self):
        return self.r.llen(self.queueKey)


    def push(self, data):
        self.r.lpush(self.queueKey, data)
        #print (self.queueKey)

    def pop(self):
       item = self.r.brpop(self.queueKey, self.timeout)
       if item:
         """ item is either nil or a 2-element array where [0] is the name of the key, [1] is the value"""
         item = item[1]
       return item

#redisClient.quit()
