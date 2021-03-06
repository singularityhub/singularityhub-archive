---
id: 3783
name: "upendrak/pacbio_singularity"
branch: "master"
tag: "latest"
commit: "bdfa9333540f2734db8756112714bc93fdc94efa"
version: "57e9de607501f52fbc40b276744125c1"
build_date: "2020-02-11T12:50:06.632Z"
size_mb: 4666
size: 3768729631
sif: "https://datasets.datalad.org/shub/upendrak/pacbio_singularity/latest/2020-02-11-bdfa9333-57e9de60/57e9de607501f52fbc40b276744125c1.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/upendrak/pacbio_singularity/latest/2020-02-11-bdfa9333-57e9de60/
recipe: https://datasets.datalad.org/shub/upendrak/pacbio_singularity/latest/2020-02-11-bdfa9333-57e9de60/Singularity
collection: upendrak/pacbio_singularity
---

# upendrak/pacbio_singularity:latest

```bash
$ singularity pull shub://upendrak/pacbio_singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%labels
MAINTAINER Upendra Devisetty <upendra@cyverse.org>
version="5.1.0.26412" description="This Dockerfile is for both isoseq"

%post
apt-get update && apt-get install -y wget unzip rsync locales
echo "LC_ALL=en_US.UTF-8" >> /etc/environment
echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
echo "LANG=en_US.UTF-8" > /etc/locale.conf
locale-gen en_US.UTF-8
wget https://downloads.pacbcloud.com/public/software/installers/smrtlink_5.1.0.26412.zip
unzip -P 9rVkq3HT smrtlink_5.1.0.26412.zip && rm smrtlink_5.1.0.26412.zip
SMRT_ROOT=/smrtlink
SMRT_USER=smrtanalysis
./smrtlink_5.1.0.26412.run --rootdir $SMRT_ROOT --smrttools-only
PATH=/smrtlink/smrtcmds/bin/:$PATH

wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh && bash miniconda.sh -b -p /miniconda
PATH=/miniconda/bin/:$PATH
conda config --add channels conda-forge
conda config --add channels defaults
conda config --add channels r
conda config --add channels bioconda
conda install -y isoseq3

%environment
export SMRT_ROOT=/smrtlink
export SMRT_USER=smrtanalysis
export PATH=/smrtlink/smrtcmds/bin/:$PATH
export PATH=/miniconda/bin/:$PATH

%runscript
exec /bin/bash "$@"
```

## Collection

 - Name: [upendrak/pacbio_singularity](https://github.com/upendrak/pacbio_singularity)
 - License: None

