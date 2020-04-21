#!/bin/bash

sed -e 's/\(.*\)/\L\1/' hh_sorted.csv | sed -e 's/ data scientist[^,]\+/\"/' > hh_positions.csv;


