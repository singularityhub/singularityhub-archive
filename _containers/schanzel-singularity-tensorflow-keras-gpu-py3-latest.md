---
id: 2782
name: "schanzel/singularity-tensorflow-keras-gpu-py3"
branch: "master"
tag: "latest"
commit: "06179c8406f795eb91dfb9b95e0f80cd01d39365"
version: "98bcd57a3116968cf1b4f822c6272a36"
build_date: "2021-03-13T20:20:55.106Z"
size_mb: 3011
size: 1359175711
sif: "https://datasets.datalad.org/shub/schanzel/singularity-tensorflow-keras-gpu-py3/latest/2021-03-13-06179c84-98bcd57a/98bcd57a3116968cf1b4f822c6272a36.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/schanzel/singularity-tensorflow-keras-gpu-py3/latest/2021-03-13-06179c84-98bcd57a/
recipe: https://datasets.datalad.org/shub/schanzel/singularity-tensorflow-keras-gpu-py3/latest/2021-03-13-06179c84-98bcd57a/Singularity
collection: schanzel/singularity-tensorflow-keras-gpu-py3
---

# schanzel/singularity-tensorflow-keras-gpu-py3:latest

```bash
$ singularity pull shub://schanzel/singularity-tensorflow-keras-gpu-py3:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: schanzel/tensorflow-keras-gpu-py3:latest

%environment
  SHELL=/bin/bash
  export SHELL

%setup

%post
  . /environment
  echo 'SHELL=/bin/bash' >> /environment
  chmod +x /environment
  mkdir /scratch /data 

%runscript

%test
```

## Collection

 - Name: [schanzel/singularity-tensorflow-keras-gpu-py3](https://github.com/schanzel/singularity-tensorflow-keras-gpu-py3)
 - License: [MIT License](https://api.github.com/licenses/mit)

