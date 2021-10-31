---
id: 773
name: "divetea/debian"
branch: "master"
tag: "latest"
commit: "12bfe05b348072eb62a6c730d2f9f2dc1f1aaef0"
version: "4431bac4fcb6788acd1d6a55c056f209"
build_date: "2020-04-22T12:53:55.247Z"
size_mb: 471
size: 131092511
sif: "https://datasets.datalad.org/shub/divetea/debian/latest/2020-04-22-12bfe05b-4431bac4/4431bac4fcb6788acd1d6a55c056f209.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/divetea/debian/latest/2020-04-22-12bfe05b-4431bac4/
recipe: https://datasets.datalad.org/shub/divetea/debian/latest/2020-04-22-12bfe05b-4431bac4/Singularity
collection: divetea/debian
---

# divetea/debian:latest

```bash
$ singularity pull shub://divetea/debian:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: debian:jessie

%help
You are using a container with debian_jessie

%environment
LC_ALL=C
export LC_ALL
LC_NUMERIC=en_GB.UTF-8
export LC_NUMERIC

%post
apt-get -y update
apt-get -y dist-upgrade
apt-get -y install file
apt-get -y install libpng12-0 libmng1
apt-get -y install build-essential

%runscript
echo "Arguments received: $*"
```

## Collection

 - Name: [divetea/debian](https://github.com/divetea/debian)
 - License: None

