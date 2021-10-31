---
id: 4639
name: "QuentinLetourneur/Let-it-bin"
branch: "master"
tag: "metagen"
commit: "2555085d0243d0c6d982f056c8c37eefd6c392f3"
version: "cb1c8be6d198e4a3f4c87f3044c6d04c"
build_date: "2018-09-03T17:16:24.234Z"
size_mb: 692
size: 294723615
sif: "https://datasets.datalad.org/shub/QuentinLetourneur/Let-it-bin/metagen/2018-09-03-2555085d-cb1c8be6/cb1c8be6d198e4a3f4c87f3044c6d04c.simg"
url: https://datasets.datalad.org/shub/QuentinLetourneur/Let-it-bin/metagen/2018-09-03-2555085d-cb1c8be6/
recipe: https://datasets.datalad.org/shub/QuentinLetourneur/Let-it-bin/metagen/2018-09-03-2555085d-cb1c8be6/Singularity
collection: QuentinLetourneur/Let-it-bin
---

# QuentinLetourneur/Let-it-bin:metagen

```bash
$ singularity pull shub://QuentinLetourneur/Let-it-bin:metagen
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%setup
	export LC_ALL=C
	
%files
	bin/cluster_to_fasta.py /usr/local/bin
	bin/fasta.py /usr/local/bin

%post
    mkdir /pasteur
    apt -y update
    apt -y install wget build-essential python2.7
    
	cd /home
	wget https://cran.r-project.org/bin/linux/ubuntu/xenial/r-base-core_3.2.5-1xenial_amd64.deb
    apt -y install ./r-base-core_3.2.5-1xenial_amd64.deb
    
    R --vanilla -e """packages = c('Rcpp', 'MASS', 'mixtools', 'doParallel', 'foreach', 'seqinr', 'getopt')
    install.packages(packages, dependencies=T, repo='http://cran.univ-paris1.fr/')"""
    
    wget https://github.com/BioAlgs/MetaGen/archive/master.zip
    unzip master.zip
    rm master.zip
```

## Collection

 - Name: [QuentinLetourneur/Let-it-bin](https://github.com/QuentinLetourneur/Let-it-bin)
 - License: None

