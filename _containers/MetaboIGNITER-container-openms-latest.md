---
id: 12517
name: "MetaboIGNITER/container-openms"
branch: "develop"
tag: "latest"
commit: "e613698e34ea313e88a1afb3027312b8f89df7b8"
version: "f571fb0bbafa93a049e952bfbd5d0945"
build_date: "2020-03-13T13:50:04.852Z"
size_mb: 3400.0
size: 1343569951
sif: "https://datasets.datalad.org/shub/MetaboIGNITER/container-openms/latest/2020-03-13-e613698e-f571fb0b/f571fb0bbafa93a049e952bfbd5d0945.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/MetaboIGNITER/container-openms/latest/2020-03-13-e613698e-f571fb0b/
recipe: https://datasets.datalad.org/shub/MetaboIGNITER/container-openms/latest/2020-03-13-e613698e-f571fb0b/Singularity
collection: MetaboIGNITER/container-openms
---

# MetaboIGNITER/container-openms:latest

```bash
$ singularity pull shub://MetaboIGNITER/container-openms:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:xenial
%files
runTest1.sh /usr/local/bin/runTest1.sh
%labels
MAINTAINER PhenoMeNal-H2020 Project ( phenomenal-h2020-users@googlegroups.com )
Description="OpenMS port."
software.version="2.1.0"
version="0.2"
%post



# Install dependencies
apt-get -y update
apt-get -y --no-install-recommends install cmake g++ autoconf automake qt4-dev-tools patch libtool make git software-properties-common python-software-properties libboost-all-dev libsvm-dev libglpk-dev libzip-dev zlib1g-dev libxerces-c-dev libbz2-dev libqt4-dbg libqt4-dev libqt4-opengl-dev libqtwebkit-dev
apt-get -y --no-install-recommends install libboost-regex-dev libboost-iostreams-dev libboost-date-time-dev libboost-math-dev libsvm-dev libglpk-dev libzip-dev zlib1g-dev libxerces-c-dev libbz2-dev seqan-dev libwildmagic-dev libwildmagic5v5 libwildmagic5v5-dbg libeigen3-dev
apt-get -y --no-install-recommends install python-setuptools python-pip python-nose python-numpy python-wheel cython cython-dbg doxygen doxygen-dbg

pip install autowrap

# Create needed directories
mkdir /usr/src/openms
mkdir /usr/src/openms/contrib-build
mkdir /usr/src/openms/openms-build

# Build contrib stuff
cd /usr/src/openms
git clone https://github.com/OpenMS/contrib
cd /usr/src/openms/contrib-build
cmake -DBUILD_TYPE=SEQAN ../contrib && \
cmake -DBUILD_TYPE=WILDMAGIC ../contrib && \
cmake -DBUILD_TYPE=EIGEN ../contrib

# Build OpenMS
cd /usr/src/openms
git clone https://github.com/OpenMS/OpenMS
cd /usr/src/openms/OpenMS
git checkout tags/Release2.1.0
cd /usr/src/openms/openms-build
cmake -DCMAKE_PREFIX_PATH="/usr/src/openms/contrib-build/;/usr/src/openms/contrib/;/usr/;/usr/local" -DBOOST_USE_STATIC=OFF -DHAS_XSERVER=Off ../OpenMS && make

# Build PyOpenMS
#WORKDIR /usr/src/openms/openms-build
#RUN cmake -DCMAKE_PREFIX_PATH="/usr/src/openms/contrib-build/;/usr/src/openms/contrib/;/usr/;/usr/local" -DBOOST_USE_STATIC=OFF -DHAS_XSERVER=Off -DPYOPENMS=ON ../OpenMS && make pyopenms
#RUN easy_install pyopenms
pip install -Iv pyopenms==2.1.0

# Clean up
apt-get -y clean && apt-get -y autoremove && rm -rf /var/lib/{cache,log}/ /tmp/* /var/tmp/*

# Set environment and user
PATH=/usr/src/openms/openms-build/bin/:$PATH
#RUN groupadd -g 9999 -f openms
#RUN useradd -d /home/openms -m -g openms -u 9999 -s /bin/bash openms
#RUN echo 'openms:openms' | chpasswd
#WORKDIR /home/openms
su - # openms # #USER openms

# Add testing to container

# Docker entrypoint
#ENTRYPOINT [ "/bin/sh" ]

%environment
export PATH=/usr/src/openms/openms-build/bin/:$PATH
%runscript
cd /usr/src/openms/openms-build
exec /bin/bash "$@"
%startscript
cd /usr/src/openms/openms-build
exec /bin/bash "$@"
```

## Collection

 - Name: [MetaboIGNITER/container-openms](https://github.com/MetaboIGNITER/container-openms)
 - License: None

