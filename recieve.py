import pika

connection = pika.BlockingConnection(pika.URLParameters('amqp://nowzklsc:Rv3YwrPwxmYxNSKOrK7LGuE5YtbtVv2d@shark.rmq.cloudamqp.com/nowzklsc'))
channel = connection.channel()

channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
	print(" [x] Received %r" % body)


channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
