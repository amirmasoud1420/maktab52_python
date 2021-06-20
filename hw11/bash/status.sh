#!/bin/bash
req = $(curl --write out"%{req}\n" "https://api.sunrise-sunset.org/json?lat=36.5452581&lng=52.6846571&date=today" --output result.txt --silent )
echo $req
