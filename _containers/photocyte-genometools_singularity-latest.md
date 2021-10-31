---
id: 13203
name: "photocyte/genometools_singularity"
branch: "master"
tag: "latest"
commit: "f1c861bb3addf5b4cecd8201612553cb75b17b2a"
version: "041eddc7038614773d666ed91b882f6a"
build_date: "2020-06-03T17:53:24.615Z"
size_mb: 198.0
size: 77926431
sif: "https://datasets.datalad.org/shub/photocyte/genometools_singularity/latest/2020-06-03-f1c861bb-041eddc7/041eddc7038614773d666ed91b882f6a.sif"
url: https://datasets.datalad.org/shub/photocyte/genometools_singularity/latest/2020-06-03-f1c861bb-041eddc7/
recipe: https://datasets.datalad.org/shub/photocyte/genometools_singularity/latest/2020-06-03-f1c861bb-041eddc7/Singularity
collection: photocyte/genometools_singularity
---

# photocyte/genometools_singularity:latest

```bash
$ singularity pull shub://photocyte/genometools_singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:20.04

%labels
MAINTAINER TRF

%files

%environment
    
%post
    apt-get update
    apt-get install locales
    locale-gen "en_US.UTF-8"
    dpkg-reconfigure locales
    apt-get install -y genometools libgenometools0 libgenometools0-dev
    
%runscript
```

## Collection

 - Name: [photocyte/genometools_singularity](https://github.com/photocyte/genometools_singularity)
 - License: None

