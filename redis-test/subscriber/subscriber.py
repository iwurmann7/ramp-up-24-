import redis

def run_subscriber():

    redis_connection = redis.Redis(host='redis', port=6379)
    pubsub_system = redis_connection.pubsub()
    pubsub_system.subscribe('notification_channel')

    print("Subscribed to 'notification_channel'. Waiting for messages...")


    for message in pubsub_system.listen():
        if message['type'] == 'message':
            print(f"Received message: {message['data'].decode('utf-8')}")

if __name__ == "__main__":
    run_subscriber()