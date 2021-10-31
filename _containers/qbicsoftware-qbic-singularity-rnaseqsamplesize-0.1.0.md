---
id: 5558
name: "qbicsoftware/qbic-singularity-rnaseqsamplesize"
branch: "development"
tag: "0.1.0"
commit: "c3672397adf1f82e5670c7b89b43fadbad82412b"
version: "42dde4a4d8b2428732c571d09509c5d8"
build_date: "2018-11-11T00:03:06.751Z"
size_mb: 1584
size: 521830431
sif: "https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-rnaseqsamplesize/0.1.0/2018-11-11-c3672397-42dde4a4/42dde4a4d8b2428732c571d09509c5d8.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/qbicsoftware/qbic-singularity-rnaseqsamplesize/0.1.0/2018-11-11-c3672397-42dde4a4/
recipe: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-rnaseqsamplesize/0.1.0/2018-11-11-c3672397-42dde4a4/Singularity
collection: qbicsoftware/qbic-singularity-rnaseqsamplesize
---

# qbicsoftware/qbic-singularity-rnaseqsamplesize:0.1.0

```bash
$ singularity pull shub://qbicsoftware/qbic-singularity-rnaseqsamplesize:0.1.0
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

