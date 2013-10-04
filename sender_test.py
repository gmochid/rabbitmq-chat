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

# declaring a new queue
connhelper.register_queue()

def publish(text):
	connhelper.publish_message(body=text)
	print "[x] sent %s" % text

text = raw_input('Send message : ')
publish(text)

connhelper.close_connection()
