#! /bin/bash

docker run --init -p 5000:5000 ptsdocker16/interview-test-server > /dev/null 2>&1 & 

sleep 5

python -m unittest discover -s ./tests -v > test.output

docker rm $(docker stop $(docker ps -a -q --filter ancestor=ptsdocker16/interview-test-server --format="{{.ID}}")) 