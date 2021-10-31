---
id: 3915
name: "mwiens91/test-error-containers"
branch: "master"
tag: "latest"
commit: "36e4fc34cdd8d12856f358b188dc374e74d1f81d"
version: "a819672dfe4cb3760da448c52ca83e69"
build_date: "2019-08-09T04:48:11.922Z"
size_mb: 432
size: 185978911
sif: "https://datasets.datalad.org/shub/mwiens91/test-error-containers/latest/2019-08-09-36e4fc34-a819672d/a819672dfe4cb3760da448c52ca83e69.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/mwiens91/test-error-containers/latest/2019-08-09-36e4fc34-a819672d/
recipe: https://datasets.datalad.org/shub/mwiens91/test-error-containers/latest/2019-08-09-36e4fc34-a819672d/Singularity
collection: mwiens91/test-error-containers
---

# mwiens91/test-error-containers:latest

```bash
$ singularity pull shub://mwiens91/test-error-containers:latest
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
OSVersion: xenial
MirrorURL: http://us.archive.ubuntu.com/ubuntu/

%files
    error_raise.py /error_raise.py

%post
    apt-get install -y software-properties-common
    apt-add-repository universe
    apt-get update
    apt-get install -y python

    cd /
```

## Collection

 - Name: [mwiens91/test-error-containers](https://github.com/mwiens91/test-error-containers)
 - License: None

