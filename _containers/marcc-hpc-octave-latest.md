---
id: 880
name: "marcc-hpc/octave"
branch: "v3.8.2-ompi_v4.0-gcc_v4.4"
tag: "latest"
commit: "6291bf1004f0d5ec172de66cb28b83fe621ba4cd"
version: "36dfbeea21ab059921849529221c0d6a"
build_date: "2020-03-12T20:16:15.400Z"
size_mb: 1361
size: 481173535
sif: "https://datasets.datalad.org/shub/marcc-hpc/octave/latest/2020-03-12-6291bf10-36dfbeea/36dfbeea21ab059921849529221c0d6a.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/marcc-hpc/octave/latest/2020-03-12-6291bf10-36dfbeea/
recipe: https://datasets.datalad.org/shub/marcc-hpc/octave/latest/2020-03-12-6291bf10-36dfbeea/Singularity
collection: marcc-hpc/octave
---

# marcc-hpc/octave:latest

```bash
$ singularity pull shub://marcc-hpc/octave:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:latest

%environment
# use bash as default shell
SHELL=/bin/bash
export SHELL

%setup
# runs on host - the path to the image is $SINGULARITY_ROOTFS

%post
# MARCC mounts
mkdir /scratch /work-zfs /data

# post-setup script
yum -y install wget which # i like to download and know where things are

yum install -y epel-release
yum install -y octave octave-devel
OCTAVE_VERSION=`octave-cli --eval version|tail -1|cut -d\  -f3`
touch /usr/share/octave/$OCTAVE_VERSION/etc/built-in-docstrings

yum install -y git mercurial autoconf libtool flex unzip make

ompi=ompi
cd
git clone https://github.com/open-mpi/ompi.git $ompi
cd $ompi
./autogen.pl                                                     > ompi-install.log
./configure --prefix=/usr/local --enable-shared --enable-static >> ompi-install.log
make -j5                                                        >> ompi-install.log
make install                                                    >> ompi-install.log

export LD_CUSTOM_PATH=/usr/local/lib:/usr/local/lib/openmpi
export LD_LIBRARY_PATH=$LD_CUSTOM_PATH:$LD_LIBRARY_PATH
export LD_RUN_PATH=$LD_CUSTOM_PATH:$LD_RUN_PATH

octavempi=octavempi
cd
hg clone http://hg.code.sf.net/p/octave/mpi $octavempi
cd $octavempi
hg archive ../mpi.zip
octave-cli --eval 'pkg install ../mpi.zip'
```

## Collection

 - Name: [marcc-hpc/octave](https://github.com/marcc-hpc/octave)
 - License: None

