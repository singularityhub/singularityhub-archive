---
id: 15268
name: "swarder/NEMO-AMM7-recipe"
branch: "main"
tag: "latest"
commit: "03509907ba51b290959adbfaea72cd7dfc8a46bd"
version: "12b800a5c7640310f6f469db3600ea80"
build_date: "2021-01-13T15:20:20.843Z"
size_mb: 1552.0
size: 463036447
sif: "https://datasets.datalad.org/shub/swarder/NEMO-AMM7-recipe/latest/2021-01-13-03509907-12b800a5/12b800a5c7640310f6f469db3600ea80.sif"
url: https://datasets.datalad.org/shub/swarder/NEMO-AMM7-recipe/latest/2021-01-13-03509907-12b800a5/
recipe: https://datasets.datalad.org/shub/swarder/NEMO-AMM7-recipe/latest/2021-01-13-03509907-12b800a5/Singularity
collection: swarder/NEMO-AMM7-recipe
---

# swarder/NEMO-AMM7-recipe:latest

```bash
$ singularity pull shub://swarder/NEMO-AMM7-recipe:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: vcatechnology/linux-mint

%post
    export DEBIAN_FRONTEND=noninteractive
    apt-get update && apt-get -y dist-upgrade
    apt-get -y install subversion
    apt-get install -y openmpi-bin libmpich-dev libopenmpi-dev lam4-dev gcc g++ gfortran m4 vim
    apt-get install -y build-essential
    apt-get install -y libcurl4-openssl-dev
    ln -s /usr/bin/make /usr/bin/gmake
    apt-get install -y git
    unset DEBIAN_FRONTEND

    mkdir /nemo
    cd /nemo
    git clone https://github.com/swarder/NEMO-AMM7-recipe.git installations
    cd installations/install_scripts
    ./install_zlib.sh
    ./install_hdf5.sh
    ./install_netcdf-c.sh
    ./install_netcdf-fortran.sh
    ./install_xios.sh

%environment
    export LC_ALL=C.UTF-8

%labels
    Author Simon Warder
```

## Collection

 - Name: [swarder/NEMO-AMM7-recipe](https://github.com/swarder/NEMO-AMM7-recipe)
 - License: None

