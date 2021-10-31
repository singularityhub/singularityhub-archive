---
id: 8767
name: "jlboat/BioinfoContainers"
branch: "master"
tag: "bcl2fastq"
commit: "5f15386e1057282311ce1b4a7cae3f747425ed6b"
version: "66d6f1f9c302062c0b2b5d7544d096d1"
build_date: "2020-08-04T07:13:55.512Z"
size_mb: 284
size: 101441567
sif: "https://datasets.datalad.org/shub/jlboat/BioinfoContainers/bcl2fastq/2020-08-04-5f15386e-66d6f1f9/66d6f1f9c302062c0b2b5d7544d096d1.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jlboat/BioinfoContainers/bcl2fastq/2020-08-04-5f15386e-66d6f1f9/
recipe: https://datasets.datalad.org/shub/jlboat/BioinfoContainers/bcl2fastq/2020-08-04-5f15386e-66d6f1f9/Singularity
collection: jlboat/BioinfoContainers
---

# jlboat/BioinfoContainers:bcl2fastq

```bash
$ singularity pull shub://jlboat/BioinfoContainers:bcl2fastq
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: centos:latest

%help
    singularity run bcl2fastq.simg -h

%labels
    Topic Bioinformatics
    Input BCL
    Output FASTQ
    bcl2fastq v2.20.0.422

%post
    yum install -y unzip wget
    wget https://support.illumina.com/content/dam/illumina-support/documents/downloads/software/bcl2fastq/bcl2fastq2-v2-20-0-linux-x86-64.zip -O /opt/bcl2fastq2-v2-20-0-linux-x86-64.zip
    unzip /opt/bcl2fastq2-v2-20-0-linux-x86-64.zip
    ls 
    rpm -i bcl2fastq2-v2.20.0.422-Linux-x86_64.rpm 
    rm /opt/bcl2fastq2-v2-20-0-linux-x86-64.zip
    rm /bcl2fastq2-v2.20.0.422-Linux-x86_64.rpm

%runscript
    exec bcl2fastq "$@"
```

## Collection

 - Name: [jlboat/BioinfoContainers](https://github.com/jlboat/BioinfoContainers)
 - License: [MIT License](https://api.github.com/licenses/mit)

