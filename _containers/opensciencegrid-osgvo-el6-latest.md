---
id: 412
name: "opensciencegrid/osgvo-el6"
branch: "master"
tag: "latest"
commit: "3e83e6653584e64eb52b9d8e27073cab78fe151e"
version: "60ffeee7df556250515e6cae8580ce42"
build_date: "2018-11-07T13:35:00.974Z"
size_mb: 5767
size: 2807123999
sif: "https://datasets.datalad.org/shub/opensciencegrid/osgvo-el6/latest/2018-11-07-3e83e665-60ffeee7/60ffeee7df556250515e6cae8580ce42.simg"
url: https://datasets.datalad.org/shub/opensciencegrid/osgvo-el6/latest/2018-11-07-3e83e665-60ffeee7/
recipe: https://datasets.datalad.org/shub/opensciencegrid/osgvo-el6/latest/2018-11-07-3e83e665-60ffeee7/Singularity
collection: opensciencegrid/osgvo-el6
---

# opensciencegrid/osgvo-el6:latest

```bash
$ singularity pull shub://opensciencegrid/osgvo-el6:latest
```

## Singularity Recipe

```singularity
bootstrap:docker
From:centos:6

%post

yum -y upgrade
yum -y install epel-release yum-plugin-priorities

# osg repo
yum -y install http://repo.opensciencegrid.org/osg/3.4/osg-3.4-el6-release-latest.rpm

# pegasus repo
echo -e "# Pegasus\n[Pegasus]\nname=Pegasus\nbaseurl=http://download.pegasus.isi.edu/wms/download/rhel/6/\$basearch/\ngpgcheck=0\nenabled=1\npriority=50" >/etc/yum.repos.d/pegasus.repo

# well rounded basic system to support a wide range of user jobs
yum -y grouplist
yum -y groupinstall "Additional Development" \
                    "Compatibility Libraries" \
                    "Console Internet Tools" \
                    "Development Tools" \
                    "Internet Applications" \
                    "Networking Tools" \
                    "Scientific Support"

yum -y install \
    redhat-lsb \
    astropy-tools \
	bc \
	binutils \
	binutils-devel \
	coreutils \
	curl \
	fontconfig \
	gcc \
	gcc-c++ \
	gcc-gfortran \
	git \
	glew-devel \
	glib2-devel \
	glib-devel \
	graphviz \
	gsl-devel \
	java-1.8.0-openjdk \
	java-1.8.0-openjdk-devel \
	libgfortran \
	libGLU \
	libX11-devel \
	libXaw-devel \
	libXext-devel \
	libXft-devel \
	libxml2 \
	libxml2-devel \
	libXmu-devel \
	libXpm \
	libXpm-devel \
	libXt \
	mesa-libGL-devel \
	numpy \
	octave \
	octave-devel \
	osg-wn-client \
	openssl098e \
	p7zip p7zip-plugins \
	python-astropy \
	python-devel \
	R-devel \
	redhat-lsb-core \
	rsync \
	scipy \
    stashcache-client \
	subversion \
	tcl-devel \
	tcsh \
	time \
	tk-devel \
	wget \
	which

# Cuda and cudnn - in case we land on GPU nodes. See:
#  https://developer.nvidia.com/cuda-downloads
#  https://gitlab.com/nvidia/cuda/blob/centos7/9.0/devel/cudnn7/Dockerfile
rpm -Uvh https://developer.download.nvidia.com/compute/cuda/repos/rhel6/x86_64/cuda-repo-rhel6-9.0.176-1.x86_64.rpm \
    && yum -y clean all \
    && yum -y install cuda-9-1 \
    && cd /usr/local \
    && curl -fsSL http://developer.download.nvidia.com/compute/redist/cudnn/v7.0.5/cudnn-9.1-linux-x64-v7.tgz -O \
    && tar --no-same-owner -xzf cudnn-9.1-linux-x64-v7.tgz -C /usr/local \
    && rm -f cudnn-9.1-linux-x64-v7.tgz \
    && ldconfig

# osg
# use CA certs from CVMFS
yum -y install osg-ca-certs osg-wn-client
rm -f /etc/grid-security/certificates/*.r0

# htcondor - include so we can chirp
yum -y install condor

# pegasus
yum -y install pegasus

# Cleaning caches to reduce size of image
yum clean all

# required directories
for MNTPOINT in \
    /cvmfs \
    /hadoop \
    /hdfs \
    /lizard \
    /mnt/hadoop \
    /mnt/hdfs \
    /xenon \
    /spt \
    /stash2 \
; do \
    mkdir -p $MNTPOINT ; \
done

# make sure we have a way to bind host provided libraries
# see https://github.com/singularityware/singularity/issues/611
mkdir -p /host-libs /etc/OpenCL/vendors

# build info
echo "Timestamp:" `date --utc` | tee /image-build-info.txt
```

## Collection

 - Name: [opensciencegrid/osgvo-el6](https://github.com/opensciencegrid/osgvo-el6)
 - License: None

