---
id: 3645
name: "myNameIsPatrick/idq-services"
branch: "master"
tag: "kafka-cp"
commit: "286fb8b1dc06e0516b1cb074e037f95b2f81a16a"
version: "7d8e63f26cdf970ca2b6ebb99a5df978"
build_date: "2018-07-24T19:19:06.059Z"
size_mb: 456
size: 211292191
sif: "https://datasets.datalad.org/shub/myNameIsPatrick/idq-services/kafka-cp/2018-07-24-286fb8b1-7d8e63f2/7d8e63f26cdf970ca2b6ebb99a5df978.simg"
url: https://datasets.datalad.org/shub/myNameIsPatrick/idq-services/kafka-cp/2018-07-24-286fb8b1-7d8e63f2/
recipe: https://datasets.datalad.org/shub/myNameIsPatrick/idq-services/kafka-cp/2018-07-24-286fb8b1-7d8e63f2/Singularity
collection: myNameIsPatrick/idq-services
---

# myNameIsPatrick/idq-services:kafka-cp

```bash
$ singularity pull shub://myNameIsPatrick/idq-services:kafka-cp
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: confluentinc/cp-kafka:3.2.4

% environment
    KAFKA_ZOOKEEPER_CONNECT=localhost:2181
    KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://localhost:9092
    KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR=1
    export KAFKA_ADVERTISED_LISTENERS KAFKA_ZOOKEEPER_CONNECT KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR
```

## Collection

 - Name: [myNameIsPatrick/idq-services](https://github.com/myNameIsPatrick/idq-services)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

