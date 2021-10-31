---
id: 10915
name: "tuxtobin/singularity-freebayes"
branch: "master"
tag: "latest"
commit: "56a2411e8badc4d36e19952dcc4bb6c3dbc0982e"
version: "1aa2510745a5fee5dea6eec5a1ecbdf5"
build_date: "2020-11-19T15:37:42.147Z"
size_mb: 1048.0
size: 371372063
sif: "https://datasets.datalad.org/shub/tuxtobin/singularity-freebayes/latest/2020-11-19-56a2411e-1aa25107/1aa2510745a5fee5dea6eec5a1ecbdf5.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/tuxtobin/singularity-freebayes/latest/2020-11-19-56a2411e-1aa25107/
recipe: https://datasets.datalad.org/shub/tuxtobin/singularity-freebayes/latest/2020-11-19-56a2411e-1aa25107/Singularity
collection: tuxtobin/singularity-freebayes
---

# tuxtobin/singularity-freebayes:latest

```bash
$ singularity pull shub://tuxtobin/singularity-freebayes:latest
```

## Singularity Recipe

```singularity
# Install using YUM (CentOS-7)
BootStrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/
Include: yum

# If you want the updates (available at the bootstrap date) to be installed
# inside the container during the bootstrap instead of the General Availability
# point release (7.x) then uncomment the following line
UpdateURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/updates/$basearch/

%help
freebayes is a Bayesian genetic variant detector designed to find small polymorphisms, specifically SNPs (single-nucleotide polymorphisms), indels (insertions and deletions), MNPs (multi-nucleotide polymorphisms), and complex events (composite insertion and substitution events) smaller than the length of a short-read sequencing alignment.
 
%labels
Maintainer Erik Garrison
Version v1.0

%post
yum -y install git make gcc gcc-c++ wget which bzip2-devel xz-devel zlib-devel

mkdir -p /opt/software
cd /opt/software

git clone --recursive https://github.com/ekg/freebayes.git
cd freebayes
make
make install
```

## Collection

 - Name: [tuxtobin/singularity-freebayes](https://github.com/tuxtobin/singularity-freebayes)
 - License: None

