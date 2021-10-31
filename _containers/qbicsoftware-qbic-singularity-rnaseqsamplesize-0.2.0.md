---
id: 5573
name: "qbicsoftware/qbic-singularity-rnaseqsamplesize"
branch: "development"
tag: "0.2.0"
commit: "ac9c36d80522a6995e9113065cb9480c9799f06d"
version: "9f8ea7b3b55addb0996f7e6c5c96a59a"
build_date: "2018-11-12T19:45:45.239Z"
size_mb: 1691
size: 568586271
sif: "https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-rnaseqsamplesize/0.2.0/2018-11-12-ac9c36d8-9f8ea7b3/9f8ea7b3b55addb0996f7e6c5c96a59a.simg"
url: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-rnaseqsamplesize/0.2.0/2018-11-12-ac9c36d8-9f8ea7b3/
recipe: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-rnaseqsamplesize/0.2.0/2018-11-12-ac9c36d8-9f8ea7b3/Singularity
collection: qbicsoftware/qbic-singularity-rnaseqsamplesize
---

# qbicsoftware/qbic-singularity-rnaseqsamplesize:0.2.0

```bash
$ singularity pull shub://qbicsoftware/qbic-singularity-rnaseqsamplesize:0.2.0
```

## Singularity Recipe

```singularity
From:nfcore/base
Bootstrap:docker

%labels
    MAINTAINER Sven Fillinger <sven.fillinger@qbic.uni-tuebingen.de>
    DESCRIPTION Singularity image containing all requirements for the rnaseq samplesize app
    VERSION 1.0

%environment
    PATH=/opt/conda/envs/rnaseqsamplesize-1.0/bin:$PATH
    export PATH

%files
    environment.yml /
    script.py
    sample_size_matrix.R /
    power_matrix.R /

%post
    /opt/conda/bin/conda env create -f /environment.yml
    /opt/conda/bin/conda clean -a

%runscript
    exec python /script.py "$@"
```

## Collection

 - Name: [qbicsoftware/qbic-singularity-rnaseqsamplesize](https://github.com/qbicsoftware/qbic-singularity-rnaseqsamplesize)
 - License: [MIT License](https://api.github.com/licenses/mit)

