---
id: 3642
name: "myNameIsPatrick/idq-services"
branch: "master"
tag: "kafka"
commit: "5de2a7b60fd93d45797ed6535316982f321588c0"
version: "7fdcd726a8b580dd7a2a8069da824e54"
build_date: "2018-07-24T19:19:06.065Z"
size_mb: 282
size: 144834591
sif: "https://datasets.datalad.org/shub/myNameIsPatrick/idq-services/kafka/2018-07-24-5de2a7b6-7fdcd726/7fdcd726a8b580dd7a2a8069da824e54.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/myNameIsPatrick/idq-services/kafka/2018-07-24-5de2a7b6-7fdcd726/
recipe: https://datasets.datalad.org/shub/myNameIsPatrick/idq-services/kafka/2018-07-24-5de2a7b6-7fdcd726/Singularity
collection: myNameIsPatrick/idq-services
---

# myNameIsPatrick/idq-services:kafka

```bash
$ singularity pull shub://myNameIsPatrick/idq-services:kafka
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: wurstmeister/kafka:2.11-0.11.0.2

% environment
    KAFKA_ADVERTISED_HOST_NAME=${HOSTNAME}
    KAFKA_ZOOKEEPER_CONNECT=${HOSTNAME}:2181
    KAFKA_ADVERTISED_PORT=9092
    export KAFKA_ADVERTISED_HOST_NAME KAFKA_ZOOKEEPER_CONNECT KAFKA_ADVERTISED_PORT
```

## Collection

 - Name: [myNameIsPatrick/idq-services](https://github.com/myNameIsPatrick/idq-services)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

