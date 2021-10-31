---
id: 1646
name: "nealplatt/sH_hybridization"
branch: "master"
tag: "latest"
commit: "83fcebaa5cbc92da7581aaca36ead0358ed4f660"
version: "a16cb090803aab238c9c11d5866f6147"
build_date: "2018-02-06T23:37:02.039Z"
size_mb: 2595
size: 1360052255
sif: "https://datasets.datalad.org/shub/nealplatt/sH_hybridization/latest/2018-02-06-83fcebaa-a16cb090/a16cb090803aab238c9c11d5866f6147.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/nealplatt/sH_hybridization/latest/2018-02-06-83fcebaa-a16cb090/
recipe: https://datasets.datalad.org/shub/nealplatt/sH_hybridization/latest/2018-02-06-83fcebaa-a16cb090/Singularity
collection: nealplatt/sH_hybridization
---

# nealplatt/sH_hybridization:latest

```bash
$ singularity pull shub://nealplatt/sH_hybridization:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04

%labels
AUTHOR Roy "Neal" Platt
MAINTAINER rplatt@txbiomed.org
VERSION 0.1
DATE 5 Feb 2018

%post
    apt-get update
    apt-get clean
    apt-get install -qy \
                wget \
		bzip2 \
                r-base \
                r-base-dev \
                default-jre \
                bwa \
                samtools \
                git \
                zip \
		nano \
		vim \
                dialog

    mkdir /usr/software

    cd /usr/software/
    
    #Install bioconda
    wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
    chmod u+x Miniconda3-latest-Linux-x86_64.sh 
    bash ./Miniconda3-latest-Linux-x86_64.sh -b -p /usr/software/miniconda3
    export PATH="/usr/software/miniconda3/bin:$PATH"
    conda install -y -c bioconda snakemake
    rm Miniconda3-latest-Linux-x86_64.sh
    ln -s /usr/software/miniconda3/bin/* /usr/local/bin/

    #Install GATK
    wget https://github.com/broadinstitute/gatk/releases/download/4.0.1.1/gatk-4.0.1.1.zip
    unzip gatk-4.0.1.1.zip
    rm gatk-4.0.1.1.zip
    ln -s /usr/software/gatk-4.0.1.1/gatk /usr/local/bin/

    wget http://www.usadellab.org/cms/uploads/supplementary/Trimmomatic/Trimmomatic-0.36.zip
    unzip Trimmomatic-0.36.zip
    ln -s /usr/software/Trimmomatic-0.36/trimmomatic-0.36.jar /usr/software/
    rm -r Trimmomatic-0.36.zip Trimmomatic-0.36



#%runscript
#    exec /bin/bash
```

## Collection

 - Name: [nealplatt/sH_hybridization](https://github.com/nealplatt/sH_hybridization)
 - License: None

