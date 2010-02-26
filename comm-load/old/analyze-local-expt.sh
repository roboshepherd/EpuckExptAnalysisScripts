#!/bin/bash
PREFIX=$1
START=$2
END=$3
MAX_LINE=215
~/scripts/comm-load/report_taskserver_signals.sh $START $END
~/scripts/comm-load/report_local_taskinfo_signals.sh $START $END
~/scripts/comm-load/sum_any_signals.py $MAX_LINE server_signals_report.txt $PREFIX
~/scripts/comm-load/sum_any_signals.py $MAX_LINE local_signals_report.txt $PREFIX