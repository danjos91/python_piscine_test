#!/bin/bash

echo "“id”,“created_at”,“name”,“has_test”,“alternate_url”" > hh.csv;
cat hh.json | jq -r -f filter.jq >> hh.csv

