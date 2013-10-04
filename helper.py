import pika

class ConnHelper(object):
	count_object = 0
	exchange_list = []

	def __init__(self, host="localhost", nickname="Farthen Dur"):
		self._connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
		self._channel = self._connection.channel()
		self._id = '027-%d' % ConnHelper.count_object
		self._nickname = nickname

		ConnHelper.count_object += 1

		self.register_queue()


	# getter and setter connection
	def get_conn(self):
		return self._connection
	def set_conn(self, value):
		self._connection = value
	def del_conn(self):
		del self._connection
	connection = property(get_conn, set_conn, del_conn, "Connection Properties")

	# getter and setter channel
	def get_ch(self):
		return self._channel
	def set_ch(self, value):
		self._channel = value
	def del_ch(self):
		del self._channel
	channel = property(get_ch, set_ch, del_ch, "Channel Properties")

	# getter and setter id
	def get_id(self):
		return self._id
	def set_id(self, value):
		self._id = value
	def del_id(self):
		del self._id
	id = property(get_id, set_id, del_id, "ID Properties")

	# getter and setter nickname
	def get_nick(self):
		return self._nickname
	def set_nick(self, value):
		self._nickname = value
	def del_nick(self):
		del self._nickname
	nickname = property(get_nick, set_nick, del_nick, "Nickname Properties")

	def register_exchange(self, exchange_name='027-hello'):
		self._channel.exchange_declare(exchange=exchange_name, type='fanout')

	def register_queue(self):
		self._channel.queue_declare(self._id)

	def register_listener(self, callback, no_ack=True):
		self._channel.basic_consume(callback, queue=self._id, no_ack=no_ack)

	def bind_queue_exchange(self, exchange_name='027-hello'):
		self.register_exchange(exchange_name)
		self._channel.queue_bind(exchange=exchange_name, queue=self._id)
		ConnHelper.exchange_list.append(exchange_name)

	def unbind_queue_exchange(self, exchange_name='027-hello'):
		self._channel.queue_unbind(exchange=exchange_name, queue=self._id)
		ConnHelper.exchange_list.remove(exchange_name)

	def publish_message(self, body='Hello World!!'):
		for exchange in ConnHelper.exchange_list:
			send_message(exchange, body)

	def send_message(self, exchange_name='027-hello', body='Hello World!!'):
		self._channel.basic_publish(exchange=exchange_name, routing_key=exchange_name, body='[%s] (%s) %s' % (exchange_name, self._nickname, body))

	def start_consuming(self):
		self._channel.start_consuming()

	def close_connection(self):
		self._connection.close()
