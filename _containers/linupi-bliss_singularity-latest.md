---
id: 13338
name: "linupi/bliss_singularity"
branch: "master"
tag: "latest"
commit: "37a0f64fcb4803a4c6b5ac5179f8fe8821a15602"
version: "41af0872175c38b443dbefcfceddc34a"
build_date: "2020-06-15T08:28:04.439Z"
size_mb: 626.0
size: 267014175
sif: "https://datasets.datalad.org/shub/linupi/bliss_singularity/latest/2020-06-15-37a0f64f-41af0872/41af0872175c38b443dbefcfceddc34a.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/linupi/bliss_singularity/latest/2020-06-15-37a0f64f-41af0872/
recipe: https://datasets.datalad.org/shub/linupi/bliss_singularity/latest/2020-06-15-37a0f64f-41af0872/Singularity
collection: linupi/bliss_singularity
---

# linupi/bliss_singularity:latest

```bash
$ singularity pull shub://linupi/bliss_singularity:latest
```

## Singularity Recipe

```singularity
#!/bin/bash
# 
# Linus Pithan <linus.pithan@esrf.fr>
# 2017/10/26: initial version
# based on truatpasteurdotfr/singularity-docker-miniconda3

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
#conda list > /conda.txt
touch /`date -u -Iseconds`

%labels
MAINTAINER linupi
```

## Collection

 - Name: [linupi/bliss_singularity](https://github.com/linupi/bliss_singularity)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

