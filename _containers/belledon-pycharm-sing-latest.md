---
id: 1502
name: "belledon/pycharm-sing"
branch: "master"
tag: "latest"
commit: "ca43547f3d211ae6feb5b09cc7fde0786af1e223"
version: "e2e7104e1c8a32a5aeff937d1838a1be"
build_date: "2018-01-30T14:49:35.386Z"
size_mb: 950
size: 629964831
sif: "https://datasets.datalad.org/shub/belledon/pycharm-sing/latest/2018-01-30-ca43547f-e2e7104e/e2e7104e1c8a32a5aeff937d1838a1be.simg"
url: https://datasets.datalad.org/shub/belledon/pycharm-sing/latest/2018-01-30-ca43547f-e2e7104e/
recipe: https://datasets.datalad.org/shub/belledon/pycharm-sing/latest/2018-01-30-ca43547f-e2e7104e/Singularity
collection: belledon/pycharm-sing
---

# belledon/pycharm-sing:latest

```bash
$ singularity pull shub://belledon/pycharm-sing:latest
```

## Singularity Recipe

```singularity
bootstrap: docker
from: ubuntu:16.04

%post
  apt-get update
  apt-get install -y wget

  mkdir /pycharm-src && cd /pycharm-src
  wget https://download.jetbrains.com/python/pycharm-community-2017.3.2.tar.gz
  tar -xvzf pycharm-community-2017.3.2.tar.gz
```

## Collection

 - Name: [belledon/pycharm-sing](https://github.com/belledon/pycharm-sing)
 - License: None

