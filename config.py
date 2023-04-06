import pika


def get_channel():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    channel = connection.channel()
    channel.confirm_delivery()
    return channel


def dead_letter_queue(channel):
    channel.exchange_declare(exchange='dlx')
    queue = channel.queue_declare(queue='dlq', durable=True)
    channel.queue_bind(exchange='dlx', routing_key='hello', queue=queue.method.queue)
    return queue


def get_queue(channel):
    arguments = {
        'x-message-ttl': 10000,
        "x-dead-letter-exchange": "dlx",
        "x-max-length": 5,
        "x-overflow": "reject-publish"
    }

    return channel.queue_declare(queue='hello', durable=True, arguments=arguments)
