---
id: 392
name: "opensciencegrid/osgvo-el7"
branch: "master"
tag: "latest"
commit: "02b2c3b17116ccd64c6c6d384d24ea66aaac009f"
version: "826330b0e5b812100324c2c8042aecad"
build_date: "2019-01-23T18:33:52.124Z"
size_mb: 1801
size: 669466655
sif: "https://datasets.datalad.org/shub/opensciencegrid/osgvo-el7/latest/2019-01-23-02b2c3b1-826330b0/826330b0e5b812100324c2c8042aecad.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/opensciencegrid/osgvo-el7/latest/2019-01-23-02b2c3b1-826330b0/
recipe: https://datasets.datalad.org/shub/opensciencegrid/osgvo-el7/latest/2019-01-23-02b2c3b1-826330b0/Singularity
collection: opensciencegrid/osgvo-el7
---

# opensciencegrid/osgvo-el7:latest

```bash
$ singularity pull shub://opensciencegrid/osgvo-el7:latest
```

## Singularity Recipe

```singularity
bootstrap:docker
From:centos:7

%post

yum -y upgrade
yum -y install epel-release yum-plugin-priorities

# osg repo
yum -y install http://repo.opensciencegrid.org/osg/3.4/osg-3.4-el7-release-latest.rpm

# pegasus repo
echo -e "# Pegasus\n[Pegasus]\nname=Pegasus\nbaseurl=http://download.pegasus.isi.edu/wms/download/rhel/7/\$basearch/\ngpgcheck=0\nenabled=1\npriority=50" >/etc/yum.repos.d/pegasus.repo

# well rounded basic system to support a wide range of user jobs
yum -y groups mark convert
yum -y grouplist
yum -y groupinstall "Compatibility Libraries" \
                    "Development Tools" \
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
	libgomp \
	libicu \
	libquadmath \
	libtool \
	libtool-ltdl \
	libtool-ltdl-devel \
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
	openssh \
	openssh-server \
	openssl098e \
	osg-wn-client \
	p7zip \
	p7zip-plugins \
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

# osg
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

 - Name: [opensciencegrid/osgvo-el7](https://github.com/opensciencegrid/osgvo-el7)
 - License: None

