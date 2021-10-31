---
id: 575
name: "truatpasteurdotfr/singularity-docker-miniconda"
branch: "master"
tag: "latest"
commit: "9d77da105fd799aaa0781a9dd4c03f78f61403ef"
version: "c0654c97effc57b6f99409d2b10ff67a"
build_date: "2020-11-02T09:22:37.026Z"
size_mb: 780
size: 258142239
sif: "https://datasets.datalad.org/shub/truatpasteurdotfr/singularity-docker-miniconda/latest/2020-11-02-9d77da10-c0654c97/c0654c97effc57b6f99409d2b10ff67a.simg"
url: https://datasets.datalad.org/shub/truatpasteurdotfr/singularity-docker-miniconda/latest/2020-11-02-9d77da10-c0654c97/
recipe: https://datasets.datalad.org/shub/truatpasteurdotfr/singularity-docker-miniconda/latest/2020-11-02-9d77da10-c0654c97/Singularity
collection: truatpasteurdotfr/singularity-docker-miniconda
---

# truatpasteurdotfr/singularity-docker-miniconda:latest

```bash
$ singularity pull shub://truatpasteurdotfr/singularity-docker-miniconda:latest
```

## Singularity Recipe

```singularity
#!/bin/bash
# 
# Tru Huynh <tru@pasteur.fr>
# 2017/10/26: initial version
# use as baseline to build a container from miniconda

BootStrap: docker
From: continuumio/miniconda

%runscript
echo "This is what happens when you run the container..."
export PATH=/opt/conda/bin:${PATH}
/bin/bash

%post
export PATH=/opt/conda/bin:${PATH}
echo "Hello from inside the container"
conda update -y conda
conda update --all
conda list > /conda.txt
touch /`date -u -Iseconds`

%labels
MAINTAINER truatpasteurdotfr
```

## Collection

 - Name: [truatpasteurdotfr/singularity-docker-miniconda](https://github.com/truatpasteurdotfr/singularity-docker-miniconda)
 - License: None

