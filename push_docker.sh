#!/bin/sh 


GIT_COMMIT=$(git rev-parse HEAD)

docker build \
       -t "caheredia/caiso-connector:${GIT_COMMIT}" \
       -f Dockerfile .
       
