---
id: 2664
name: "khanlab/cfmm2tar"
branch: "master"
tag: "v0.0.1b"
commit: "4cb75071f3d1852cbf57fbb9cfd57478f6991af4"
version: "ee0998a3601a4a86dff34f977b6a3563"
build_date: "2018-04-26T18:47:51.111Z"
size_mb: 633
size: 262115359
sif: "https://datasets.datalad.org/shub/khanlab/cfmm2tar/v0.0.1b/2018-04-26-4cb75071-ee0998a3/ee0998a3601a4a86dff34f977b6a3563.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/khanlab/cfmm2tar/v0.0.1b/2018-04-26-4cb75071-ee0998a3/
recipe: https://datasets.datalad.org/shub/khanlab/cfmm2tar/v0.0.1b/2018-04-26-4cb75071-ee0998a3/Singularity
collection: khanlab/cfmm2tar
---

# khanlab/cfmm2tar:v0.0.1b

```bash
$ singularity pull shub://khanlab/cfmm2tar:v0.0.1b
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:xenial
#########


%setup
#########
mkdir -p $SINGULARITY_ROOTFS/src
cp -Rv . $SINGULARITY_ROOTFS/src


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

pip install -U pip setuptools

cd /src

#install pydicom
mkdir /opt/pydicom
cd /opt/pydicom
git clone https://www.github.com/pydicom/pydicom.git
cd pydicom
git checkout ebf6a79602348d003a1d1324c66626f9f2b05432
python setup.py install


#needed when install dcm4che
apt-get install -y default-jre


#install dcm4che
cd /src
bash install_dcm4che_ubuntu.sh /opt


#########
%environment

#export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

#anaconda2
export PATH=/opt/anaconda2/bin/:$PATH

#dcm4che
export PATH=/opt/dcm4che-3.3.8/bin:$PATH

#python scripts
export PATH=/src:$PATH
export _JAVA_OPTIONS="-Xmx4048m"

%runscript
exec cfmm2tar $@
```

## Collection

 - Name: [khanlab/cfmm2tar](https://github.com/khanlab/cfmm2tar)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

