#!/bin/bash

echo "name","count" > hh_uniq_positions.csv;
sed -e s/','/" "/g  hh_positions.csv | sed -e 's/\"[^ ]\+//' | sed -e 's/\"[^ ]\+//' | 
	sed -e 's/ [^ ]\+$//' | uniq -f 4 -c | sed -e 's/ [^ ]\+$//'| sed 's/^\s*//' >> hh_uniq_positions.csv;

