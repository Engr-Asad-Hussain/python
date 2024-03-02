docker-compose -f "docker-compose.yaml" down
docker rmi redis:7.0
docker rmi flask:sde
docker rmi mysql:sde