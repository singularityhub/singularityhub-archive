---
id: 13379
name: "jacobhepkema/basset_singularity_from_docker"
branch: "master"
tag: "latest"
commit: "95dfe5d0edef0b048e4ab4ce65b23c86c49dd7d1"
version: "e13b939efd140edf8bd35f7bd01cfa45"
build_date: "2020-06-16T16:53:50.194Z"
size_mb: 3362.0
size: 1569386527
sif: "https://datasets.datalad.org/shub/jacobhepkema/basset_singularity_from_docker/latest/2020-06-16-95dfe5d0-e13b939e/e13b939efd140edf8bd35f7bd01cfa45.sif"
url: https://datasets.datalad.org/shub/jacobhepkema/basset_singularity_from_docker/latest/2020-06-16-95dfe5d0-e13b939e/
recipe: https://datasets.datalad.org/shub/jacobhepkema/basset_singularity_from_docker/latest/2020-06-16-95dfe5d0-e13b939e/Singularity
collection: jacobhepkema/basset_singularity_from_docker
---

# jacobhepkema/basset_singularity_from_docker:latest

```bash
$ singularity pull shub://jacobhepkema/basset_singularity_from_docker:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: lzamparo/basset

%help
    lzamparo's basset docker image
  
%labels
    Maintainer @jacobhepkema
    Version v0.1

# I think that the files I need for Basset are in /root/Basset/src.
# To allow for access:
%post
    chmod -R 777 /root
    chmod -R 777 /opt
    chmod -R 777 /usr
```

## Collection

 - Name: [jacobhepkema/basset_singularity_from_docker](https://github.com/jacobhepkema/basset_singularity_from_docker)
 - License: None

