#!/bin/bash

curl -H 'User-Agent: api-test-agent' 'https://api.hh.ru/vacancies?text=$1&area=1&items_on_page=20' -o hh.json
