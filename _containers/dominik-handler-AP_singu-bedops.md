---
id: 9801
name: "dominik-handler/AP_singu"
branch: "master"
tag: "bedops"
commit: "73bb63eb0a2ca0196113195cf991f93113b73dfa"
version: "eb0089ab72e55fe8902bd4ee098cda5e"
build_date: "2021-02-26T21:45:25.798Z"
size_mb: 596
size: 200302623
sif: "https://datasets.datalad.org/shub/dominik-handler/AP_singu/bedops/2021-02-26-73bb63eb-eb0089ab/eb0089ab72e55fe8902bd4ee098cda5e.simg"
url: https://datasets.datalad.org/shub/dominik-handler/AP_singu/bedops/2021-02-26-73bb63eb-eb0089ab/
recipe: https://datasets.datalad.org/shub/dominik-handler/AP_singu/bedops/2021-02-26-73bb63eb-eb0089ab/Singularity
collection: dominik-handler/AP_singu
---

# dominik-handler/AP_singu:bedops

```bash
$ singularity pull shub://dominik-handler/AP_singu:bedops
```

## Singularity Recipe

```singularity
#bedtools in singularity

Bootstrap: docker
From: conda/miniconda3

%labels
  maintainer Dominik Handler <Dominik Handler@imba.oeaw.ac.at>
  bedops v2.4.36  

%runscript
    bedtools "$@"

%post
  conda config --add channels defaults
  conda config --add channels conda-forge
  conda config --add channels bioconda

  conda install bedops


    mkdir /groups
    mkdir /scratch
    mkdir /scratch-ii2

%environment

%test
```

## Collection

 - Name: [dominik-handler/AP_singu](https://github.com/dominik-handler/AP_singu)
 - License: None

