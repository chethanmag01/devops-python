docker images | sed 1d > dockerimages.txt
docker ps | sed 1d | tr '"' ' '> dockerrunningcontainers.txt
docker ps -a | sed 1d | tr '"' ' ' > dockerallcontainers.txt
