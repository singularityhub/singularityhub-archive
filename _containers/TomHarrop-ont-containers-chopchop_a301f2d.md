---
id: 11480
name: "TomHarrop/ont-containers"
branch: "master"
tag: "chopchop_a301f2d"
commit: "641f5cf731f2e70d44b54ab0e2143e58d5bcab63"
version: "0ef558220834da993437c922a6186d0869f008417e81147ce20890ffea974e30"
build_date: "2019-11-04T01:32:52.545Z"
size_mb: 583.1796875
size: 611508224
sif: "https://datasets.datalad.org/shub/TomHarrop/ont-containers/chopchop_a301f2d/2019-11-04-641f5cf7-0ef55822/0ef558220834da993437c922a6186d0869f008417e81147ce20890ffea974e30.sif"
url: https://datasets.datalad.org/shub/TomHarrop/ont-containers/chopchop_a301f2d/2019-11-04-641f5cf7-0ef55822/
recipe: https://datasets.datalad.org/shub/TomHarrop/ont-containers/chopchop_a301f2d/2019-11-04-641f5cf7-0ef55822/Singularity
collection: TomHarrop/ont-containers
---

# TomHarrop/ont-containers:chopchop_a301f2d

```bash
$ singularity pull shub://TomHarrop/ont-containers:chopchop_a301f2d
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: python:2.7.16-buster

%help

    Python 2.7.16 with chopchop a301f2d
    
%labels

    MAINTAINER "Tom Harrop (twharrop@gmail.com)"
    VERSION "chopchop a301f2d"

%runscript

    exec /usr/local/bin/python /chopchop/chopchop.py "$@"

%post
    # python dependencies
    /usr/local/bin/pip install \
        argparse \
        biopython \
        keras \
        mysqlclient \
        np-utils \
        numpy \
        pandas \
        scikit-learn==0.18.0 \
        scipy

    # ucsc's gff3ToGenePred
    wget \
        -O /usr/local/bin/gff3ToGenePred \
    http://hgdownload.cse.ucsc.edu/admin/exe/linux.x86_64/gff3ToGenePred
    chmod 755 /usr/local/bin/gff3ToGenePred

    # chopchop
    git clone \
        https://bitbucket.org/valenlab/chopchop.git
    cd chopchop || exit 1
    git checkout a301f2d

%environment
    export PATH="${PATH}:/chopchop:/chopchop/bowtie:/chopchop/svm_light"
```

## Collection

 - Name: [TomHarrop/ont-containers](https://github.com/TomHarrop/ont-containers)
 - License: None

