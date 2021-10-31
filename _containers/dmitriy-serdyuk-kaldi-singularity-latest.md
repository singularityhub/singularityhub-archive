---
id: 10174
name: "dmitriy-serdyuk/kaldi-singularity"
branch: "master"
tag: "latest"
commit: "1273a47d2421e731109bb6a62fc89ee60a651703"
version: "b25b4a5b8b8d5127d5af4c2e54463f3ad9c102ee179a9edc5c9cecca1dc3eb27"
build_date: "2019-09-18T18:50:22.781Z"
size_mb: 3671.58984375
size: 3849940992
sif: "https://datasets.datalad.org/shub/dmitriy-serdyuk/kaldi-singularity/latest/2019-09-18-1273a47d-b25b4a5b/b25b4a5b8b8d5127d5af4c2e54463f3ad9c102ee179a9edc5c9cecca1dc3eb27.sif"
url: https://datasets.datalad.org/shub/dmitriy-serdyuk/kaldi-singularity/latest/2019-09-18-1273a47d-b25b4a5b/
recipe: https://datasets.datalad.org/shub/dmitriy-serdyuk/kaldi-singularity/latest/2019-09-18-1273a47d-b25b4a5b/Singularity
collection: dmitriy-serdyuk/kaldi-singularity
---

# dmitriy-serdyuk/kaldi-singularity:latest

```bash
$ singularity pull shub://dmitriy-serdyuk/kaldi-singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: pytorch/pytorch:1.0.1-cuda10.0-cudnn7-runtime

%post
        echo "Installing Tools with apt-get "
        apt-get update
        apt-get install -y --no-install-recommends g++ make automake autoconf bzip2 unzip wget sox libtool git subversion python2.7 python3 zlib1g-dev ca-certificates patch ffmpeg vim 
        cd /
        git clone https://github.com/kaldi-asr/kaldi.git
        cd kaldi/tools
        ./extras/install_mkl.sh
        make
        cd /kaldi/src
        ./configure --shared --use-cuda=no
        make depend
        make

%environment
        SHELL=/bin/bash
        export SHELL
```

## Collection

 - Name: [dmitriy-serdyuk/kaldi-singularity](https://github.com/dmitriy-serdyuk/kaldi-singularity)
 - License: None

