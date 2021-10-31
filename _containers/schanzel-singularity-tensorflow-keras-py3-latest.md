---
id: 2807
name: "schanzel/singularity-tensorflow-keras-py3"
branch: "master"
tag: "latest"
commit: "43d37502cdce0c059780a5814b133dd245f693e0"
version: "9ed67bc361df93cf109ad12980dbab2b"
build_date: "2021-04-13T22:46:21.455Z"
size_mb: 2423
size: 1184780319
sif: "https://datasets.datalad.org/shub/schanzel/singularity-tensorflow-keras-py3/latest/2021-04-13-43d37502-9ed67bc3/9ed67bc361df93cf109ad12980dbab2b.simg"
url: https://datasets.datalad.org/shub/schanzel/singularity-tensorflow-keras-py3/latest/2021-04-13-43d37502-9ed67bc3/
recipe: https://datasets.datalad.org/shub/schanzel/singularity-tensorflow-keras-py3/latest/2021-04-13-43d37502-9ed67bc3/Singularity
collection: schanzel/singularity-tensorflow-keras-py3
---

# schanzel/singularity-tensorflow-keras-py3:latest

```bash
$ singularity pull shub://schanzel/singularity-tensorflow-keras-py3:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: schanzel/tensorflow-keras-py3:latest

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

 - Name: [schanzel/singularity-tensorflow-keras-py3](https://github.com/schanzel/singularity-tensorflow-keras-py3)
 - License: [MIT License](https://api.github.com/licenses/mit)

