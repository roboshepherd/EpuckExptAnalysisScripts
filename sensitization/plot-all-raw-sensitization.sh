for i in {1..16}
do
    ~/EpuckExptAnalysisScripts/sensitization/plot-raw-sensitization-of-single-robot.py ` echo Robot$i*.txt`
done