---
id: 1602
name: "khanlab/retrieve_cfmm"
branch: "master"
tag: "v0.0.5"
commit: "5af788bb9077ccdb7376d91c9070cb6b07d20b06"
version: "d6174dd7091b5ffb3df33c841928ce3f"
build_date: "2018-02-05T10:17:18.712Z"
size_mb: 628
size: 258797599
sif: "https://datasets.datalad.org/shub/khanlab/retrieve_cfmm/v0.0.5/2018-02-05-5af788bb-d6174dd7/d6174dd7091b5ffb3df33c841928ce3f.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/khanlab/retrieve_cfmm/v0.0.5/2018-02-05-5af788bb-d6174dd7/
recipe: https://datasets.datalad.org/shub/khanlab/retrieve_cfmm/v0.0.5/2018-02-05-5af788bb-d6174dd7/Singularity
collection: khanlab/retrieve_cfmm
---

# khanlab/retrieve_cfmm:v0.0.5

```bash
$ singularity pull shub://khanlab/retrieve_cfmm:v0.0.5
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:xenial
#
# dcm4che 3.3.8

#create image
#cd Dropbox/Robarts/singularites/dcm4che
#sudo singularity build ~/singularities/dcm4che.simg Singularity

#########
%setup
#########
mkdir -p $SINGULARITY_ROOTFS/src
cp -Rv . $SINGULARITY_ROOTFS/src
#cp ./*.sh $SINGULARITY_ROOTFS
#ln -fs /usr/share/zoneinfo/US/Pacific-New /etc/localtime && dpkg-reconfigure -f noninteractive tzdata
#mkdir -p $SINGULARITY_ROOTFS/opt/retrieve_cfmm
#cp ./*.py $SINGULARITY_ROOTFS/opt/retrieve_cfmm

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


# checkout specific git release 
#SINGULARITY_TAG=${SINGULARITY_BUILDDEF#Singularity.}
#if [ ! "$SINGULARITY_TAG" = "Singularity" ]
#then
#  git checkout $SINGULARITY_TAG
#fi


#install pydicom
mkdir /opt/pydicom
cd /opt/pydicom
git clone https://www.github.com/pydicom/pydicom.git
cd pydicom
git checkout ebf6a79602348d003a1d1324c66626f9f2b05432
python setup.py install


#needed when install dcm4che
apt-get install -y default-jre

cd /src
bash 14.install_dcm4che_ubuntu.sh /opt


#########
%environment

#export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

#anaconda2
export PATH=/opt/anaconda2/bin/:$PATH

#dcm4che
export PATH=/opt/dcm4che-3.3.8/bin:$PATH

#python scripts
export PATH=/src:$PATH

#########
#fix error if run the image on graham:
#Error occurred during initialization of VM
#java.lang.OutOfMemoryError: unable to create new native thread

export _JAVA_OPTIONS="-Xmx4048m"

%runscript
exec python /src/retrieve_cfmm_tgz.py $@
```

## Collection

 - Name: [khanlab/retrieve_cfmm](https://github.com/khanlab/retrieve_cfmm)
 - License: None

