---
id: 6401
name: "sameerd/parliament2"
branch: "master"
tag: "latest"
commit: "3528254a64b83082344a9e1b5b671f79222d54a6"
version: "ab278066b752478c8a3905d27e4d2cba"
build_date: "2021-04-19T22:15:01.378Z"
size_mb: 5583
size: 2464342047
sif: "https://datasets.datalad.org/shub/sameerd/parliament2/latest/2021-04-19-3528254a-ab278066/ab278066b752478c8a3905d27e4d2cba.simg"
url: https://datasets.datalad.org/shub/sameerd/parliament2/latest/2021-04-19-3528254a-ab278066/
recipe: https://datasets.datalad.org/shub/sameerd/parliament2/latest/2021-04-19-3528254a-ab278066/Singularity
collection: sameerd/parliament2
---

# sameerd/parliament2:latest

```bash
$ singularity pull shub://sameerd/parliament2:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:14.04

%setup
tar -czf ${SINGULARITY_ROOTFS}/resources.tar.gz resources/

%files
parliament2.py /
parliament2.sh /
svtyper_env.yml /

%labels
MAINTAINER Originally written by Samantha Zarate. Minor modifications by Sameer

%post
# Set the base image to Ubuntu 14.04

# File Author / Maintainer

# System packages 
apt-get update && apt-get install -y curl wget

# Install miniconda to /miniconda
curl -LO http://repo.continuum.io/miniconda/Miniconda-latest-Linux-x86_64.sh
bash Miniconda-latest-Linux-x86_64.sh -p /miniconda -b
rm Miniconda-latest-Linux-x86_64.sh
PATH=/miniconda/bin:${PATH}
# RUN conda update -y conda

/bin/bash -c "echo 'deb http://dnanexus-apt-prod.s3.amazonaws.com/ubuntu trusty/amd64/' > /etc/apt/sources.list.d/dnanexus.list"
/bin/bash -c "echo 'deb http://dnanexus-apt-prod.s3.amazonaws.com/ubuntu trusty/all/' >> /etc/apt/sources.list.d/dnanexus.list"
wget https://wiki.dnanexus.com/images/files/ubuntu-signing-key.gpg
apt-key add ubuntu-signing-key.gpg

apt-get update -y && apt-get upgrade -y && apt-get install -y --force-yes \
autoconf \
bedtools \
bsdtar \
build-essential \
cmake \
dx-toolkit \
g++ \
gcc \
gettext \
gfortran \
git \
gzip \
inkscape \
libc6 \
libcurl4-openssl-dev \
libfontconfig \
libfreetype6-dev \
libgsl0-dev \
libgtkmm-3.0-dev \
libhdf5-serial-dev  \
liblzma-dev \
liblzo2-dev \
libpangomm-1.4-dev \
libpng-dev \
libpopt-dev \
libpthread-stubs0-dev \
librsvg2-bin \
librsvg2-dev \
libsqlite3-dev \
libstdc++6 \
libx11-dev \
libxext-dev \
libxft-dev \
libxpm-dev \
libxslt1-dev \
python-pip \
sqlite3 \
wget \
wkhtmltopdf \
xvfb \
zlib1g-dev
apt-get update

conda config --add channels conda-forge
conda config --add channels bioconda
conda config --add channels defaults
conda install -c bioconda samtools
conda install -c bioconda sambamba -y
conda install -c bioconda bcftools -y
conda install -c bcbio bx-python -y
conda install -c defaults networkx -y
conda install -c bioconda samblaster -y
conda install gcc_linux-64 -y
conda install -c bioconda manta
conda update -y pyopenssl

cd /
tar -zxf resources.tar.gz 
cp -a /resources/* /
rm -rf /resources/

conda install -c defaults -y numpy
pip install https://github.com/bioinform/breakseq2/archive/2.2.tar.gz
pip install pycparser
pip install asn1crypto
pip install idna
pip install ipaddress

pip install dxpy

# create separate conda environments for svviz and svtyper
conda create -y --name svviz_env svviz

# We have to use a slightly different method for 
# svtyper as it installs software directly from git 
conda env create --name svtyper_env --file /svtyper_env.yml
#rm /svtyper_env.yml

cd /root
mkdir -p /home/dnanexus/in /home/dnanexus/out

cd /home/dnanexus

/bin/bash -c "source /etc/profile.d/dnanexus.environment.sh"

PATH=${PATH}:/home/dnanexus/
PATH=${PATH}:/opt/conda/bin/
PATH=${PATH}:/usr/bin/
PYTHONPATH=${PYTHONPATH}:/opt/conda/bin/
ROOTSYS=/home/dnanexus/root
LD_LIBRARY_PATH=/usr/lib/root/lib
LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/home/dnanexus/root/lib
DYLD_LIBRARY_PATH=/usr/lib/root/lib
HTSLIB_LIBRARY_DIR=/usr/local/lib
HTSLIB_INCLUDE_DIR=/usr/local/include

cd /home/dnanexus
mv /parliament2.py .
mv /parliament2.sh .
chmod +x parliament2.py
chmod +x parliament2.sh

%environment
export PATH=/miniconda/bin:${PATH}
export PATH=${PATH}:/home/dnanexus/
export PATH=${PATH}:/opt/conda/bin/
export PATH=${PATH}:/usr/bin/
export PYTHONPATH=${PYTHONPATH}:/opt/conda/bin/
export ROOTSYS=/home/dnanexus/root
export LD_LIBRARY_PATH=/usr/lib/root/lib
export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/home/dnanexus/root/lib
export DYLD_LIBRARY_PATH=/usr/lib/root/lib
export HTSLIB_LIBRARY_DIR=/usr/local/lib
export HTSLIB_INCLUDE_DIR=/usr/local/include

%runscript
exec /home/dnanexus/parliament2.py "$@"
```

## Collection

 - Name: [sameerd/parliament2](https://github.com/sameerd/parliament2)
 - License: [Apache License 2.0](https://api.github.com/licenses/apache-2.0)

