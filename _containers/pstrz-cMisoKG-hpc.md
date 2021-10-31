---
id: 2548
name: "pstrz/cMisoKG"
branch: "master"
tag: "hpc"
commit: "bcd66ef17b9db872edfeae87abc27e174203ebdb"
version: "86281ae4f5ee0920333854b2f0a8eb22"
build_date: "2018-05-02T08:28:06.201Z"
size_mb: 1393
size: 542277663
sif: "https://datasets.datalad.org/shub/pstrz/cMisoKG/hpc/2018-05-02-bcd66ef1-86281ae4/86281ae4f5ee0920333854b2f0a8eb22.simg"
url: https://datasets.datalad.org/shub/pstrz/cMisoKG/hpc/2018-05-02-bcd66ef1-86281ae4/
recipe: https://datasets.datalad.org/shub/pstrz/cMisoKG/hpc/2018-05-02-bcd66ef1-86281ae4/Singularity
collection: pstrz/cMisoKG
---

# pstrz/cMisoKG:hpc

```bash
$ singularity pull shub://pstrz/cMisoKG:hpc
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

