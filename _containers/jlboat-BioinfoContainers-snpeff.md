---
id: 8781
name: "jlboat/BioinfoContainers"
branch: "master"
tag: "snpeff"
commit: "3cfec3b1a9b5e851e46175990878fda7ab571cfd"
version: "196c81451e575d280df908ae80077090"
build_date: "2020-02-27T08:59:09.143Z"
size_mb: 768
size: 348659743
sif: "https://datasets.datalad.org/shub/jlboat/BioinfoContainers/snpeff/2020-02-27-3cfec3b1-196c8145/196c81451e575d280df908ae80077090.simg"
url: https://datasets.datalad.org/shub/jlboat/BioinfoContainers/snpeff/2020-02-27-3cfec3b1-196c8145/
recipe: https://datasets.datalad.org/shub/jlboat/BioinfoContainers/snpeff/2020-02-27-3cfec3b1-196c8145/Singularity
collection: jlboat/BioinfoContainers
---

# jlboat/BioinfoContainers:snpeff

```bash
$ singularity pull shub://jlboat/BioinfoContainers:snpeff
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: debian:latest

%labels
    Topic Bioinformatics
    snpeff conda-latest

%help
    singularity run --app snpEff snpeff.simg 
    singularity run --app snpSift snpeff.simg 

%post
    apt-get update --fix-missing && apt-get install -y openjdk-8-jre wget unzip
    wget http://sourceforge.net/projects/snpeff/files/snpEff_latest_core.zip
    unzip snpEff_latest_core.zip
    
%apprun snpEff
    exec java -jar /snpEff/snpEff.jar "$@"

%apphelp snpEff
    singularity run --app snpEff snpeff.simg

%apprun snpSift
    exec java -jar /snpEff/SnpSift.jar "$@"

%apphelp snpSift
    singularity run --app snpSift snpeff.simg
```

## Collection

 - Name: [jlboat/BioinfoContainers](https://github.com/jlboat/BioinfoContainers)
 - License: [MIT License](https://api.github.com/licenses/mit)

