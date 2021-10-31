---
id: 1954
name: "ShaluJhanwar/testdir"
branch: "master"
tag: "latest"
commit: "486a0a746fce6b8add4cc9cf2171bd9e8b2968d6"
version: "2d4df28981af79838718df8b61ac1b94"
build_date: "2018-03-06T14:18:18.491Z"
size_mb: 425
size: 155488287
sif: "https://datasets.datalad.org/shub/ShaluJhanwar/testdir/latest/2018-03-06-486a0a74-2d4df289/2d4df28981af79838718df8b61ac1b94.simg"
url: https://datasets.datalad.org/shub/ShaluJhanwar/testdir/latest/2018-03-06-486a0a74-2d4df289/
recipe: https://datasets.datalad.org/shub/ShaluJhanwar/testdir/latest/2018-03-06-486a0a74-2d4df289/Singularity
collection: ShaluJhanwar/testdir
---

# ShaluJhanwar/testdir:latest

```bash
$ singularity pull shub://ShaluJhanwar/testdir:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:7.3.1611

%runscript

   #"I can put here whatever I want to happen by default when the user runs the container"
   cat << EOF
This container includes the following apps:
STAR version 2.5.2b - https://github.com/alexdobin/STAR
HTSeq version 0.6.1p1 - http://www-huber.embl.de/HTSeq/
Pysam version 0.9.0 - https://github.com/pysam-developers/pysam
To execute a binary inside the container do "singularity exec /path/to/container.img binary-name"
EOF

%post

   echo "Here we are installing software and other dependencies for the container!"

   echo "Installing STAR"
   yum -y install make gcc gcc-c++ zlib-devel
   cd /usr/local/src/
   curl -o STAR-2.5.2b.tar.gz  https://codeload.github.com/alexdobin/STAR/tar.gz/2.5.2b
   tar xf STAR-2.5.2b.tar.gz
   cd /usr/local/src/STAR-2.5.2b/source
   make STAR && make STARlong
   cp /usr/local/src/STAR-2.5.2b/source/{STAR,STARlong} /usr/local/bin

   echo "Installing HTSeq and Pysam"
   yum -y install epel-release
   yum -y install make gcc gcc-c++ zlib-devel python-devel python-pip numpy
   pip install HTSeq==0.6.1p1
   pip install Pysam==0.9.0

   yum clean all

%apprun STAR
%apprun htseq-count
```

## Collection

 - Name: [ShaluJhanwar/testdir](https://github.com/ShaluJhanwar/testdir)
 - License: None

