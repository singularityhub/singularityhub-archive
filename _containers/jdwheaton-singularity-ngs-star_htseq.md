---
id: 2863
name: "jdwheaton/singularity-ngs"
branch: "master"
tag: "star_htseq"
commit: "c21ec4a88f680bfd258980617240e4d66e9c47a9"
version: "a8f9502c230f5824bc33ee1a26376d79"
build_date: "2020-06-05T17:22:24.649Z"
size_mb: 662
size: 229560351
sif: "https://datasets.datalad.org/shub/jdwheaton/singularity-ngs/star_htseq/2020-06-05-c21ec4a8-a8f9502c/a8f9502c230f5824bc33ee1a26376d79.simg"
url: https://datasets.datalad.org/shub/jdwheaton/singularity-ngs/star_htseq/2020-06-05-c21ec4a8-a8f9502c/
recipe: https://datasets.datalad.org/shub/jdwheaton/singularity-ngs/star_htseq/2020-06-05-c21ec4a8-a8f9502c/Singularity
collection: jdwheaton/singularity-ngs
---

# jdwheaton/singularity-ngs:star_htseq

```bash
$ singularity pull shub://jdwheaton/singularity-ngs:star_htseq
```

## Singularity Recipe

```singularity
bootstrap: docker
From: centos:7

%post
	yum -y update
	yum -y install wget git gzip bzip2 gcc gcc-c++ make zlib-devel epel-release
	yum -y install python-pip
	cd /
	wget https://github.com/alexdobin/STAR/archive/2.6.0a.tar.gz
	tar -xzf 2.6.0a.tar.gz
	cd STAR-2.6.0a/source
	make
	pip install HTSeq
	
%environment
	export PATH=$PATH:/STAR-2.6.0a/source
```

## Collection

 - Name: [jdwheaton/singularity-ngs](https://github.com/jdwheaton/singularity-ngs)
 - License: None

