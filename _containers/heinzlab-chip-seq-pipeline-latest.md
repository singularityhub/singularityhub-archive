---
id: 5385
name: "heinzlab/chip-seq-pipeline"
branch: "master"
tag: "latest"
commit: "b78007b86037cf43d69051f45836b02f1b8bff54"
version: "71902750b408b843f5c3f34e70bb52c9"
build_date: "2018-10-31T13:30:53.693Z"
size_mb: 3723
size: 1248268319
sif: "https://datasets.datalad.org/shub/heinzlab/chip-seq-pipeline/latest/2018-10-31-b78007b8-71902750/71902750b408b843f5c3f34e70bb52c9.simg"
url: https://datasets.datalad.org/shub/heinzlab/chip-seq-pipeline/latest/2018-10-31-b78007b8-71902750/
recipe: https://datasets.datalad.org/shub/heinzlab/chip-seq-pipeline/latest/2018-10-31-b78007b8-71902750/Singularity
collection: heinzlab/chip-seq-pipeline
---

# heinzlab/chip-seq-pipeline:latest

```bash
$ singularity pull shub://heinzlab/chip-seq-pipeline:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3

%labels
    MAINTAINER Carlos Guzman <cag104@eng.ucsd.edu>
    DESCRIPTION Container image containing all requirements for the adapted heinzlab/chip-seq-pipeline
    VERSION 0.1dev

%files
    environment.yml /

%environment
	PATH=/opt/conda/envs/chipseq-0.1dev/bin:$PATH
	export PATH

%post
    apt-get -y update
    apt-get -y install build-essential libboost-all-dev libgsl-dev libz-dev

    /opt/conda/bin/conda env create -f /environment.yml
    /opt/conda/bin/conda clean -a

    git clone https://github.com/rnakato/SSP.git
    cd SSP
    make
    mv bin/ssp /opt/conda/envs/chipseq-0.1dev/bin
```

## Collection

 - Name: [heinzlab/chip-seq-pipeline](https://github.com/heinzlab/chip-seq-pipeline)
 - License: None

