---
id: 15546
name: "timo-singularity/rivet"
branch: "master"
tag: "latest"
commit: "2cdf34808654d4f843bd7b5dcd7be7daec2e4743"
version: "6a37bb5953d19a96880517f7b9b89bb4"
build_date: "2021-03-30T12:26:52.598Z"
size_mb: 1965.0
size: 514953247
sif: "https://datasets.datalad.org/shub/timo-singularity/rivet/latest/2021-03-30-2cdf3480-6a37bb59/6a37bb5953d19a96880517f7b9b89bb4.sif"
url: https://datasets.datalad.org/shub/timo-singularity/rivet/latest/2021-03-30-2cdf3480-6a37bb59/
recipe: https://datasets.datalad.org/shub/timo-singularity/rivet/latest/2021-03-30-2cdf3480-6a37bb59/Singularity
collection: timo-singularity/rivet
---

# timo-singularity/rivet:latest

```bash
$ singularity pull shub://timo-singularity/rivet:latest
```

## Singularity Recipe

```singularity
#Bootstrap: library
#From: centos:8
Bootstrap: docker
From: centos:8

%help

  Base container with Rivet

%environment
  
  . /usr/local/rivetenv.sh

%post
  
  yum -y update
  yum -y install python3 python3-devel python3-pip
  ln -fs /usr/bin/python3 /usr/bin/python
  yum -y install wget zlib-devel
  yum -y groupinstall 'Development Tools'
  yum -y install gcc-gfortran cmake

  wget https://gitlab.com/hepcedar/rivetbootstrap/raw/3.1.0/rivet-bootstrap
  chmod +x rivet-bootstrap
  INSTALL_PREFIX=/usr/local ./rivet-bootstrap

  ldconfig
  yum clean all
```

## Collection

 - Name: [timo-singularity/rivet](https://github.com/timo-singularity/rivet)
 - License: None

