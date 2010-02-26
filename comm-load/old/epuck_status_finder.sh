#!/bin/bash
cat dbus-log.txt | grep TaskStatus | grep -w /robot$1 > Epuck$1-TaskStatus.log
