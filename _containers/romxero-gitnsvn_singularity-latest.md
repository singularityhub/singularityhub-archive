---
id: 11846
name: "romxero/gitnsvn_singularity"
branch: "master"
tag: "latest"
commit: "1af90ed51d7298c4dad2448fa1c15a40045c654b"
version: "b498e798af4dc0f4c541d006c63a9652"
build_date: "2019-12-19T19:00:21.250Z"
size_mb: 784.0
size: 273268767
sif: "https://datasets.datalad.org/shub/romxero/gitnsvn_singularity/latest/2019-12-19-1af90ed5-b498e798/b498e798af4dc0f4c541d006c63a9652.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/romxero/gitnsvn_singularity/latest/2019-12-19-1af90ed5-b498e798/
recipe: https://datasets.datalad.org/shub/romxero/gitnsvn_singularity/latest/2019-12-19-1af90ed5-b498e798/Singularity
collection: romxero/gitnsvn_singularity
---

# romxero/gitnsvn_singularity:latest

```bash
$ singularity pull shub://romxero/gitnsvn_singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:xenial

%labels
Author "Randall Cab White - rcwhite@stanford.edu"


#########
#%setup
#########

#Downlaod packages
%post
  apt-get -ym update
  apt-get -ym install wget curl git git-all subversion python python3 language-pack-en-base
  
%environment
  export IMAGE_NAME="git_and_subversion"
  export LC_ALL=C
%runscript
```

## Collection

 - Name: [romxero/gitnsvn_singularity](https://github.com/romxero/gitnsvn_singularity)
 - License: None

