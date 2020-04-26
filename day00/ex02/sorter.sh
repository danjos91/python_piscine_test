#!/bin/bash

head -n1 hh.csv > hh_sorted.csv;
tail -n20 hh.csv | sort -k2 -k1 >> hh_sorted.csv;
