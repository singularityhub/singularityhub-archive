---
id: 4700
name: "MarissaLL/singularity-containers"
branch: "master"
tag: "vcftools_0.1.17"
commit: "6179055e98266f01ed062044637b2d9e339c94bb"
version: "230db32b3097775cd51432092f9cbcb1"
build_date: "2019-10-07T21:49:47.126Z"
size_mb: 401
size: 180346911
sif: "https://datasets.datalad.org/shub/MarissaLL/singularity-containers/vcftools_0.1.17/2019-10-07-6179055e-230db32b/230db32b3097775cd51432092f9cbcb1.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/MarissaLL/singularity-containers/vcftools_0.1.17/2019-10-07-6179055e-230db32b/
recipe: https://datasets.datalad.org/shub/MarissaLL/singularity-containers/vcftools_0.1.17/2019-10-07-6179055e-230db32b/Singularity
collection: MarissaLL/singularity-containers
---

# MarissaLL/singularity-containers:vcftools_0.1.17

```bash
$ singularity pull shub://MarissaLL/singularity-containers:vcftools_0.1.17
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
OSVersion: bionic
MirrorURL: http://archive.ubuntu.com/ubuntu/
Include: build-essential language-pack-en wget autoconf automake pkg-config zlib1g-dev


%labels

        MAINTAINER "Marissa Le Lec"
        VERSION "VCFtools 0.1.17"

%post
        
        wget https://github.com/vcftools/vcftools/tarball/master --no-check-certificate
        tar -xvf master
        cd vcftools-vcftools-d0c95c5/ || exit 1
        ./autogen.sh
        ./configure
        make
        make install
        cd .. || exit 1
        rm -r vcftools-vcftools-d0c95c5/

%runscript

        exec /usr/local/bin/vcftools "$@"
```

## Collection

 - Name: [MarissaLL/singularity-containers](https://github.com/MarissaLL/singularity-containers)
 - License: None

