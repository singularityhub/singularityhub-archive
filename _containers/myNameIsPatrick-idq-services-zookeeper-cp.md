---
id: 3646
name: "myNameIsPatrick/idq-services"
branch: "master"
tag: "zookeeper-cp"
commit: "06e00e7846dd4e5cd12426f02f94a16805e709e0"
version: "fc720ef10d31ba6c83e10a02d44dc9c4"
build_date: "2018-07-24T21:22:23.431Z"
size_mb: 550
size: 258977823
sif: "https://datasets.datalad.org/shub/myNameIsPatrick/idq-services/zookeeper-cp/2018-07-24-06e00e78-fc720ef1/fc720ef10d31ba6c83e10a02d44dc9c4.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/myNameIsPatrick/idq-services/zookeeper-cp/2018-07-24-06e00e78-fc720ef1/
recipe: https://datasets.datalad.org/shub/myNameIsPatrick/idq-services/zookeeper-cp/2018-07-24-06e00e78-fc720ef1/Singularity
collection: myNameIsPatrick/idq-services
---

# myNameIsPatrick/idq-services:zookeeper-cp

```bash
$ singularity pull shub://myNameIsPatrick/idq-services:zookeeper-cp
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: confluentinc/cp-zookeeper:4.0.2
Includecmd: no

% environment
    export SINGULARITY_BINDPATH="/usr/lib/jvm/jre"
    export ZOOKEEPER_DATA_DIR=/tmp/zookeeper
    export ZOOKEEPER_CLIENT_PORT=2271
    export ZOOKEEPER_MAX_CLIENT_CNXNS=0

% startscript
    /etc/confluent/docker/run
```

## Collection

 - Name: [myNameIsPatrick/idq-services](https://github.com/myNameIsPatrick/idq-services)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

