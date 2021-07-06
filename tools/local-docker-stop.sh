#! /bin/bash
docker rm $(docker stop $(docker ps -a -q --filter ancestor=ptsdocker16/interview-test-server --format="{{.ID}}"))
docker rm $(docker stop $(docker ps -a -q --filter ancestor=marginal-tax-api --format="{{.ID}}"))