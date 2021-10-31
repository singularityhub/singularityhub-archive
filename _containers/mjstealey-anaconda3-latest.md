---
id: 3009
name: "mjstealey/anaconda3"
branch: "master"
tag: "latest"
commit: "c955e8f37133e4a533f15a0226d2a6248e70aaa8"
version: "62ffde45ef7203285f98e1e529e183b9"
build_date: "2020-08-12T10:56:46.028Z"
size_mb: 4000
size: 2058182687
sif: "https://datasets.datalad.org/shub/mjstealey/anaconda3/latest/2020-08-12-c955e8f3-62ffde45/62ffde45ef7203285f98e1e529e183b9.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/mjstealey/anaconda3/latest/2020-08-12-c955e8f3-62ffde45/
recipe: https://datasets.datalad.org/shub/mjstealey/anaconda3/latest/2020-08-12-c955e8f3-62ffde45/Singularity
collection: mjstealey/anaconda3
---

# mjstealey/anaconda3:latest

```bash
$ singularity pull shub://mjstealey/anaconda3:latest
```

## Singularity Recipe

```singularity
Bootstrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/
Include: yum

%help

%setup

%files

%labels
  Maintainer Michael J. Stealey
  Maintainer_Email stealey@renci.org
  Anaconda_Version 5.1.0
  Python_Version 3.6.4

%environment
  export ANACONDA_VERSION=5.1.0
  export PATH=/usr/local/anaconda/bin:$PATH

%post
  export ANACONDA_VERSION=5.1.0

  yum -y install \
    bzip2 ca-certificates \
    libglib2.0-0 libxext6 libsm6 libxrender1 \
    git mercurial subversion
  cd /usr/local
  curl -L https://repo.anaconda.com/archive/Anaconda3-${ANACONDA_VERSION}-Linux-x86_64.sh -o Anaconda3-${ANACONDA_VERSION}-Linux-x86_64.sh
  bash Anaconda3-${ANACONDA_VERSION}-Linux-x86_64.sh -b -p /usr/local/anaconda

%apprun python
  exec python "${@}"

%apprun conda
  exec conda "${@}"

%runscript
  exec "${@}"

%test
```

## Collection

 - Name: [mjstealey/anaconda3](https://github.com/mjstealey/anaconda3)
 - License: None

