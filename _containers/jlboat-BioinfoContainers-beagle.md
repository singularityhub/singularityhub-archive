---
id: 8918
name: "jlboat/BioinfoContainers"
branch: "master"
tag: "beagle"
commit: "01fd237ed1c7688e532770e499b506f0d189a7b5"
version: "348867ee6bf90928378485d4b4e9da6a"
build_date: "2019-05-09T08:14:51.136Z"
size_mb: 528
size: 195604511
sif: "https://datasets.datalad.org/shub/jlboat/BioinfoContainers/beagle/2019-05-09-01fd237e-348867ee/348867ee6bf90928378485d4b4e9da6a.simg"
url: https://datasets.datalad.org/shub/jlboat/BioinfoContainers/beagle/2019-05-09-01fd237e-348867ee/
recipe: https://datasets.datalad.org/shub/jlboat/BioinfoContainers/beagle/2019-05-09-01fd237e-348867ee/Singularity
collection: jlboat/BioinfoContainers
---

# jlboat/BioinfoContainers:beagle

```bash
$ singularity pull shub://jlboat/BioinfoContainers:beagle
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: debian:latest

%help
    # Run as below for beagle help
    singularity run beagle.simg 

%labels
    Topic Bioinformatics
    Input BCL
    Output FASTQ
    beagle 5.0

%post
    apt-get update --fix-missing && apt-get install -y wget openjdk-8-jre && rm -rf /var/lib/apt/lists/*
    cd /opt
    wget https://faculty.washington.edu/browning/beagle/beagle.28Sep18.793.jar
    apt-get remove -y wget
    apt autoremove -y
    chmod 777 /opt

%runscript
    exec java -jar /opt/beagle.28Sep18.793.jar "$@"
```

## Collection

 - Name: [jlboat/BioinfoContainers](https://github.com/jlboat/BioinfoContainers)
 - License: [MIT License](https://api.github.com/licenses/mit)

