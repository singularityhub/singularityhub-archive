---
id: 515
name: "pegasus-isi/montage-workflow-v2"
branch: "master"
tag: "latest"
commit: "9841ddabbbb97cba60fc57bda767cfe1f3caff61"
version: "577cc3372152a358c34cab99302278a8"
build_date: "2021-04-17T03:09:18.067Z"
size_mb: 1626
size: 511606815
sif: "https://datasets.datalad.org/shub/pegasus-isi/montage-workflow-v2/latest/2021-04-17-9841ddab-577cc337/577cc3372152a358c34cab99302278a8.simg"
url: https://datasets.datalad.org/shub/pegasus-isi/montage-workflow-v2/latest/2021-04-17-9841ddab-577cc337/
recipe: https://datasets.datalad.org/shub/pegasus-isi/montage-workflow-v2/latest/2021-04-17-9841ddab-577cc337/Singularity
collection: pegasus-isi/montage-workflow-v2
---

# pegasus-isi/montage-workflow-v2:latest

```bash
$ singularity pull shub://pegasus-isi/montage-workflow-v2:latest
```

## Singularity Recipe

```singularity
bootstrap:docker
From:centos:7

%environment

PATH=/opt/Montage/bin:/usr/bin:/bin


%setup

mkdir $SINGULARITY_ROOTFS/opt/montage-workflow-v2
cp -a * $SINGULARITY_ROOTFS/opt/montage-workflow-v2/


%post

yum -y upgrade
yum -y install epel-release yum-plugin-priorities

# osg repo
yum -y install http://repo.opensciencegrid.org/osg/3.4/osg-3.4-el7-release-latest.rpm

# pegasus repo
echo -e "# Pegasus\n[Pegasus]\nname=Pegasus\nbaseurl=http://download.pegasus.isi.edu/wms/download/rhel/7/\$basearch/\ngpgcheck=0\nenabled=1\npriority=50" >/etc/yum.repos.d/pegasus.repo

yum -y install \
    astropy-tools \
    file \
    gcc \
    gcc-gfortran \
    java-1.8.0-openjdk \
    java-1.8.0-openjdk-devel \
    libjpeg-turbo-devel \
    openjpeg-devel \
    osg-ca-certs \
    osg-wn-client \
    pegasus \
    python-astropy \
    python-devel \
    python-future \
    python-pip \
    unzip \
    wget

# Cleaning caches to reduce size of image
yum clean all

# wget -nv http://montage.ipac.caltech.edu/download/Montage_v5.0.tar.gz 
cd /opt && \
    wget -nv https://github.com/Caltech-IPAC/Montage/archive/master.zip && \
    unzip master.zip && \
    rm -f master.zip && \
    mv Montage-master Montage && \
    cd Montage && \
    make
```

## Collection

 - Name: [pegasus-isi/montage-workflow-v2](https://github.com/pegasus-isi/montage-workflow-v2)
 - License: [Apache License 2.0](https://api.github.com/licenses/apache-2.0)

