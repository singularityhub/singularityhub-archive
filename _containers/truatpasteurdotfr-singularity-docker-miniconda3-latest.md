---
id: 576
name: "truatpasteurdotfr/singularity-docker-miniconda3"
branch: "master"
tag: "latest"
commit: "bc99fa8141d45c6f9915c33261c4c1b2e216e773"
version: "de0684080854656b79608bb675f3a5b0"
build_date: "2020-12-19T09:38:52.519Z"
size_mb: 877
size: 344088607
sif: "https://datasets.datalad.org/shub/truatpasteurdotfr/singularity-docker-miniconda3/latest/2020-12-19-bc99fa81-de068408/de0684080854656b79608bb675f3a5b0.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/truatpasteurdotfr/singularity-docker-miniconda3/latest/2020-12-19-bc99fa81-de068408/
recipe: https://datasets.datalad.org/shub/truatpasteurdotfr/singularity-docker-miniconda3/latest/2020-12-19-bc99fa81-de068408/Singularity
collection: truatpasteurdotfr/singularity-docker-miniconda3
---

# truatpasteurdotfr/singularity-docker-miniconda3:latest

```bash
$ singularity pull shub://truatpasteurdotfr/singularity-docker-miniconda3:latest
```

## Singularity Recipe

```singularity
#!/bin/bash
# 
# Tru Huynh <tru@pasteur.fr>
# 2017/10/26: initial version
# use as baseline to build a container from miniconda3

BootStrap: docker
From: continuumio/miniconda3

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

 - Name: [truatpasteurdotfr/singularity-docker-miniconda3](https://github.com/truatpasteurdotfr/singularity-docker-miniconda3)
 - License: None

