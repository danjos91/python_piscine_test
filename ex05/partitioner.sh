#!/bin/bash

cat hh_positions.csv | sort -t '-' -k2 | cut -d 't' -f 1 | sed 's/\"/ /g'| uniq -f 2 | cut -d " " -f 4 | tail -n 2 > dates.txt

MAX=`sed -n $= dates.txt`;
for i in 1 $MAX
do
	echo '“id”,“created_at”,“name”,“has_test”,“alternate_url”' > "`sed "${i}q;d" dates.txt`".csv;
	cat hh_positions.csv | grep `sed "${i}q;d" dates.txt` >> "`sed "${i}q;d" dates.txt`".csv;
done

