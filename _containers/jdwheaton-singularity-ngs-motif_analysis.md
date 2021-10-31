---
id: 3983
name: "jdwheaton/singularity-ngs"
branch: "master"
tag: "motif_analysis"
commit: "3d300637caf1bcf37f5d150c2a02d2f41ebb5769"
version: "63a7ca2b64de95d600adea768f18f16c"
build_date: "2018-08-14T19:41:12.293Z"
size_mb: 1010
size: 359219231
sif: "https://datasets.datalad.org/shub/jdwheaton/singularity-ngs/motif_analysis/2018-08-14-3d300637-63a7ca2b/63a7ca2b64de95d600adea768f18f16c.simg"
url: https://datasets.datalad.org/shub/jdwheaton/singularity-ngs/motif_analysis/2018-08-14-3d300637-63a7ca2b/
recipe: https://datasets.datalad.org/shub/jdwheaton/singularity-ngs/motif_analysis/2018-08-14-3d300637-63a7ca2b/Singularity
collection: jdwheaton/singularity-ngs
---

# jdwheaton/singularity-ngs:motif_analysis

```bash
$ singularity pull shub://jdwheaton/singularity-ngs:motif_analysis
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:7

# This container holds motif analysis tools including MEME-suite, as well as helpers like bedtools2.

%post
	# Install required build tools
    yum -y update
    yum -y install wget gcc gcc-c++ make zlib-devel epel-release
    yum -y install perl-devel openmpi ghostscript openmpi-devel which
    
    # Add mpirun and mpicc to path
    ln -s /usr/lib64/openmpi/bin/mpirun /usr/bin/mpirun
    ln -s /usr/lib64/openmpi/bin/mpicc /usr/bin/mpicc
    
    # Install perl packages
    yum -y install expat-devel perl-XML-Simple perl-File-Which perl-HTML-Template perl-HTML-Tree perl-JSON
   
    # Download bedtools 
    wget https://github.com/arq5x/bedtools2/releases/download/v2.27.1/bedtools-2.27.1.tar.gz
    tar -xvzf bedtools-2.27.1.tar.gz
    cd bedtools2
    make
    
    # Install meme
    cd /
    wget http://meme-suite.org/meme-software/5.0.1/meme_5.0.1_1.tar.gz
    tar -xvzf meme_5.0.1_1.tar.gz
    cd meme-5.0.1/
    ./configure --prefix=/meme --with-url=http://meme-suite.org --enable-build-libxml2 --enable-build-libxsl
    make
    # Skip the test because all meme tests using mpi will fail because of '-p 5' setting, which will terminate the build
#     make test
    make install
   
    
    
%environment
	export PATH=$PATH:/bedtools2/bin
	export PATH=$PATH:/meme/bin
```

## Collection

 - Name: [jdwheaton/singularity-ngs](https://github.com/jdwheaton/singularity-ngs)
 - License: None

