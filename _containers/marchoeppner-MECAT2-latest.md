---
id: 8999
name: "marchoeppner/MECAT2"
branch: "master"
tag: "latest"
commit: "1706b3463ec5a8274deb3485887c14d91a44c4b4"
version: "9af9ceb6e814691c4255498efc81d8ca"
build_date: "2019-05-10T10:48:53.620Z"
size_mb: 354
size: 128639007
sif: "https://datasets.datalad.org/shub/marchoeppner/MECAT2/latest/2019-05-10-1706b346-9af9ceb6/9af9ceb6e814691c4255498efc81d8ca.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/marchoeppner/MECAT2/latest/2019-05-10-1706b346-9af9ceb6/
recipe: https://datasets.datalad.org/shub/marchoeppner/MECAT2/latest/2019-05-10-1706b346-9af9ceb6/Singularity
collection: marchoeppner/MECAT2
---

# marchoeppner/MECAT2:latest

```bash
$ singularity pull shub://marchoeppner/MECAT2:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:ubuntu:19.04

%labels
    MAINTAINER Marc Hoeppner <m.hoeppner@ikmb.uni-kiel.de>
    DESCRIPTION Singularity image containing Mecat2
    VERSION 0.1

%environment
    PATH=/opt/mecat2/Linux-amd64/bin:$PATH
    export PATH
    LC_ALL=en_US.UTF-8
    export LC_ALL
    LANG=en_US.UTF-8
    export LANG

%files

%post

apt-get -y update
apt-get -y install wget build-essential perl coreutils locales

locale-gen en_US.UTF-8
update-locale LANG=en_US.UTF-8

cd /opt

wget https://github.com/xiaochuanle/MECAT2/releases/download/20192026/mecat2_20190226_linuax_amd64.tar.gz
tar -xvf mecat2_20190226_linuax_amd64.tar.gz
rm mecat2_20190226_linuax_amd64.tar.gz
mv MECAT2 mecat2
```

## Collection

 - Name: [marchoeppner/MECAT2](https://github.com/marchoeppner/MECAT2)
 - License: None

