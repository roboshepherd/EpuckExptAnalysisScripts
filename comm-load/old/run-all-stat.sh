#!/bin/sh
~/scripts/comm-load/stat-any-signal.py Local 44 *SumOver50sec-local_signals_report.txt
~/scripts/comm-load/stat-any-signal.py Server 44 *SumOver50sec-server_signals_report.txt
~/scripts/comm-load/plot_both_signals_stat.py ServerCommLoadStat.txt LocalCommLoadStat.txt