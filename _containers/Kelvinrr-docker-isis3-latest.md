---
id: 1426
name: "Kelvinrr/docker-isis3"
branch: "master"
tag: "latest"
commit: "d9bfff080b82ff83a3178266713cc3cb374108b9"
version: "d31485ec9b681b5ac7ef3a47caf8e746"
build_date: "2018-01-22T19:49:48.198Z"
size_mb: 3161
size: 1171521567
sif: "https://datasets.datalad.org/shub/Kelvinrr/docker-isis3/latest/2018-01-22-d9bfff08-d31485ec/d31485ec9b681b5ac7ef3a47caf8e746.simg"
url: https://datasets.datalad.org/shub/Kelvinrr/docker-isis3/latest/2018-01-22-d9bfff08-d31485ec/
recipe: https://datasets.datalad.org/shub/Kelvinrr/docker-isis3/latest/2018-01-22-d9bfff08-d31485ec/Singularity
collection: Kelvinrr/docker-isis3
---

# Kelvinrr/docker-isis3:latest

```bash
$ singularity pull shub://Kelvinrr/docker-isis3:latest
```

## Singularity Recipe

```singularity
# Trivial Singularity image, piggy backs off of Docker container
Bootstrap: docker
From: kelvinrr/isis3

# handle permission issue in Singularity for Docker's home folder
%post
  mkdir /common /packages /scratch
  chmod 775 /root

%runscript
  /bin/bash
```

## Collection

 - Name: [Kelvinrr/docker-isis3](https://github.com/Kelvinrr/docker-isis3)
 - License: None

