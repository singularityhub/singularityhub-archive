---
id: 8758
name: "CreRecombinase/ptb_container"
branch: "master"
tag: "latest"
commit: "8e729869d6c11ebb0b57930d2c879764d82d54e3"
version: "9d5af63e3ae5d23d36cb359a6a826f9d"
build_date: "2019-08-26T20:11:46.684Z"
size_mb: 7589.0
size: 4456415263
sif: "https://datasets.datalad.org/shub/CreRecombinase/ptb_container/latest/2019-08-26-8e729869-9d5af63e/9d5af63e3ae5d23d36cb359a6a826f9d.sif"
url: https://datasets.datalad.org/shub/CreRecombinase/ptb_container/latest/2019-08-26-8e729869-9d5af63e/
recipe: https://datasets.datalad.org/shub/CreRecombinase/ptb_container/latest/2019-08-26-8e729869-9d5af63e/Singularity
collection: CreRecombinase/ptb_container
---

# CreRecombinase/ptb_container:latest

```bash
$ singularity pull shub://CreRecombinase/ptb_container:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: pytorch/pytorch:1.0.1-cuda10.0-cudnn7-runtime


%post
    . /opt/conda/etc/profile.d/conda.sh
    conda activate
    /opt/conda/bin/conda install -c bioconda selene-sdk
```

## Collection

 - Name: [CreRecombinase/ptb_container](https://github.com/CreRecombinase/ptb_container)
 - License: None

