---
id: 3112
name: "J35P312/LoqusPokos"
branch: "master"
tag: "latest"
commit: "eaeb678cb08b993f4920422a8c8119fd7bfe1575"
version: "5196b2266285cafdec4ddb9b341d44a1"
build_date: "2019-10-14T11:02:00.144Z"
size_mb: 1120
size: 514809887
sif: "https://datasets.datalad.org/shub/J35P312/LoqusPokos/latest/2019-10-14-eaeb678c-5196b226/5196b2266285cafdec4ddb9b341d44a1.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/J35P312/LoqusPokos/latest/2019-10-14-eaeb678c-5196b226/
recipe: https://datasets.datalad.org/shub/J35P312/LoqusPokos/latest/2019-10-14-eaeb678c-5196b226/Singularity
collection: J35P312/LoqusPokos
---

# J35P312/LoqusPokos:latest

```bash
$ singularity pull shub://J35P312/LoqusPokos:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%environment
SHELL=/bin/bash
PATH=/opt/anaconda/bin:${PATH}
LC_ALL=C.UTF-8

%runscript
    echo "This is what happens when you run the container..."
    export PATH=/opt/anaconda/bin:${PATH}

%post
    echo "Hello from inside the container"
    apt-get update
    apt-get -y install wget git bzip2 build-essential gcc zlib1g-dev language-pack-en-base apt-transport-https
    update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8

    cd /root/ && wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
    cd /root/ && chmod 700 ./Miniconda3-latest-Linux-x86_64.sh
    cd /root/ && bash ./Miniconda3-latest-Linux-x86_64.sh -b -p /opt/anaconda/

    export PATH=/opt/anaconda/bin:${PATH}

    pip install https://github.com/moonso/loqusdb/archive/2.1.zip
    
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5
    echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.6 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.6.list

    apt-get update
    apt-get install -y mongodb-org

    mkdir -p /data/db
```

## Collection

 - Name: [J35P312/LoqusPokos](https://github.com/J35P312/LoqusPokos)
 - License: None

