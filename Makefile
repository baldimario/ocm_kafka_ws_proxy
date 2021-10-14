.DEFAULT_GOAL := help
SHELL := /bin/bash

help:
	@echo -e "$$(grep -hE '^\S+:.*##' $(MAKEFILE_LIST) | sed -e 's/:.*##\s*/:/' -e 's/^\(.\+\):\(.*\)/\\x1b[36m\1\\x1b[m:\2/' | column -c2 -t -s :)"

up: ## start containers
	docker-compose -f .docker/docker-compose.yaml up -d
down: ## stop containers
	docker-compose -f .docker/docker-compose.yaml down
build: ## build containers
	docker-compose -f .docker/docker-compose.yaml build
ps: ## list containers
	docker-compose -f .docker/docker-compose.yaml ps
node: ## enter in node container
	docker exec -it ocm_node /bin/bash
python: ## enter in python container
	docker exec -it ocm_python /bin/bash
websocket: ## consume on websocket (wscat)
	docker exec -it ocm_node wscat -c 'ws://127.0.0.1:9999/?topic=test&consumerGroup=ocm_ws_group'
produce: ## produce on python
	docker exec -it ocm_python python kafka-tester.py --producer --broker ocm_kafka:9092 --iterations 1000 --frequency 1 --topic test --message Ciao 
consume: ## consume on python
	docker exec -it ocm_python python kafka-tester.py --consumer --broker ocm_kafka:9092 --group ocm_group --topic test 