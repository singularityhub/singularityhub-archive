---
id: 7549
name: "mxmlnkn/shub-containers"
branch: "master"
tag: "taurus-mpi"
commit: "44fa73e477cde28bd9d56a69315d204891a5d8d3"
version: "d0139a357d7e3196192225750ded63de"
build_date: "2019-03-01T19:49:14.143Z"
size_mb: 112
size: 39931935
sif: "https://datasets.datalad.org/shub/mxmlnkn/shub-containers/taurus-mpi/2019-03-01-44fa73e4-d0139a35/d0139a357d7e3196192225750ded63de.simg"
url: https://datasets.datalad.org/shub/mxmlnkn/shub-containers/taurus-mpi/2019-03-01-44fa73e4-d0139a35/
recipe: https://datasets.datalad.org/shub/mxmlnkn/shub-containers/taurus-mpi/2019-03-01-44fa73e4-d0139a35/Singularity
collection: mxmlnkn/shub-containers
---

# mxmlnkn/shub-containers:taurus-mpi

```bash
$ singularity pull shub://mxmlnkn/shub-containers:taurus-mpi
```

## Singularity Recipe

```singularity
BootStrap: docker
From: debian:9-slim

%files
    mca-btl-openib-device-params.ini /tmp/

%post
    apt-get update
    apt-get -y install libhwloc1 libibverbs1 libmlx5-1 libmlx4-1
    apt-get -y install wget g++ make libhwloc-dev libibverbs-dev

    mkdir -p /apps /scratch /sw /projects /opt

    cd /apps
    wget -O- 'https://github.com/SchedMD/slurm/archive/slurm-17-02-11-1.tar.gz' | tar -xz &&
    cd slurm-* &&
    ./configure --prefix=/usr --sysconfdir=/etc/slurm --localstatedir=/var --disable-debug
    make -j "$( nproc )" -C contribs/pmi2 install

    cd /apps
    wget -O- 'https://download.open-mpi.org/release/open-mpi/v3.1/openmpi-3.1.3.tar.gz' | tar -xz &&
    cd openmpi-*/ &&
    ./configure --prefix=/usr --enable-shared --enable-mpi-thread-multiple --with-verbs --enable-mpirun-prefix-by-default --with-hwloc --enable-mpi-cxx --with-slurm --with-pmi=/usr --with-pmi-libdir=/usr/lib
    make -j "$( nproc )" install
    ldconfig

    cd /apps/openmpi-*/examples &&
    make -j "$( nproc )" &&
    mkdir -p /opt/openmpi-examples &&
    find . -executable -execdir mv {} /opt/openmpi-examples \;

    mv /tmp/mca-btl-openib-device-params.ini /usr/share/openmpi/

    apt-get -y purge wget g++ make libhwloc-dev libibverbs-dev
    apt-get -y autoremove
    apt-get -y clean
    rm -rf /var/lib/apt/lists/*
    rm -rf /apps/slurm-* /apps/openmpi-*

%runscript
    /opt/openmpi-examples/ring_cxx
```

## Collection

 - Name: [mxmlnkn/shub-containers](https://github.com/mxmlnkn/shub-containers)
 - License: None

