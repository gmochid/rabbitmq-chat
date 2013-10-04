import pika
import logging
from helper import ConnHelper

# log configuration
logging.basicConfig()

# create connection to server
connhelper = ConnHelper()

def createUser():
	print 'Not yet implemented'

def changeNickname():
	print 'Not yet implemented'

def joinGroup():
	print 'Not yet implemented'

def leaveGroup():
	print 'Not yet implemented'

def sendChatToAllGroup():
	print 'Not yet implemented'

def sendChatToGroup():
	print 'Not yet implemented'

if __name__ == '__main__':
	user_input = raw_input('>> ')
	while user_input != '/EXIT':
		params = user_input.split(' ')
		user_input = raw_input('>> ')
