---
id: 1911
name: "starboarder2001/singularity-anaconda"
branch: "master"
tag: "latest"
commit: "269ddbbe3865d906d16d08f270e79934863b24d8"
version: "c83cd6de742f3addae629194ce62d06f"
build_date: "2021-01-25T13:03:04.863Z"
size_mb: 3685
size: 1911836703
sif: "https://datasets.datalad.org/shub/starboarder2001/singularity-anaconda/latest/2021-01-25-269ddbbe-c83cd6de/c83cd6de742f3addae629194ce62d06f.simg"
url: https://datasets.datalad.org/shub/starboarder2001/singularity-anaconda/latest/2021-01-25-269ddbbe-c83cd6de/
recipe: https://datasets.datalad.org/shub/starboarder2001/singularity-anaconda/latest/2021-01-25-269ddbbe-c83cd6de/Singularity
collection: starboarder2001/singularity-anaconda
---

# starboarder2001/singularity-anaconda:latest

```bash
$ singularity pull shub://starboarder2001/singularity-anaconda:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:centos:latest  

%labels
  MAINTAINER David Whiteside
  SPECIES tools

%environment
  RAWR_BASE=/code
  export RAWR_BASE

%post
  yum install -y wget bzip2
  cd /root/ && wget https://repo.continuum.io/archive/Anaconda2-5.1.0-Linux-x86_64.sh
  cd /root/ && chmod 700 ./Anaconda2-5.1.0-Linux-x86_64.sh
  cd /root/ && bash ./Anaconda2-5.1.0-Linux-x86_64.sh -b -p /opt/anaconda/

%runscript
  exec /opt/anaconda/bin/anaconda "$@"
```

## Collection

 - Name: [starboarder2001/singularity-anaconda](https://github.com/starboarder2001/singularity-anaconda)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

