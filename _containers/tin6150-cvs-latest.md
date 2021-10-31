---
id: 9993
name: "tin6150/cvs"
branch: "master"
tag: "latest"
commit: "f311fe14f7ca68d1663ce23dec0687e8f8b8363f"
version: "664ac367a8bc3da3d61c529f428af2cb"
build_date: "2019-08-14T22:46:53.630Z"
size_mb: 7
size: 3428383
sif: "https://datasets.datalad.org/shub/tin6150/cvs/latest/2019-08-14-f311fe14-664ac367/664ac367a8bc3da3d61c529f428af2cb.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/tin6150/cvs/latest/2019-08-14-f311fe14-664ac367/
recipe: https://datasets.datalad.org/shub/tin6150/cvs/latest/2019-08-14-f311fe14-664ac367/Singularity
collection: tin6150/cvs
---

# tin6150/cvs:latest

```bash
$ singularity pull shub://tin6150/cvs:latest
```

## Singularity Recipe

```singularity
# Singularity container definition cvs (concurrent version control, client)
# https://github.com/tin6150/cvs/Singularity
# https://www.singularity-hub.org/collections/3206

# usage:
# singularity pull shub://tin6150/cvs
# ln -s tin6150-cvs-master-latest.simg cvs
# export PATH=$PATH:/global/scratch/tin/singularity-repo
# cvs help

# expect to be using Singularity 2.6
# singularity-hub seems to be using Singularity 2.5
BootStrap: docker
From: alpine:3.6

%runscript
#--echo "running cvs client from the container:"
cvs "$@"

%post
echo "installing cvs using apk inside the container"
apk update
apk upgrade
apk add cvs

touch /singularity-`date +%Y%m%d-%H%M`

# used https://singularity-hub.org/containers/405 as example/reference


# n0062.lr6 has singularity 2.6-dist
# lrc-viz   has singularity 2.4-dist :(
# lrc-login, n0000.scs00 ... ??
```

## Collection

 - Name: [tin6150/cvs](https://github.com/tin6150/cvs)
 - License: None

