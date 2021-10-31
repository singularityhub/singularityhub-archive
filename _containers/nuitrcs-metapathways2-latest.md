---
id: 4941
name: "nuitrcs/metapathways2"
branch: "master"
tag: "latest"
commit: "8f5733bbc9c8196c52c11bdb767edac68c837e51"
version: "cdbda2a340ad6b3fc3984ffdc3406a1c"
build_date: "2018-09-21T20:39:55.034Z"
size_mb: 4321
size: 1593688095
sif: "https://datasets.datalad.org/shub/nuitrcs/metapathways2/latest/2018-09-21-8f5733bb-cdbda2a3/cdbda2a340ad6b3fc3984ffdc3406a1c.simg"
url: https://datasets.datalad.org/shub/nuitrcs/metapathways2/latest/2018-09-21-8f5733bb-cdbda2a3/
recipe: https://datasets.datalad.org/shub/nuitrcs/metapathways2/latest/2018-09-21-8f5733bb-cdbda2a3/Singularity
collection: nuitrcs/metapathways2
---

# nuitrcs/metapathways2:latest

```bash
$ singularity pull shub://nuitrcs/metapathways2:latest
```

## Singularity Recipe

```singularity
# Copyright (c) 2015-2016, Gregory M. Kurtzer. All rights reserved.
#
# "Singularity" Copyright (c) 2016, The Regents of the University of California,
# through Lawrence Berkeley National Laboratory (subject to receipt of any
# required approvals from the U.S. Dept. of Energy).  All rights reserved.

BootStrap: debootstrap
OSVersion: xenial
MirrorURL: http://us.archive.ubuntu.com/ubuntu/


%runscript
    echo "Please run this container image using \`singularity exec\`."

%environment
    LANG=C.UTF-8
    LC_ALL=C.UTF-8

%post
    sed -i 's/$/ universe/' /etc/apt/sources.list
    apt-get update
    apt-get -y --allow-unauthenticated install vim build-essential wget git gfortran bison
    apt-get -y --allow-unauthenticated install libibverbs-dev libibmad-dev libibumad-dev
    apt-get -y --allow-unauthenticated install librdmacm-dev libmlx5-dev libmlx4-dev unzip
    apt-get -y --allow-unauthenticated install libmotif-common csh tcsh
    apt-get -y --allow-unauthenticated install curl

    echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \
    echo 'export XDG_RUNTIME_DIR=""' > /etc/profile.d/conda.sh && \
    wget --quiet https://repo.continuum.io/archive/Anaconda3-5.2.0-Linux-x86_64.sh -O ~/anaconda.sh && \
    /bin/bash ~/anaconda.sh -b -p /opt/conda && \
    rm ~/anaconda.sh
    /opt/conda/bin/conda install --yes dask distributed -c conda-forge
    /opt/conda/bin/conda update --yes numba pandas h5py
    /opt/conda/bin/conda clean --yes --all

    cd /opt
    git clone https://github.com/hallamlab/metapathways2.git

    curl -L https://www.dropbox.com/s/ye3kpve041e0r39/MetaPathways_DBs.zip?dl=1 > MetaPathwaysDBs.zip
    unzip MetaPathwaysDBs.zip
    rm MetaPathwaysDBs.zip

    echo 'export PATH=/opt/metapathways2/executables/ubuntu:/opt/conda/bin:$PATH' >> $SINGULARITY_ENVIRONMENT
```

## Collection

 - Name: [nuitrcs/metapathways2](https://github.com/nuitrcs/metapathways2)
 - License: [MIT License](https://api.github.com/licenses/mit)

