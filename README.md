# [POC] OCM_KAFKA_WS_PROXY

## Installation

```sh
$ make build
```

## Start/Stop development environment

```sh
$ make up
$ make down
```

## Test the environment

### Start producer 

```sh
$ make produce
```

### Start consumer via websockets

```sh
make websocket
```

## Endpoint
websocket endpoint: `ws://localhost:9999`
