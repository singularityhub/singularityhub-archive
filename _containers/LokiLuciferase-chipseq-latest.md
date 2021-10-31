---
id: 5690
name: "LokiLuciferase/chipseq"
branch: "master"
tag: "latest"
commit: "6c79f51adffc1a99cbb637c17221870008e8ceac"
version: "c8cd6fed3d8472b366e366923bded925"
build_date: "2018-11-24T04:49:43.596Z"
size_mb: 5845
size: 2734440479
sif: "https://datasets.datalad.org/shub/LokiLuciferase/chipseq/latest/2018-11-24-6c79f51a-c8cd6fed/c8cd6fed3d8472b366e366923bded925.simg"
url: https://datasets.datalad.org/shub/LokiLuciferase/chipseq/latest/2018-11-24-6c79f51a-c8cd6fed/
recipe: https://datasets.datalad.org/shub/LokiLuciferase/chipseq/latest/2018-11-24-6c79f51a-c8cd6fed/Singularity
collection: LokiLuciferase/chipseq
---

# LokiLuciferase/chipseq:latest

```bash
$ singularity pull shub://LokiLuciferase/chipseq:latest
```

## Singularity Recipe

```singularity
From:nfcore/base
Bootstrap:docker

%labels
    MAINTAINER Alexander Peltzer <alexander.peltzer@qbic.uni-tuebingen.de>
    DESCRIPTION Container image containing all requirements for the nf-core/chipseq pipeline
    VERSION 1.0dev

%environment
    PATH=/opt/conda/envs/nfcore-chipseq-1.4dev/bin:$PATH
    export PATH

%files
    environment.yml /

%post
    /opt/conda/bin/conda env create -f /environment.yml
    /opt/conda/bin/conda clean -a
```

## Collection

 - Name: [LokiLuciferase/chipseq](https://github.com/LokiLuciferase/chipseq)
 - License: [MIT License](https://api.github.com/licenses/mit)

