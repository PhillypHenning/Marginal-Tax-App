#! /bin/bash

# Get the interview test server and start container using inner port 5000, outer port 5000. Put to background.
docker run --init -p 5000:5000 ptsdocker16/interview-test-server > /dev/null 2>&1 & 

sleep 5

# Start Server
python main.py

#tail -f ./data/logs/app.log

# Find images using the same image name as above, remove them all. 
docker rm $(docker stop $(docker ps -a -q --filter ancestor=ptsdocker16/interview-test-server --format="{{.ID}}"))