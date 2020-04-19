#!/bin/bash

curl -H 'User-Agent: api-test-agent' 'https://api.hh.ru/vacancies?text=data+scientist&area=1&items_on_page=20' -o hh.json
