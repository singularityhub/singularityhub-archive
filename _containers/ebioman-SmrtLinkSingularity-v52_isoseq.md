---
id: 3979
name: "ebioman/SmrtLinkSingularity"
branch: "add-license-1"
tag: "v52_isoseq"
commit: "f6e3184f6f3587d7edf69afe22624254db18c0ae"
version: "5dac424d36869bac6543f94a755d0c77"
build_date: "2018-08-14T19:41:13.184Z"
size_mb: 3429
size: 2344894495
sif: "https://datasets.datalad.org/shub/ebioman/SmrtLinkSingularity/v52_isoseq/2018-08-14-f6e3184f-5dac424d/5dac424d36869bac6543f94a755d0c77.simg"
url: https://datasets.datalad.org/shub/ebioman/SmrtLinkSingularity/v52_isoseq/2018-08-14-f6e3184f-5dac424d/
recipe: https://datasets.datalad.org/shub/ebioman/SmrtLinkSingularity/v52_isoseq/2018-08-14-f6e3184f-5dac424d/Singularity
collection: ebioman/SmrtLinkSingularity
---

# ebioman/SmrtLinkSingularity:v52_isoseq

```bash
$ singularity pull shub://ebioman/SmrtLinkSingularity:v52_isoseq
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:latest

%labels
maintained by Emanuel Schmid @ VITAL-IT
Version v5.1.0.26412

%help
This is the current PacBio collection of tools as in smrtlink version V5.1.0 from
[I am link](https://www.pacb.com/support/software-downloads/).
It furthermore includes the

 - isoseq3

In CentOS instead of Ubuntu to please admins

the standard tools should be available, not the graphical interface though

%environment
    SHELL=/bin/bash
        
%post

# install software
yum update -y -q && yum install -y -q \
        build-essential \
        gcc-multilib \
        libboost-all-dev \
        libhdf5-serial-dev \
        zlib1g-dev \
        pkg-config \
        wget \
        rsync \
        unzip \
        which \
        bzip2 \
        dirname
    


echo "add new user if not existent"
        
SMRT_USER=smrtanalysis
if ! grep -c "smrtanalysis:" /etc/passwd
then
        useradd  -g users -d /home/$SMRT_USER -s /bin/bash -p PacBio $SMRT_USER
else
        echo    "user already exists"
fi

echo "generate a new PacBio root directory and make smrtuser owner"

SMRT=/opt/pacbio
if [ ! -d $SMRT ]
then
        mkdir $SMRT
        chown smrtanalysis:users $SMRT
fi





echo "now switch to smrt-user"

su $SMRT_USER
SMRT_ROOT="/opt/pacbio/smrtlink"
cd $SMRT

echo "download and extract smrtlink"
wget -c https://downloads.pacbcloud.com/public/software/installers/smrtlink_5.1.0.26412.zip --no-check-certificate
unzip -u -P 9rVkq3HT smrtlink_5.1.0.26412.zip


if [ -d $SMRT_ROOT ] 
then 
        rm -rf $SMRT_ROOT
        ./smrtlink_5.1.0.26412.run smrtlink --rootdir $SMRT_ROOT --smrttools-only       
else
        ./smrtlink_5.1.0.26412.run smrtlink --rootdir $SMRT_ROOT --smrttools-only       
fi

wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda3.sh 
bash miniconda3.sh -b -p /opt/pacbio/miniconda
export PATH="/opt/pacbio/miniconda/bin/:$PATH"
conda config --add channels conda-forge
conda config --add channels defaults
conda config --add channels r
conda config --add channels bioconda
conda install -y isoseq3

echo "cleaning up"
rm smrtlink_5.1.0.26412.*


%environment
export PATH=/opt/pacbio/smrtlink/smrtcmds/bin/:$PATH
export PATH=/opt/pacbio/miniconda/bin/:$PATH

%runscript
exec /bin/bash "$@"
```

## Collection

 - Name: [ebioman/SmrtLinkSingularity](https://github.com/ebioman/SmrtLinkSingularity)
 - License: [MIT License](https://api.github.com/licenses/mit)

