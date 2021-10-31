---
id: 4035
name: "nskat/Singularity"
branch: "master"
tag: "py2"
commit: "4bc93d5d62eeae9e9a1be0f172e920c6d32df868"
version: "6d6c6391bf891e79d4af74fcb0a4caa5"
build_date: "2018-08-17T18:19:55.883Z"
size_mb: 1512
size: 599494687
sif: "https://datasets.datalad.org/shub/nskat/Singularity/py2/2018-08-17-4bc93d5d-6d6c6391/6d6c6391bf891e79d4af74fcb0a4caa5.simg"
url: https://datasets.datalad.org/shub/nskat/Singularity/py2/2018-08-17-4bc93d5d-6d6c6391/
recipe: https://datasets.datalad.org/shub/nskat/Singularity/py2/2018-08-17-4bc93d5d-6d6c6391/Singularity
collection: nskat/Singularity
---

# nskat/Singularity:py2

```bash
$ singularity pull shub://nskat/Singularity:py2
```

## Singularity Recipe

```singularity
BootStrap:docker
From:tensorflow/tensorflow:1.7.1


%post
apt-get update && apt-get install -y --no-install-recommends apt-utils
apt-get --force-yes -y install wget
apt-get install sudo


pip install keras
pip install tables
pip install cython
apt-get -y --force-yes install git-core
apt-get -y --force-yes install apt-file 
apt-get -y --force-yes install python-tk
apt-file update
```

## Collection

 - Name: [nskat/Singularity](https://github.com/nskat/Singularity)
 - License: None

