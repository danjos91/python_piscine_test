#!/bin/bash

curl -H 'User-Agent: api-test-agent' "https://api.hh.ru/vacancies?area=113&text=$1+$2+$3+$4&items_on_page=20" > hh.json;
