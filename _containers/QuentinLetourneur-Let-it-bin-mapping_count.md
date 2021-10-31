---
id: 4630
name: "QuentinLetourneur/Let-it-bin"
branch: "master"
tag: "mapping_count"
commit: "5a0216219f195463e23b85dc2dbd9e6afe15467a"
version: "449e5d38d6b54d544b124fe49d681845"
build_date: "2018-09-03T17:16:24.256Z"
size_mb: 702
size: 320057375
sif: "https://datasets.datalad.org/shub/QuentinLetourneur/Let-it-bin/mapping_count/2018-09-03-5a021621-449e5d38/449e5d38d6b54d544b124fe49d681845.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/QuentinLetourneur/Let-it-bin/mapping_count/2018-09-03-5a021621-449e5d38/
recipe: https://datasets.datalad.org/shub/QuentinLetourneur/Let-it-bin/mapping_count/2018-09-03-5a021621-449e5d38/Singularity
collection: QuentinLetourneur/Let-it-bin
---

# QuentinLetourneur/Let-it-bin:mapping_count

```bash
$ singularity pull shub://QuentinLetourneur/Let-it-bin:mapping_count
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%setup
    export LC_ALL=C

%post
    mkdir /pasteur
    apt -y update
    apt -y install python python-pip wget zip
    pip install pysam
    
	cd /home
    wget https://github.com/BenLangmead/bowtie2/releases/download/v2.2.9/bowtie2-2.2.9-linux-x86_64.zip
    unzip bowtie2-2.2.9-linux-x86_64.zip
    rm bowtie2-2.2.9-linux-x86_64.zip
    mv bowtie2-2.2.9/* /usr/local/bin/
    
    wget https://gitlab.pasteur.fr/aghozlan/mbma_singularity/repository/master/archive.zip
    unzip archive.zip
    rm archive.zip
    mv mbma_singularity-master-*/* /usr/local/bin
```

## Collection

 - Name: [QuentinLetourneur/Let-it-bin](https://github.com/QuentinLetourneur/Let-it-bin)
 - License: None

