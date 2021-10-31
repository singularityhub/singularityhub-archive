---
id: 4002
name: "khanlab/cfmm2tar"
branch: "master"
tag: "v0.0.1g"
commit: "122d6689c26618a70a7bc7d95abb5eba3c6ca013"
version: "02c6112ecb161f7fea84b1e48d6cfb96"
build_date: "2018-08-15T20:24:43.720Z"
size_mb: 598
size: 244060191
sif: "https://datasets.datalad.org/shub/khanlab/cfmm2tar/v0.0.1g/2018-08-15-122d6689-02c6112e/02c6112ecb161f7fea84b1e48d6cfb96.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/khanlab/cfmm2tar/v0.0.1g/2018-08-15-122d6689-02c6112e/
recipe: https://datasets.datalad.org/shub/khanlab/cfmm2tar/v0.0.1g/2018-08-15-122d6689-02c6112e/Singularity
collection: khanlab/cfmm2tar
---

# khanlab/cfmm2tar:v0.0.1g

```bash
$ singularity pull shub://khanlab/cfmm2tar:v0.0.1g
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:xenial
#########

%setup
#########
mkdir -p $SINGULARITY_ROOTFS/src
cp *.sh  $SINGULARITY_ROOTFS/src

mkdir -p $SINGULARITY_ROOTFS/apps/cfmm2tar
cp *.py  $SINGULARITY_ROOTFS/apps/cfmm2tar
cp cfmm2tar $SINGULARITY_ROOTFS/apps/cfmm2tar

#########
%post
#########

#needed for keytool
if [ ! -e /dev/fd ]
then
ln -s /proc/self/fd /dev/fd
fi

export DEBIAN_FRONTEND=noninteractive
apt-get update && apt-get install -y --no-install-recommends apt-utils \
    sudo \
    git \
    wget \
    curl \
    zip \
    unzip \
    python2.7 \
    python-pip \
    rsync \
    openssh-client

sudo pip install --upgrade pip
sudo pip install --upgrade setuptools

#for some unknown reason, need change the mode:
chmod a+x /apps/cfmm2tar/*.py


##install pydicom
#mkdir /opt/pydicom
#cd /opt/pydicom
#git clone https://www.github.com/pydicom/pydicom.git
#cd pydicom
#git checkout ebf6a79602348d003a1d1324c66626f9f2b05432
#python setup.py install

#dicomunwrap, will install pydicom
cd /apps
git clone https://gitlab.com/cfmm/DicomRaw
cd DicomRaw
sudo pip install -r requirements.txt

#needed when install dcm4che
apt-get install -y default-jre

#install dcm4che
cd /src
bash install_dcm4che_ubuntu.sh /opt

#For retrieving physio dicom files. without this line, all the physio series will not be retrieved with getscu
echo '1.3.12.2.1107.5.9.1:ImplicitVRLittleEndian;ExplicitVRLittleEndian' >>/opt/dcm4che-3.3.8/etc/getscu/store-tcs.properties

#########
%environment

export SCRATCH=/scratch/$USER

#anaconda2
export PATH=/opt/anaconda2/bin/:$PATH

#dcm4che
export PATH=/opt/dcm4che-3.3.8/bin:$PATH

#python scripts
export PATH=/apps/cfmm2tar:$PATH
export _JAVA_OPTIONS="-Xmx2048m"

%runscript
exec cfmm2tar "$@"
```

## Collection

 - Name: [khanlab/cfmm2tar](https://github.com/khanlab/cfmm2tar)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

