---
id: 6414
name: "shaheenkdr/IndianASR"
branch: "master"
tag: "indianasr"
commit: "849e67af8e8144158e4fa747eb5c370dc73432a3"
version: "39517d33eb6cc2dff79fc09dc9b2424f"
build_date: "2019-02-11T14:03:43.501Z"
size_mb: 9335
size: 4788760607
sif: "https://datasets.datalad.org/shub/shaheenkdr/IndianASR/indianasr/2019-02-11-849e67af-39517d33/39517d33eb6cc2dff79fc09dc9b2424f.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/shaheenkdr/IndianASR/indianasr/2019-02-11-849e67af-39517d33/
recipe: https://datasets.datalad.org/shub/shaheenkdr/IndianASR/indianasr/2019-02-11-849e67af-39517d33/Singularity
collection: shaheenkdr/IndianASR
---

# shaheenkdr/IndianASR:indianasr

```bash
$ singularity pull shub://shaheenkdr/IndianASR:indianasr
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: marcc-hpc/pytorch:0.4.1

%labels
        MAINTAINER shaheenkdr

%environment
        export LANGUAGE=en_US.UTF-8
        export LANG=en_US.UTF-8
        export LC_ALL=en_US.UTF-8

%post
        apt-get update && apt-get install -y --no-install-recommends apt-utils
        apt-get install -y cmake \
                           locales \
                           language-pack-en \
                           git \
			   wget \
                           g++ \
                           zlib1g-dev \
                           automake \
                           autoconf \
                           patch \
                           unzip \
                           sox \
                           libtool \
                           subversion \
                           python2.7 \
                           python3 \
			   bzip2 \
			   libatlas3-base \
			   nano \
			   zlibc \
			   zlib1g \
			   libeigen3-dev \
			   liblzma-dev \
			   libboost-all-dev
	
	echo "all done"
```

## Collection

 - Name: [shaheenkdr/IndianASR](https://github.com/shaheenkdr/IndianASR)
 - License: None

