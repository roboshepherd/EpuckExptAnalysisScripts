#!/bin/bash
cat dbus-log.txt | grep TaskInfo > TaskServerSignals.log 
START_TIME=$1
END_TIME=$2
INTERVAL=10
while [ $START_TIME -le $END_TIME ]; 
do 
    STR=$(($START_TIME / $INTERVAL))
    echo $STR
    echo "$START_TIME;   `cat TaskServerSignals.log | grep  "$STR*" | wc -l`" >> server_signals_report.txt
    START_TIME=$(($START_TIME + $INTERVAL))
done
