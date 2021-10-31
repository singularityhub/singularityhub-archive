---
id: 579
name: "truatpasteurdotfr/singularity-docker-anaconda3"
branch: "master"
tag: "latest"
commit: "0a21fedc28364e9ce96aa8e7b0f39c1af7485466"
version: "d2bc71e81b4643a204a90ac2efe58c74"
build_date: "2020-06-09T22:42:34.514Z"
size_mb: 3455
size: 1528438815
sif: "https://datasets.datalad.org/shub/truatpasteurdotfr/singularity-docker-anaconda3/latest/2020-06-09-0a21fedc-d2bc71e8/d2bc71e81b4643a204a90ac2efe58c74.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/truatpasteurdotfr/singularity-docker-anaconda3/latest/2020-06-09-0a21fedc-d2bc71e8/
recipe: https://datasets.datalad.org/shub/truatpasteurdotfr/singularity-docker-anaconda3/latest/2020-06-09-0a21fedc-d2bc71e8/Singularity
collection: truatpasteurdotfr/singularity-docker-anaconda3
---

# truatpasteurdotfr/singularity-docker-anaconda3:latest

```bash
$ singularity pull shub://truatpasteurdotfr/singularity-docker-anaconda3:latest
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

%labels
MAINTAINER truatpasteurdotfr
```

## Collection

 - Name: [truatpasteurdotfr/singularity-docker-anaconda3](https://github.com/truatpasteurdotfr/singularity-docker-anaconda3)
 - License: None

