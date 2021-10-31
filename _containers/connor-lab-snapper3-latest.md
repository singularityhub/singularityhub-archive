---
id: 10353
name: "connor-lab/snapper3"
branch: "master"
tag: "latest"
commit: "6ddc483dc69ae59dbee49ee960c8691b02556493"
version: "05864b0f5b9701dbb3bbf72e8497aeaa"
build_date: "2019-07-29T21:48:55.229Z"
size_mb: 1147.0
size: 475938847
sif: "https://datasets.datalad.org/shub/connor-lab/snapper3/latest/2019-07-29-6ddc483d-05864b0f/05864b0f5b9701dbb3bbf72e8497aeaa.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/connor-lab/snapper3/latest/2019-07-29-6ddc483d-05864b0f/
recipe: https://datasets.datalad.org/shub/connor-lab/snapper3/latest/2019-07-29-6ddc483d-05864b0f/Singularity
collection: connor-lab/snapper3
---

# connor-lab/snapper3:latest

```bash
$ singularity pull shub://connor-lab/snapper3:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: postgres:11

%post
    apt-get -y update && apt-get -y upgrade
    apt-get -y install curl git make
    apt-get -y install bzip2 libbz2-dev g++ libncurses5-dev openjdk-8-jdk-headless unzip liblzma-dev zlib1g-dev
    apt-get -y install python-dev python-pip

    pip install cython
    pip install argparse bintrees biopython psycopg2-binary paramiko PyVCF PyYAML hashids joblib

    pip install git+https://github.com/m-bull/PHEnix.git
    
    cd /opt
    git clone https://github.com/connor-lab/snapper3.git
   
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

    # FastTree
    curl -fsSL 'http://www.microbesonline.org/fasttree/FastTreeDbl' --output /usr/local/bin/FastTree
    chmod +x /usr/local/bin/FastTree

%environment
    export PICARD_JAR=/usr/local/bin/picard.jar
    export GATK_JAR=/usr/local/bin/GenomeAnalysisTK.jar
    export PATH=/opt/snapper3/scripts:$PATH
    export PYTHONPATH=/opt/snapper3:/opt/snapper3/scripts:$PYTHONPATH

%labels
    Maintainer m-bull
    Version snapperdb-m-bull-git-latest
```

## Collection

 - Name: [connor-lab/snapper3](https://github.com/connor-lab/snapper3)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

