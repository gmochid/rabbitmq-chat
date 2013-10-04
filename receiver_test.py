import pika
import logging
from helper import ConnHelper

logging.basicConfig()

# create connection to server
'''
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
'''
connhelper = ConnHelper()

connhelper.register_exchange()
connhelper.bind_queue_exchange()

print "[*] Waiting for message..."

def callback(ch, method, properties, body):
	print "[x] Received %r" % body

connhelper.register_listener(callback)

connhelper.start_consuming()
