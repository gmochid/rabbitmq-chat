import pika

class ConnHelper(object):
	def __init__(self, _host="localhost"):
		self._connection = pika.BlockingConnection(pika.ConnectionParameters(host=_host))
		self._channel = self._connection.channel()

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

	def register_queue(self, queue_name='027-hello'):
		self._channel.queue_declare(queue_name)

	def publish_message(self, exchange='', queue_name='027-hello', body='Hello World!!'):
		self._channel.basic_publish(exchange=exchange, routing_key=queue_name, body=body)

	def register_listener(self, callback, queue_name='027-hello', no_ack=True):
		self._channel.basic_consume(callback, queue=queue_name, no_ack=no_ack)

	def start_consuming(self):
		self._channel.start_consuming()

	def close_connection(self):
		self._connection.close()
