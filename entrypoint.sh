#!/bin/bash

DATADIR="./l1-data"
GENESIS="./genesis.json"

# Initialize blockchain
if [ ! -d "$DATADIR/geth" ]; then
  geth --datadir $DATADIR init $GENESIS
fi

# Start Geth node
geth --datadir $DATADIR \
  --networkid 1888 \
  --http --http.addr "0.0.0.0" --http.port 9545 \
  --http.api "eth,net,web3,personal,miner" \
  --mine --miner.threads=2 \
  --syncmode full \
  --authrpc.port 9551 \
  --authrpc.vhosts "*" \
  --http.corsdomain "*" \
  --allow-insecure-unlock \
  --verbosity 3
