---
id: 7218
name: "shaheenkdr/IndianASR"
branch: "master"
tag: "paddle"
commit: "9fcc1ad79b04585e2c0fecc93790e179a09e78d2"
version: "cc179dd6d1aac177d6f4fb14da089ad0"
build_date: "2019-02-14T08:45:04.549Z"
size_mb: 4401
size: 2751561759
sif: "https://datasets.datalad.org/shub/shaheenkdr/IndianASR/paddle/2019-02-14-9fcc1ad7-cc179dd6/cc179dd6d1aac177d6f4fb14da089ad0.simg"
url: https://datasets.datalad.org/shub/shaheenkdr/IndianASR/paddle/2019-02-14-9fcc1ad7-cc179dd6/
recipe: https://datasets.datalad.org/shub/shaheenkdr/IndianASR/paddle/2019-02-14-9fcc1ad7-cc179dd6/Singularity
collection: shaheenkdr/IndianASR
---

# shaheenkdr/IndianASR:paddle

```bash
$ singularity pull shub://shaheenkdr/IndianASR:paddle
```

## Singularity Recipe

```singularity
Bootstrap:docker
From: paddlepaddle/deep_speech:latest-gpu


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

