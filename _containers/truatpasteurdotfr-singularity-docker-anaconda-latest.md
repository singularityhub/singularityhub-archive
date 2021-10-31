---
id: 577
name: "truatpasteurdotfr/singularity-docker-anaconda"
branch: "master"
tag: "latest"
commit: "681807a327c41b9e86887dec7bed2ff6cd15094e"
version: "a932fec35f10da4ce5c9d7e3674ca448"
build_date: "2020-04-16T14:16:34.227Z"
size_mb: 3369
size: 1440722975
sif: "https://datasets.datalad.org/shub/truatpasteurdotfr/singularity-docker-anaconda/latest/2020-04-16-681807a3-a932fec3/a932fec35f10da4ce5c9d7e3674ca448.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/truatpasteurdotfr/singularity-docker-anaconda/latest/2020-04-16-681807a3-a932fec3/
recipe: https://datasets.datalad.org/shub/truatpasteurdotfr/singularity-docker-anaconda/latest/2020-04-16-681807a3-a932fec3/Singularity
collection: truatpasteurdotfr/singularity-docker-anaconda
---

# truatpasteurdotfr/singularity-docker-anaconda:latest

```bash
$ singularity pull shub://truatpasteurdotfr/singularity-docker-anaconda:latest
```

## Singularity Recipe

```singularity
#!/bin/bash
# 
# Tru Huynh <tru@pasteur.fr>
# 2017/10/26: initial version
# use as baseline to build a container from anaconda

BootStrap: docker
From: continuumio/anaconda

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

 - Name: [truatpasteurdotfr/singularity-docker-anaconda](https://github.com/truatpasteurdotfr/singularity-docker-anaconda)
 - License: None

