#! /bin/bash
docker rm $(docker stop $(docker ps -a -q --filter ancestor=ptsdocker16/interview-test-server --format="{{.ID}}"))
docker rm $(docker stop $(docker ps -a -q --filter ancestor=marginal-tax-api --format="{{.ID}}"))

docker run --init -p 5000:5000 ptsdocker16/interview-test-server > /dev/null 2>&1 & 

sleep 5

docker run --init -p 4000:4000 marginal-tax-api &
