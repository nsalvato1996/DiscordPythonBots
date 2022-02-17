#!/bin/sh

kill -9 $(ps aux | grep -e "CoinGeckoCoins.py" | awk '{ print $2 }')