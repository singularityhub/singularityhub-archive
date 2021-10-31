---
id: 2840
name: "jdwheaton/singularity-ngs"
branch: "master"
tag: "latest"
commit: "de66ff51bb6ba8d1fe31c08b581e21166c2901e4"
version: "9f12847c233853defff991c7ab30e39c"
build_date: "2020-02-11T22:43:12.198Z"
size_mb: 784
size: 239636511
sif: "https://datasets.datalad.org/shub/jdwheaton/singularity-ngs/latest/2020-02-11-de66ff51-9f12847c/9f12847c233853defff991c7ab30e39c.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jdwheaton/singularity-ngs/latest/2020-02-11-de66ff51-9f12847c/
recipe: https://datasets.datalad.org/shub/jdwheaton/singularity-ngs/latest/2020-02-11-de66ff51-9f12847c/Singularity
collection: jdwheaton/singularity-ngs
---

# jdwheaton/singularity-ngs:latest

```bash
$ singularity pull shub://jdwheaton/singularity-ngs:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:7

%post
	# Install required build tools
    yum -y update
    yum -y install git autoconf gcc make wget unzip bzip2
    # Install htslib and samtools dependencies
    yum -y install zlib-devel bzip2-devel xz-devel ncurses-devel
    # Clone htslib and samtools from github
    git clone https://github.com/samtools/htslib.git
    git clone https://github.com/samtools/samtools.git
    # Make and install htslib and samtools
    cd htslib
    autoheader
    autoconf
    ./configure
    make
    make install
    cd ../samtools
    autoheader
    autoconf
    ./configure
    make
    make install
    # Download and compile bowtie2
    cd /
    wget https://sourceforge.net/projects/bowtie-bio/files/bowtie2/2.3.4.1/bowtie2-2.3.4.1-linux-x86_64.zip
    unzip bowtie2-2.3.4.1-linux-x86_64.zip
    rm bowtie2-2.3.4.1-linux-x86_64.zip

%environment
	export PATH=$PATH:/bowtie2-2.3.4.1-linux-x86_64

%runscript
    samtools --help
```

## Collection

 - Name: [jdwheaton/singularity-ngs](https://github.com/jdwheaton/singularity-ngs)
 - License: None

