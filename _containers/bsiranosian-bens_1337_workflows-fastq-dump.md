---
id: 9988
name: "bsiranosian/bens_1337_workflows"
branch: "master"
tag: "fastq-dump"
commit: "1448ba7acbf363ac644c6ea8b8718fb65f655d19"
version: "4f684dfb810886d4358775bfe0f8219e"
build_date: "2020-10-02T18:43:49.616Z"
size_mb: 884
size: 409825311
sif: "https://datasets.datalad.org/shub/bsiranosian/bens_1337_workflows/fastq-dump/2020-10-02-1448ba7a-4f684dfb/4f684dfb810886d4358775bfe0f8219e.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bsiranosian/bens_1337_workflows/fastq-dump/2020-10-02-1448ba7a-4f684dfb/
recipe: https://datasets.datalad.org/shub/bsiranosian/bens_1337_workflows/fastq-dump/2020-10-02-1448ba7a-4f684dfb/Singularity
collection: bsiranosian/bens_1337_workflows
---

# bsiranosian/bens_1337_workflows:fastq-dump

```bash
$ singularity pull shub://bsiranosian/bens_1337_workflows:fastq-dump
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04


# this command assumes at least singularity 2.3
%environment
    PATH="/usr/local/anaconda/bin:$PATH"

%post 
    apt-get update
    apt-get install -y wget build-essential

    # install anaconda
    if [ ! -d /usr/local/anaconda ]; then
         wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
            -O ~/anaconda.sh && \
         bash ~/anaconda.sh -b -p /usr/local/anaconda && \
         rm ~/anaconda.sh
    fi
        export PATH="/usr/local/anaconda/bin:$PATH"

    conda install -y -c bioconda parallel-fastq-dump

%runscript
   exec /bin/bash
```

## Collection

 - Name: [bsiranosian/bens_1337_workflows](https://github.com/bsiranosian/bens_1337_workflows)
 - License: None

