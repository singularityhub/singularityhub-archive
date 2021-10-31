---
id: 8605
name: "mru4913/singularity-docker-anaconda3"
branch: "master"
tag: "latest"
commit: "ce4e9a2c3a2662e8a5aff979c827d48577c08dc9"
version: "01ccd4a20025129c058610ce750e8f4d"
build_date: "2019-10-29T09:50:51.223Z"
size_mb: 5970
size: 3313070111
sif: "https://datasets.datalad.org/shub/mru4913/singularity-docker-anaconda3/latest/2019-10-29-ce4e9a2c-01ccd4a2/01ccd4a20025129c058610ce750e8f4d.simg"
url: https://datasets.datalad.org/shub/mru4913/singularity-docker-anaconda3/latest/2019-10-29-ce4e9a2c-01ccd4a2/
recipe: https://datasets.datalad.org/shub/mru4913/singularity-docker-anaconda3/latest/2019-10-29-ce4e9a2c-01ccd4a2/Singularity
collection: mru4913/singularity-docker-anaconda3
---

# mru4913/singularity-docker-anaconda3:latest

```bash
$ singularity pull shub://mru4913/singularity-docker-anaconda3:latest
```

## Singularity Recipe

```singularity
#!/bin/bash
# 
# Tru Huynh <tru@pasteur.fr>
# 2017/10/26: initial version
# use as baseline to build a container from anaconda3

BootStrap: docker
From: continuumio/anaconda3

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
conda install pytorch torchvision -c pytorch
conda install scikit-learn

%labels
MAINTAINER truatpasteurdotfr
```

## Collection

 - Name: [mru4913/singularity-docker-anaconda3](https://github.com/mru4913/singularity-docker-anaconda3)
 - License: [Other](None)

