---
id: 15811
name: "saviodot/singularity_MACS2"
branch: "main"
tag: "latest"
commit: "829e4bfcfc5b65062c06c8e76919782d06a30312"
version: "0522b36ddbe9fee52b7203aed5054944"
build_date: "2021-03-25T17:05:09.152Z"
size_mb: 994.0
size: 348110879
sif: "https://datasets.datalad.org/shub/saviodot/singularity_MACS2/latest/2021-03-25-829e4bfc-0522b36d/0522b36ddbe9fee52b7203aed5054944.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/saviodot/singularity_MACS2/latest/2021-03-25-829e4bfc-0522b36d/
recipe: https://datasets.datalad.org/shub/saviodot/singularity_MACS2/latest/2021-03-25-829e4bfc-0522b36d/Singularity
collection: saviodot/singularity_MACS2
---

# saviodot/singularity_MACS2:latest

```bash
$ singularity pull shub://saviodot/singularity_MACS2:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: python:3.8

%labels
  Maintainer Savio Chow
  Python_version 3.8
  MACS2_version 2.2.7.1

%help
  This image will run MACS2, downloaded from pip and uses python3.8

%apprun python
  exec python "${@}"

%apprun macs2
  exec macs2 "${@}"

%runscript
  exec macs2 "${@}"

%environment
  export PATH=/usr/lib/python3.8/bin:${PATH}
  export SHELL=/bin/bash
  export LC_ALL=en_US.UTF-8
  export LANG=en_US.UTF-8
  export LANGUAGE=en_US.UTF-8
  
%post
  pip install --no-cache-dir MACS2
```

## Collection

 - Name: [saviodot/singularity_MACS2](https://github.com/saviodot/singularity_MACS2)
 - License: None

