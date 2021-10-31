---
id: 9370
name: "jemunro/nf-fastq-dump"
branch: "master"
tag: "latest"
commit: "a5344b1ef5a24f2eebfc0c32448ae6c34a5392c2"
version: "7bae2edf566f3469d76c912b607f85cf"
build_date: "2019-05-28T04:27:36.300Z"
size_mb: 837
size: 325824543
sif: "https://datasets.datalad.org/shub/jemunro/nf-fastq-dump/latest/2019-05-28-a5344b1e-7bae2edf/7bae2edf566f3469d76c912b607f85cf.simg"
url: https://datasets.datalad.org/shub/jemunro/nf-fastq-dump/latest/2019-05-28-a5344b1e-7bae2edf/
recipe: https://datasets.datalad.org/shub/jemunro/nf-fastq-dump/latest/2019-05-28-a5344b1e-7bae2edf/Singularity
collection: jemunro/nf-fastq-dump
---

# jemunro/nf-fastq-dump:latest

```bash
$ singularity pull shub://jemunro/nf-fastq-dump:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3:latest

%labels
    MAINTAINER Jacob Munro
    AUTHOR Bahlo Lab
    DESCRIPTION container image with requirements for NGS sequence simulation using ART
    VERSION 0.0.1

%files
    environment.yml /

%post
    apt-get update && apt-get install -y procps
    /opt/conda/bin/conda env create -f /environment.yml
    /opt/conda/bin/conda clean --all -y

%environment
    export PATH="/opt/conda/envs/fastq-dumper/bin:/opt/conda/bin:$PATH"
```

## Collection

 - Name: [jemunro/nf-fastq-dump](https://github.com/jemunro/nf-fastq-dump)
 - License: None

