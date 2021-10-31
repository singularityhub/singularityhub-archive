---
id: 8693
name: "darachm/safepy"
branch: "master"
tag: "latest"
commit: "5fb6446919aa9416d8ccf3edee8c2568f5e6c38b"
version: "cba5e4993800a46701fc318533ea45e9"
build_date: "2019-05-17T08:23:24.804Z"
size_mb: 1106
size: 485363743
sif: "https://datasets.datalad.org/shub/darachm/safepy/latest/2019-05-17-5fb64469-cba5e499/cba5e4993800a46701fc318533ea45e9.simg"
url: https://datasets.datalad.org/shub/darachm/safepy/latest/2019-05-17-5fb64469-cba5e499/
recipe: https://datasets.datalad.org/shub/darachm/safepy/latest/2019-05-17-5fb64469-cba5e499/Singularity
collection: darachm/safepy
---

# darachm/safepy:latest

```bash
$ singularity pull shub://darachm/safepy:latest
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

    This is for making a singularity image such that it can run python with 
    the `safe` module from Baryshnikova.
    
%post

    apt-get -y update
    apt-get -y upgrade
    apt-get -y install git python3 python3-pip ipython3 python3-dev build-essential sudo python3-tk

    cd /home
    git clone https://github.com/baryshnikova-lab/safepy
    pip3 install -r safepy/extras/requirements.txt
    mv safepy /usr/local/lib/python3.6/dist-packages
```

## Collection

 - Name: [darachm/safepy](https://github.com/darachm/safepy)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

