---
id: 3747
name: "dnousome/JWCI_ComputationalBio-"
branch: "master"
tag: "latest"
commit: "f801e44f63b290260a0ae15ccdfb9b950384c5b3"
version: "7647052de66eacdaefa6bad95e01c556"
build_date: "2018-07-28T02:46:42.406Z"
size_mb: 867
size: 523952159
sif: "https://datasets.datalad.org/shub/dnousome/JWCI_ComputationalBio-/latest/2018-07-28-f801e44f-7647052d/7647052de66eacdaefa6bad95e01c556.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/dnousome/JWCI_ComputationalBio-/latest/2018-07-28-f801e44f-7647052d/
recipe: https://datasets.datalad.org/shub/dnousome/JWCI_ComputationalBio-/latest/2018-07-28-f801e44f-7647052d/Singularity
collection: dnousome/JWCI_ComputationalBio-
---

# dnousome/JWCI_ComputationalBio-:latest

```bash
$ singularity pull shub://dnousome/JWCI_ComputationalBio-:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:latest

%environment
	PATH=/usr/loca/bin:$PATH

%post
	apt-get -y update
	apt-get -y install wget git autoconf build-essential libbz2-dev liblzma-dev zlib1g-dev libncurses5-dev  #python bwa fastqc 


####Add STAR
git clone https://github.com/alexdobin/STAR/ STAR
cp STAR/bin/Linux_x86_64_static/STAR /usr/local/bin

####Add samtools/htslib/bcftools
git clone https://github.com/samtools/htslib htslib
cd htslib
autoheader
autoconf
./configure
make
make install
cd ~

git clone https://github.com/samtools/samtools samtools
cd samtools
autoheader
autoconf -Wno-syntax
./configure
make
make install
cd ~

git clone https://github.com/samtools/bcftools bcftools
cd bcftools
autoheader
autoconf
./configure
make
make install
cd ~

export LD_LIBRARY_PATH=/usr/local/lib 

%labels
Maintainer Darryl Nousome dnousome@gmail.com
```

## Collection

 - Name: [dnousome/JWCI_ComputationalBio-](https://github.com/dnousome/JWCI_ComputationalBio-)
 - License: None

