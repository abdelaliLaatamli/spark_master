# Setup Kafka on Docker
firstly we install docker and docker compose on our machine 
- [How To Install and Use Docker on Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04)
- [How To Install and Use Docker Compose on Ubuntu 22.04](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-22-04)

- Then put [Docker Compose File](./docker-composer.yml) in dir , change ``MACHINE_IP`` with your machine ip then start Docker Stack by 
```shell
docker-compose up -d
``` 
to start with scale 
```shell
docker-compose up -d --scale image=numberToScale
``` 

- to stop kafka 
```shell
docker-compose down
```


