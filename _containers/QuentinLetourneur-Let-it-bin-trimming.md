---
id: 4644
name: "QuentinLetourneur/Let-it-bin"
branch: "master"
tag: "trimming"
commit: "4e03e7640366a8d25b3492994181c4d2e3e7bdf9"
version: "0689e6c02658358fc829096e0acdeab9"
build_date: "2019-12-06T17:28:44.738Z"
size_mb: 560
size: 213307423
sif: "https://datasets.datalad.org/shub/QuentinLetourneur/Let-it-bin/trimming/2019-12-06-4e03e764-0689e6c0/0689e6c02658358fc829096e0acdeab9.simg"
url: https://datasets.datalad.org/shub/QuentinLetourneur/Let-it-bin/trimming/2019-12-06-4e03e764-0689e6c0/
recipe: https://datasets.datalad.org/shub/QuentinLetourneur/Let-it-bin/trimming/2019-12-06-4e03e764-0689e6c0/Singularity
collection: QuentinLetourneur/Let-it-bin
---

# QuentinLetourneur/Let-it-bin:trimming

```bash
$ singularity pull shub://QuentinLetourneur/Let-it-bin:trimming
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%files
	bin/alienTrimmerPF8contaminants.fasta /home/

%post
    mkdir /pasteur
    apt -y update
    apt -y install wget build-essential gcj-jdk
    
	cd /home
    wget ftp://ftp.pasteur.fr/pub/gensoft/projects/AlienTrimmer/AlienTrimmer_0.4.0.tar.gz
    tar -xzf AlienTrimmer_0.4.0.tar.gz
    rm AlienTrimmer_0.4.0.tar.gz
    cd AlienTrimmer_0.4.0/src
	sed "s:-march=native::g" -i Makefile
    make
    mv AlienTrimmer /usr/local/bin/
```

## Collection

 - Name: [QuentinLetourneur/Let-it-bin](https://github.com/QuentinLetourneur/Let-it-bin)
 - License: None

