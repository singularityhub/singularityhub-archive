---
id: 4029
name: "willianmh/singularity"
branch: "master"
tag: "latest"
commit: "bd0fc1773b82505b4a74cffd1dab9d0d28da1fb4"
version: "d831d6f5a34d6ecf9309813499ae1a0d"
build_date: "2018-08-31T03:21:36.281Z"
size_mb: 672
size: 256331807
sif: "https://datasets.datalad.org/shub/willianmh/singularity/latest/2018-08-31-bd0fc177-d831d6f5/d831d6f5a34d6ecf9309813499ae1a0d.simg"
url: https://datasets.datalad.org/shub/willianmh/singularity/latest/2018-08-31-bd0fc177-d831d6f5/
recipe: https://datasets.datalad.org/shub/willianmh/singularity/latest/2018-08-31-bd0fc177-d831d6f5/Singularity
collection: willianmh/singularity
---

# willianmh/singularity:latest

```bash
$ singularity pull shub://willianmh/singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:latest


%post

  apt-get update
  apt-get install -y wget git vim tmux tree htop
  apt-get install -y libtool m4 automake
  apt-get install -y unrar unzip
  apt-get install libz-dev

  # Utility and support packages
  apt-get install -y aptitude build-essential cmake gcc g++ gfortran git \
      pkg-config python-pip python-dev software-properties-common



  # wget "http://registrationcenter-download.intel.com/akdlm/irc_nas/tec/12998/parallel_studio_xe_2018_update3_cluster_edition_online.tgz"
  #
  # mkdir ~/psxe_staging_area
	# tar -xvzf parallel_studio_xe_2018_update3_cluster_edition_online.tgz -C ~/psxe_staging_area
  #
	# cd ~/psxe_staging_area/parallel_studio_xe_2018_update3_cluster_edition_online

  # sed -i 's/decline/accept/' silent.cfg
  # sed -i 's/COMPONENTS=DEFAULTS/COMPONENTS=ALL/' silent.cfg
  # sed -i 's/ACTIVATION_TYPE=exist_lic/ACTIVATION_TYPE=serial_number/' silent.cfg
  # sed -i 's/#ACTIVATION_SERIAL_NUMBER=snpat/ACTIVATION_SERIAL_NUMBER=/' silent.cfg

  # ./install.sh --silent=silent.cfg

  # ---------------------------------------------------------------------------
  # Installing METIS
  # ---------------------------------------------------------------------------

  # dependencies
  # wget "https://cmake.org/files/v3.12/cmake-3.12.1.tar.gz"
  # tar -xzf cmake-3.12.1.tar.gz
  # cd cmake-3.12.1
  # ./bootstrap
  # make
  # make install
  # cd /root
  #
  # # Install METIS
  # wget "http://glaros.dtc.umn.edu/gkhome/fetch/sw/metis/metis-5.1.0.tar.gz"
  # tar -xvf metis-5.1.0.tar.gz
  # cd metis-5.1.0
  # make config
  # make
  # cd /root

  # ---------------------------------------------------------------------------
  # Installing MUMPS
  # ---------------------------------------------------------------------------

  # apt-get install -y libblas-dev liblapack-dev
  #
  # wget "http://www.mpich.org/static/downloads/3.2.1/mpich-3.2.1.tar.gz"
  # tar xfz mpich-3.2.1.tar.gz
  # cd mpich-3.2.1
  # ./configure -disable-fast CFLAGS=-O2 FFLAGS=-O2 CXXFLAGS=-O2 FCFLAGS=-O2 -prefix=/opt/mpich3 CC=gcc FC=gfortran F77=gfortran
  # make
  # make install
  # cd /root
  #
  # wget "http://www.netlib.org/blas/blas-3.8.0.tgz"
  # tar -xvzf blas-3.8.0.tgz
  # cd /blas-3.8.0
  # gfortran -c -O3 *.f
  # ar rv libblas.a *.o
  # cp libblas.a /usr/local/lib/

  # cd /root

  # wget "http://www.netlib.org/lapack/lapack-3.8.0.tar.gz"
  # cd lapack-3.8.0
  # mv make.inc.example make.inc
  # make
  # cp liblapack.a /usr/local/lib/
  # cd /root

  # wget "http://mumps.enseeiht.fr/MUMPS_5.1.2.tar.gz"
  # tar -xvf MUMPS_5.1.2.tar.gz
  # cd MUMPS_5.1.2
  # cp Make.inc/Makefile.debian.PAR ./Makefile.inc
  # make all
  # cd /root



%runscript

exec echo Hello "$@"
```

## Collection

 - Name: [willianmh/singularity](https://github.com/willianmh/singularity)
 - License: None

