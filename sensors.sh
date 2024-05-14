#!/usr/bin/env bash

# stop script on error
set -e

# User defined topic
read -p "Input the topic you wish to publish/subscribe to: " topic
read -p "How many messages do you want to receive? (enter 0 to keep connection open) " count

# run sensor.py app using certificates downloaded in package
printf "\nRunning the sensors application...\n"
python3 sensors.py --endpoint a3rzefpfvv2j7j-ats.iot.us-east-1.amazonaws.com --ca_file root-CA.crt --cert Pi3aPlus.cert.pem --key Pi3aPlus.private.key --client_id basicPubSub --topic sdk/test/$topic --count $count
