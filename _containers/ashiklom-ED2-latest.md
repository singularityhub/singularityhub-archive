---
id: 1850
name: "ashiklom/ED2"
branch: "singularity"
tag: "latest"
commit: "d511f19fda421f4c7003ac53d7eea2db26660431"
version: "debe388a69dbe447c598fc5684143ed4"
build_date: "2018-03-02T00:33:59.113Z"
size_mb: 636
size: 217120799
sif: "https://datasets.datalad.org/shub/ashiklom/ED2/latest/2018-03-02-d511f19f-debe388a/debe388a69dbe447c598fc5684143ed4.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ashiklom/ED2/latest/2018-03-02-d511f19f-debe388a/
recipe: https://datasets.datalad.org/shub/ashiklom/ED2/latest/2018-03-02-d511f19f-debe388a/Singularity
collection: ashiklom/ED2
---

# ashiklom/ED2:latest

```bash
$ singularity pull shub://ashiklom/ED2:latest
```

## Singularity Recipe

```singularity
# Singularity recipe file for ED and EDR
# Author: Alexey Shiklomanov
#
# To build a singularity container from this file, run the following command:
# 
# sudo singularity build ed2.simg singularity_recipe
#
# Note that this requires singularity to be installed, and has to be done on a 
# machine where you have sudo access.

Bootstrap: docker
From: ubuntu:xenial

# Sync local ED files inside singularity container
%setup
    rsync -avz --progress ED ${SINGULARITY_ROOTFS}
    rsync -avz --progress EDR ${SINGULARITY_ROOTFS}

# Main install script
%post
    # Install software dependencies
    apt-get update
    apt-get install -y \
        openmpi-bin \
        libopenmpi-dev \
        libhdf5-openmpi-dev \
        netcdf-bin \
        libnetcdf-dev \
        gfortran

    # Install ED
    cd /ED/build
    ./install.sh -k E -p singularity -g

    # Install EDR
    cd /EDR/build
    ./install.sh -k E -p singularity -g
    
    # Create cluster-specific empty directories (required to work natively on these systems)
    # BU SCC:
    mkdir -p /scratch /usr1 /usr2 /usr3 /usr4 /project /projectnb /var/spool/sge /share

    # PEcAn servers
    mkdir -p /fs1 /fs2 /fs3 /fs4

    # BNL MODEX
    mkdir -p /data

%apprun ED
    echo "============= Running ED ============="
    ulimit -s unlimited
    /ED/build/ed_2.1-opt $@
    echo "============= Done ==================="

%apprun EDR
    echo "============= Running EDR ============"
    ulimit -s unlimited
    /EDR/build/ed_2.1-opt $@
    echo "============= Done ==================="
```

## Collection

 - Name: [ashiklom/ED2](https://github.com/ashiklom/ED2)
 - License: None

