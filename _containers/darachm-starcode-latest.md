---
id: 8655
name: "darachm/starcode"
branch: "master"
tag: "latest"
commit: "7c96e22933b086c152b34c53537fa37bab58868b"
version: "d10e5ed21e5faaab19f8ca87d2930487"
build_date: "2021-01-02T14:50:08.853Z"
size_mb: 387
size: 149856287
sif: "https://datasets.datalad.org/shub/darachm/starcode/latest/2021-01-02-7c96e229-d10e5ed2/d10e5ed21e5faaab19f8ca87d2930487.simg"
url: https://datasets.datalad.org/shub/darachm/starcode/latest/2021-01-02-7c96e229-d10e5ed2/
recipe: https://datasets.datalad.org/shub/darachm/starcode/latest/2021-01-02-7c96e229-d10e5ed2/Singularity
collection: darachm/starcode
---

# darachm/starcode:latest

```bash
$ singularity pull shub://darachm/starcode:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04
#Bootstrap: localimage
#From: ../ubuntu-1804-updated_container/ubuntu.simg

%labels
MAINTAINER darachm

%help

    This makes a singularity container for starcode
    
%post

    apt-get -y update
    apt-get -y upgrade
    apt-get -y install git g++ gcc-4.8 make

    cd /home
    git clone https://github.com/gui11aume/starcode
    make -C starcode
    mv starcode/starcode /usr/local/bin/starcode

%test

    starcode -h
```

## Collection

 - Name: [darachm/starcode](https://github.com/darachm/starcode)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

