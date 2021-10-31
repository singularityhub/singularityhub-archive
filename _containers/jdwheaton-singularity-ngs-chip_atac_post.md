---
id: 3452
name: "jdwheaton/singularity-ngs"
branch: "master"
tag: "chip_atac_post"
commit: "5f09f35d6cebc74de81a36aa6856a9a286d3a3bc"
version: "47a7b9fadad824f0ee00535f23a753db"
build_date: "2020-02-11T22:43:57.670Z"
size_mb: 6668
size: 2114383903
sif: "https://datasets.datalad.org/shub/jdwheaton/singularity-ngs/chip_atac_post/2020-02-11-5f09f35d-47a7b9fa/47a7b9fadad824f0ee00535f23a753db.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jdwheaton/singularity-ngs/chip_atac_post/2020-02-11-5f09f35d-47a7b9fa/
recipe: https://datasets.datalad.org/shub/jdwheaton/singularity-ngs/chip_atac_post/2020-02-11-5f09f35d-47a7b9fa/Singularity
collection: jdwheaton/singularity-ngs
---

# jdwheaton/singularity-ngs:chip_atac_post

```bash
$ singularity pull shub://jdwheaton/singularity-ngs:chip_atac_post
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:7

# This container holds Picard tools, bedtools2, IGVTools, deeptools, MACS2, homer, and subread necessary for post-processing
# and visualization of ATAC-seq and ChIP-seq data.

%post
	# Install required build tools
    yum -y update
    yum -y install wget gcc-c++ make zlib-devel unzip which zip epel-release
    yum -y install curl-devel python-devel python-pip perl
    # We need java for Picard
    yum -y install java-1.8.0-openjdk-devel
    # Install the Picard 2.18.9 jar in root
    wget https://github.com/broadinstitute/picard/releases/download/2.18.9/picard.jar
    # Download bedtools 
    wget https://github.com/arq5x/bedtools2/releases/download/v2.27.1/bedtools-2.27.1.tar.gz
    tar -xvzf bedtools-2.27.1.tar.gz
    cd bedtools2
    make
    # Install IGVtools
    cd /
    wget http://data.broadinstitute.org/igv/projects/downloads/2.3/igvtools_2.3.98.zip
    unzip igvtools_2.3.98.zip
    # Install deeptools
    pip install deeptools
    # Install MACS2
    pip install macs2
    # Install subread
    cd /
    wget https://sourceforge.net/projects/subread/files/subread-1.6.2/subread-1.6.2-Linux-x86_64.tar.gz
    tar -xvzf subread-1.6.2-Linux-x86_64.tar.gz
    # Install homer
    mkdir /homer
    cd /homer
    wget http://homer.ucsd.edu/homer/configureHomer.pl
    perl configureHomer.pl -install
    perl /homer/.//configureHomer.pl -install mm10
    
    
%environment
	export PATH=$PATH:/bedtools2/bin
	export PATH=$PATH:/IGVTools
    export PATH=$PATH:/subread-1.6.2-Linux-x86_64/bin
    export PATH=$PATH:/homer/bin
```

## Collection

 - Name: [jdwheaton/singularity-ngs](https://github.com/jdwheaton/singularity-ngs)
 - License: None

