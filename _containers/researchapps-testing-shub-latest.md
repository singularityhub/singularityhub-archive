---
id: 14485
name: "researchapps/testing-shub"
branch: "master"
tag: "latest"
commit: "298eb56a357d10d6fba761cbff63ed8531b9b191"
version: "ecb1d8d87a89def036318949620a56882a15c944cd68612deb72fd93140e4246"
build_date: "2020-09-28T17:12:22.274Z"
size_mb: 337.140625
size: 353517568
sif: "https://datasets.datalad.org/shub/researchapps/testing-shub/latest/2020-09-28-298eb56a-ecb1d8d8/ecb1d8d87a89def036318949620a56882a15c944cd68612deb72fd93140e4246.sif"
url: https://datasets.datalad.org/shub/researchapps/testing-shub/latest/2020-09-28-298eb56a-ecb1d8d8/
recipe: https://datasets.datalad.org/shub/researchapps/testing-shub/latest/2020-09-28-298eb56a-ecb1d8d8/Singularity
collection: researchapps/testing-shub
---

# researchapps/testing-shub:latest

```bash
$ singularity pull shub://researchapps/testing-shub:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%environment
    export LC_ALL=C
    export DEBIAN_FRONTEND=noninteractive

%post
  export DEBIAN_FRONTEND=noninteractive
  apt-get update
  apt-get install -y git wget

  echo "DONE with OS install and update"
  echo "Define environment variable for conda install path"
  export ROOT_INSTALL_PATH="/usr/local"
  export CONDA_INSTALL_PATH="/usr/local/miniconda3"
  echo "Change to install directory"
  cd $ROOT_INSTALL_PATH
  echo "Download and install miniconda"
  wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
  echo "Install conda"
  bash Miniconda3-latest-Linux-x86_64.sh -b -p $CONDA_INSTALL_PATH
```

## Collection

 - Name: [researchapps/testing-shub](https://github.com/researchapps/testing-shub)
 - License: None

