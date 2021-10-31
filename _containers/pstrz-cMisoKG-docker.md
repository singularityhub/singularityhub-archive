---
id: 2568
name: "pstrz/cMisoKG"
branch: "master"
tag: "docker"
commit: "60da23428915a652bab651b51728160e42e33112"
version: "097807e1d8f610541035216fd487e196"
build_date: "2018-04-28T18:44:39.752Z"
size_mb: 1387
size: 572616735
sif: "https://datasets.datalad.org/shub/pstrz/cMisoKG/docker/2018-04-28-60da2342-097807e1/097807e1d8f610541035216fd487e196.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/pstrz/cMisoKG/docker/2018-04-28-60da2342-097807e1/
recipe: https://datasets.datalad.org/shub/pstrz/cMisoKG/docker/2018-04-28-60da2342-097807e1/Singularity
collection: pstrz/cMisoKG
---

# pstrz/cMisoKG:docker

```bash
$ singularity pull shub://pstrz/cMisoKG:docker
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu

%post
    apt-get -y install python3
    apt-get update
    apt-get update --fix-missing
    apt-get -y install python3-pip    
    apt-get -y install git-core
    git clone https://github.com/GPflow/GPflow.git
    cd GPflow
    export LC_all=C
    pip3 install .
    cd
    pip3 install -U pymc3
    pip3 install -U pytest
```

## Collection

 - Name: [pstrz/cMisoKG](https://github.com/pstrz/cMisoKG)
 - License: None

