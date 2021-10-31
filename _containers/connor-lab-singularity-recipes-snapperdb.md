---
id: 6997
name: "connor-lab/singularity-recipes"
branch: "master"
tag: "snapperdb"
commit: "28db0e500498d5e9487b8ea1d3b6190f7c6afacb"
version: "5c1a44be7e0e6a0d5d7b01d2f4b5406c"
build_date: "2019-06-17T19:35:29.682Z"
size_mb: 939
size: 399999007
sif: "https://datasets.datalad.org/shub/connor-lab/singularity-recipes/snapperdb/2019-06-17-28db0e50-5c1a44be/5c1a44be7e0e6a0d5d7b01d2f4b5406c.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/connor-lab/singularity-recipes/snapperdb/2019-06-17-28db0e50-5c1a44be/
recipe: https://datasets.datalad.org/shub/connor-lab/singularity-recipes/snapperdb/2019-06-17-28db0e50-5c1a44be/Singularity
collection: connor-lab/singularity-recipes
---

# connor-lab/singularity-recipes:snapperdb

```bash
$ singularity pull shub://connor-lab/singularity-recipes:snapperdb
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:latest

%post
    yum install -y epel-release
    yum -y update
    yum install -y git make
    yum install -y bzip2 bzip2-devel gcc-c++ ncurses-devel java-1.8.0-openjdk-headless unzip xz-devel zlib-devel
    yum install -y python-devel python2-pip

 
    pip install cython
    pip install argparse bintrees biopython psycopg2-binary paramiko PyVCF PyYAML hashids joblib

    pip install git+https://github.com/m-bull/PHEnix.git
    pip install git+https://github.com/m-bull/snapperdb.git
   
    # SAMtools
    curl -fsSL 'https://github.com/samtools/samtools/releases/download/1.9/samtools-1.9.tar.bz2' | tar -xj -C /tmp/
    cd /tmp/samtools-1.9 && ./configure && make && make install
    rm -rf /tmp/samtools-1.9

    # BCFtools
    curl -fsSL 'https://github.com/samtools/bcftools/releases/download/1.9/bcftools-1.9.tar.bz2' | tar -xj -C /tmp/
    cd /tmp/bcftools-1.9 && ./configure && make && make install
    rm -rf /tmp/bcftools-1.9

    # Minimap2
    cd /tmp
    git clone https://github.com/lh3/minimap2 /tmp/minimap2
    cd /tmp/minimap2
    make
    mv /tmp/minimap2/minimap2 /usr/local/bin/
    rm -rf /tmp/minimap2

    # BWA
    cd /tmp
    git clone https://github.com/lh3/bwa /tmp/bwa
    cd /tmp/bwa
    make
    mv /tmp/bwa/bwa /usr/local/bin/
    rm -rf /tmp/bwa

    # Picard
    curl -fsSL 'https://github.com/broadinstitute/picard/releases/download/2.18.16/picard.jar' --output /usr/local/bin/picard.jar

    # GATK
    curl -fsSL 'https://software.broadinstitute.org/gatk/download/auth?package=GATK-archive&version=3.8-1-0-gf15c1c3ef' | tar -xj -C /usr/local/bin
    find /usr/local/bin/GenomeAnalysisTK* -name "GenomeAnalysisTK.jar" -exec ln -s {} /usr/local/bin \;

%environment
    export PICARD_JAR=/usr/local/bin/picard.jar
    export GATK_JAR=/usr/local/bin/GenomeAnalysisTK.jar

%labels
    Maintainer m-bull
    Version snapperdb-m-bull-git-latest
```

## Collection

 - Name: [connor-lab/singularity-recipes](https://github.com/connor-lab/singularity-recipes)
 - License: None

