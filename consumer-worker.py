import redis
import dhjqueue

r = redis.Redis(host='localhost',)

logsQueue  = dhjqueue.Queue('logs', r)

def logMessages():
    replies = logsQueue.pop()
    if replies:
        queueName = replies[0]
        message = replies[1]
    else:
        print("the pop is broken")
        return None

    print("[consumer] Got log: %s" % str(message)) 
    print("%s logs left" % str(logsQueue.size()))

    # Recursively call itself
    logMessages()


if __name__ == "__main__":
    logMessages()
