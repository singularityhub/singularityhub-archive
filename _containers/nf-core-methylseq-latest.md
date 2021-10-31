---
id: 3909
name: "nf-core/methylseq"
branch: "master"
tag: "latest"
commit: "1d3f5cc5898c973832722a7e76538eab0933b3f5"
version: "033e5ab2c4b5b367db2577f023eb5315"
build_date: "2019-02-01T14:00:52.409Z"
size_mb: 3002
size: 1039638559
sif: "https://datasets.datalad.org/shub/nf-core/methylseq/latest/2019-02-01-1d3f5cc5-033e5ab2/033e5ab2c4b5b367db2577f023eb5315.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/nf-core/methylseq/latest/2019-02-01-1d3f5cc5-033e5ab2/
recipe: https://datasets.datalad.org/shub/nf-core/methylseq/latest/2019-02-01-1d3f5cc5-033e5ab2/Singularity
collection: nf-core/methylseq
---

# nf-core/methylseq:latest

```bash
$ singularity pull shub://nf-core/methylseq:latest
```

## Singularity Recipe

```singularity
From:nfcore/base
Bootstrap:docker

%labels
    MAINTAINER Phil Ewels <phil.ewels@scilifelab.se>
    DESCRIPTION Container image containing all requirements for the nf-core/methylseq pipeline
    VERSION 1.3

%environment
    PATH=/opt/conda/envs/nf-core-methylseq-1.3/bin:$PATH
    export PATH

%files
    environment.yml /

%post
    /opt/conda/bin/conda env create -f /environment.yml
    /opt/conda/bin/conda clean -a
```

## Collection

 - Name: [nf-core/methylseq](https://github.com/nf-core/methylseq)
 - License: [MIT License](https://api.github.com/licenses/mit)

