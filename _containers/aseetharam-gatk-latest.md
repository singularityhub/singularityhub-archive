---
id: 14059
name: "aseetharam/gatk"
branch: "master"
tag: "latest"
commit: "ce52603c0580d6ee71289bd552a4b704bb8e4b61"
version: "f3fd82023ffd34704886912a2c626796c7b61673527852bcf888b96366f2bc00"
build_date: "2021-04-16T18:55:22.882Z"
size_mb: 1700.859375
size: 1783480320
sif: "https://datasets.datalad.org/shub/aseetharam/gatk/latest/2021-04-16-ce52603c-f3fd8202/f3fd82023ffd34704886912a2c626796c7b61673527852bcf888b96366f2bc00.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/aseetharam/gatk/latest/2021-04-16-ce52603c-f3fd8202/
recipe: https://datasets.datalad.org/shub/aseetharam/gatk/latest/2021-04-16-ce52603c-f3fd8202/Singularity
collection: aseetharam/gatk
---

# aseetharam/gatk:latest

```bash
$ singularity pull shub://aseetharam/gatk:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: broadinstitute/gatk:4.2.0.0

%labels
   MAINTAINER Arun Seetharam
   EMAIL arnstrm@iastate.edu

%runscript
   echo "use the '$GATKHOME' for location of gatk jar file which is '$GATK'"
   echo "use the '$PICARDHOME' for the location of picard.jar file" 
   echo "all tools are in the path (datamash, bioawk, bwa, samtools, vcftools)" 

%environment
    export GATKHOME=/gatk
    export GATK=gatk-package-4.2.0.0-local.jar
    export PICARDHOME=/picard
    export PATH=$PATH:/opt/bwa-mem2-2.0pre2_x64-linux

%post
   curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add
   apt-get update
   apt-get install -y build-essential wget curl git autoconf automake
   apt-get install -y gcc g++ bison make
   apt-get install -y perl zlib1g-dev libbz2-dev liblzma-dev libcurl4-gnutls-dev libssl-dev libncurses5-dev
   # install BWA
   apt-get install -y bwa
   # install datamash   
   apt-get install -y datamash
   # install bedtools
   apt-get install -y bedtools
   # vcftools
   apt-get install -y vcftools
   # install samtools
   apt-get install -y samtools
   # install bioawk
   cd /opt
   git clone https://github.com/lh3/bioawk.git
   cd bioawk
   make
   mv bioawk maketab /usr/bin/
   # picard
   mkdir -p /picard
   cd /picard
   wget https://github.com/broadinstitute/picard/releases/download/2.25.1/picard.jar
   # install BWA-mem2
   mkdir -p /bwa-mem2
   cd /opt
   curl -L https://github.com/bwa-mem2/bwa-mem2/releases/download/v2.0pre2/bwa-mem2-2.0pre2_x64-linux.tar.bz2 | tar jxf -
```

## Collection

 - Name: [aseetharam/gatk](https://github.com/aseetharam/gatk)
 - License: None

