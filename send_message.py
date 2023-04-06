#!/usr/bin/env python
import pika.exceptions

import config
from config import *
import logging

#logging.basicConfig(level=logging.DEBUG)


def send_message(channel):
    try:
        publish = channel.basic_publish(exchange='', routing_key='hello', body=str.encode('Hello World!'),
                                        properties=pika.BasicProperties(
                                            delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE))
        print(publish)
    except pika.exceptions.NackError as e:
        print(e)


if __name__ == '__main__':
    channel = config.get_channel()
    config.dead_letter_queue(channel)
    send_message(channel)
