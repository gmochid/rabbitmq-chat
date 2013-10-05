import thread
import pika
import logging
from helper import ConnHelper

# log configuration
logging.basicConfig()

def changeNickname(client, new_nickname):
	client.nickname = new_nickname

def joinGroup(client, group_name):
	client.bind_queue_exchange(group_name)

def leaveGroup(client, group_name):
	client.unbind_queue_exchange(group_name)

def sendChatToAllGroup(client, body):
	client.publish_message(body)

def sendChatToGroup(client, group_name, body):
	client.send_message(group_name, body)

def callbackIncomingChat(ch, method, properties, body):
	print " >> %s" % body

if __name__ == '__main__':
	
	client = ConnHelper()
	client.register_listener(callbackIncomingChat)
	thread.start_new_thread(client.start_consuming, ())

	print " [*] Created user with id = %s and nickname = %s" % (client.id, client.nickname)

	user_input = raw_input('')

	while user_input != '/EXIT':
		params = user_input.split(' ')

		if params[0] == '/NICK':
			changeNickname(client, params[1:])
			print ' [*] Nickname changed into %s' % client.nickname
		elif params[0] == '/JOIN':
			joinGroup(client, params[1])
			print ' [*] Joined to group %s' % params[1]
		elif params[0] == '/LEAVE':
			leaveGroup(client, params[1])
			print ' [*] Leaved to group %s' % params[1]
		elif params[0][0] == '@':
			sendChatToGroup(client, string.replace(params[0], '@', ''), params[1:])
		else:
			sendChatToAllGroup(client, params)
			print ' [*] Sent message to all group joined'

		user_input = raw_input('')
