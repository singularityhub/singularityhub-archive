---
id: 4626
name: "QuentinLetourneur/Let-it-bin"
branch: "master"
tag: "filtering"
commit: "5e65c5e2c8bcf0e8d2ec082d85e6241acdae29d0"
version: "7e93a11736f8d2c14ac8c211f8de9d12"
build_date: "2018-09-03T17:16:24.271Z"
size_mb: 262
size: 105709599
sif: "https://datasets.datalad.org/shub/QuentinLetourneur/Let-it-bin/filtering/2018-09-03-5e65c5e2-7e93a117/7e93a11736f8d2c14ac8c211f8de9d12.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/QuentinLetourneur/Let-it-bin/filtering/2018-09-03-5e65c5e2-7e93a117/
recipe: https://datasets.datalad.org/shub/QuentinLetourneur/Let-it-bin/filtering/2018-09-03-5e65c5e2-7e93a117/Singularity
collection: QuentinLetourneur/Let-it-bin
---

# QuentinLetourneur/Let-it-bin:filtering

```bash
$ singularity pull shub://QuentinLetourneur/Let-it-bin:filtering
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
    apt -y install wget zip python
    
	cd /home
    wget https://github.com/BenLangmead/bowtie2/releases/download/v2.2.9/bowtie2-2.2.9-linux-x86_64.zip
    unzip bowtie2-2.2.9-linux-x86_64.zip
    rm bowtie2-2.2.9-linux-x86_64.zip
    mv bowtie2-2.2.9/* /usr/local/bin/
```

## Collection

 - Name: [QuentinLetourneur/Let-it-bin](https://github.com/QuentinLetourneur/Let-it-bin)
 - License: None

