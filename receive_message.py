#!/usr/bin/env python
import pika, sys, os

import config
from config import *


def main(channel):
    print(f"Message count is: {config.get_queue(channel).method.message_count}")
    print(f"Dead messages count is: {config.dead_letter_queue(channel).method.message_count}")

    def callback(ch, method, properties, body):
        # ch.basic_reject(method.delivery_tag)
        print(" [x] Received %r" % body)

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main(config.get_channel())
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
