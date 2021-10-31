---
id: 5202
name: "ucr-singularity/cs100"
branch: "master"
tag: "latest"
commit: "57d7bcaed63aa712f1277ba800a8a2203f250046"
version: "f1d094da96593bbb66bc7443001a2a73"
build_date: "2018-10-11T09:24:02.705Z"
size_mb: 211
size: 91422751
sif: "https://datasets.datalad.org/shub/ucr-singularity/cs100/latest/2018-10-11-57d7bcae-f1d094da/f1d094da96593bbb66bc7443001a2a73.simg"
url: https://datasets.datalad.org/shub/ucr-singularity/cs100/latest/2018-10-11-57d7bcae-f1d094da/
recipe: https://datasets.datalad.org/shub/ucr-singularity/cs100/latest/2018-10-11-57d7bcae-f1d094da/Singularity
collection: ucr-singularity/cs100
---

# ucr-singularity/cs100:latest

```bash
$ singularity pull shub://ucr-singularity/cs100:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%post

# Make sure packages are up to date
apt-get update
apt-get -y upgrade

# init in the container
apt-get install -y systemd-sysv
```

## Collection

 - Name: [ucr-singularity/cs100](https://github.com/ucr-singularity/cs100)
 - License: None

