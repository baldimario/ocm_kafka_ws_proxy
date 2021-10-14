#!/usr/bin/python
# pip install kafka-python
from kafka import KafkaConsumer
from kafka import KafkaProducer
import json
import argparse
import time

DEFAULT_BROKER = '127.0.0.1:9092'
parser = argparse.ArgumentParser(description='Kafka tester.')
parser.add_argument('--producer', action='store_true', help='Producer mode')
parser.add_argument('--consumer', action='store_true', help='Consumer mode')
parser.add_argument('--topic', action='store', type=str, default="topic", help='Topic')
parser.add_argument('--group', action='store', type=str, default="group", help='Group for Consumer')
parser.add_argument('--broker', action='store', type=str, default=DEFAULT_BROKER, help='Group for Consumer')
parser.add_argument('--message', action='store', type=str, default='Mario', help='Message for Producer')
parser.add_argument('--iterations', action='store', type=int, default=1, help='Message iterations for Producer')
parser.add_argument('--frequency', action='store', type=int, default=1, help='Message frequency for Producer')
args = parser.parse_args()              

def check_arg(args, params):
	for param in params:
		if not vars(args)[param]:
			print(f'Missing {param}')
			exit(0)
		
if args.consumer:
	check_arg(args, ['topic', 'group', 'broker'])
	
	consumer = KafkaConsumer(args.topic, bootstrap_servers=[args.broker],
		 enable_auto_commit=True,
		 group_id=args.group,
		 auto_offset_reset='latest'
 		)
	
	c = 0
	for message in consumer:
		data = json.loads(message.value)
		print (c, data)
		c += 1

if args.producer:
	check_arg(args, ['topic', 'broker', 'message', 'iterations', 'frequency'])
	producer = KafkaProducer(bootstrap_servers=[args.broker],
		value_serializer=lambda x: json.dumps(x).encode('utf-8')
	)
	
	def produce(args, i):
		producer.send(args.topic, value='{}: {}'.format(i, args.message))
		print('.')
		time.sleep(1/args.frequency) #dt

	if args.iterations > 0:		
		for i in range(args.iterations):
			produce(args, i)
	
	if args.iterations < 0:
		i = 0
		while True:
			produce(args, i)
			i += 1
