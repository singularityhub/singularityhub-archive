---
id: 9989
name: "bsiranosian/bens_1337_workflows"
branch: "master"
tag: "fastq-pair"
commit: "72f0065cbdd92ce62d622189a3b265d21b2729a8"
version: "9b97f71d9d2a20019419793e778aa4d8"
build_date: "2020-01-13T04:02:09.623Z"
size_mb: 317
size: 124964895
sif: "https://datasets.datalad.org/shub/bsiranosian/bens_1337_workflows/fastq-pair/2020-01-13-72f0065c-9b97f71d/9b97f71d9d2a20019419793e778aa4d8.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bsiranosian/bens_1337_workflows/fastq-pair/2020-01-13-72f0065c-9b97f71d/
recipe: https://datasets.datalad.org/shub/bsiranosian/bens_1337_workflows/fastq-pair/2020-01-13-72f0065c-9b97f71d/Singularity
collection: bsiranosian/bens_1337_workflows
---

# bsiranosian/bens_1337_workflows:fastq-pair

```bash
$ singularity pull shub://bsiranosian/bens_1337_workflows:fastq-pair
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04


# this command assumes at least singularity 2.3
%environment
    PATH="/fastq-pair-master/:$PATH"

%post 
    apt-get update
    apt-get install -y wget build-essential unzip

    # get from github
    wget https://github.com/linsalrob/fastq-pair/archive/master.zip
    unzip master.zip
    cd fastq-pair-master
    gcc *.c -o fastq_pair    
    export PATH="/fastq-pair-master/:$PATH"

    # can test with this line
    # fastq_pair -t 1000 /fastq-pair-master/test/left.fastq /fastq-pair-master/test/right.fastq

%runscript
   exec /bin/bash
```

## Collection

 - Name: [bsiranosian/bens_1337_workflows](https://github.com/bsiranosian/bens_1337_workflows)
 - License: None

