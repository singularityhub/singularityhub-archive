---
id: 3825
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "basecall_wrapper_0.0.29"
commit: "fec9257bf938639ba3ab6aabaa5b8a726d9ba9bd"
version: "1f8a4f41307c7014438172e7573b97c9"
build_date: "2018-08-02T08:31:48.450Z"
size_mb: 2422
size: 943632415
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/basecall_wrapper_0.0.29/2018-08-02-fec9257b-1f8a4f41/1f8a4f41307c7014438172e7573b97c9.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/singularity-containers/basecall_wrapper_0.0.29/2018-08-02-fec9257b-1f8a4f41/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/basecall_wrapper_0.0.29/2018-08-02-fec9257b-1f8a4f41/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:basecall_wrapper_0.0.29

```bash
$ singularity pull shub://TomHarrop/singularity-containers:basecall_wrapper_0.0.29
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: rocker/tidyverse:3.5.1

%help

    basecall_wrapper 0.0.29 with Python 3.5.3 and albacore 2.3.1
    
%labels

    MAINTAINER "Tom Harrop (twharrop@gmail.com) "
    VERSION "basecall_wrapper 0.0.29 with albacore 2.3.1"

%runscript

    exec /usr/local/bin/basecall_wrapper "$@"

%post

    # install apt packages
    apt-get update
    apt-get install -y \
        default-jre \
        python3-pip

    # install bbmap
    wget -O "bbmap.tar.gz" \
        "https://sourceforge.net/projects/bbmap/files/BBMap_38.00.tar.gz"
    mkdir bbmap-install
    tar -zxf bbmap.tar.gz \
        -C bbmap-install \
        --strip-components 1
    cp -r bbmap-install/resources/* /
    cp -r bbmap-install/* /usr/local/bin/
    rm -rf bbmap.tar.gz bbmap-install

    # install python bits
    pip3 install --upgrade pip
    /usr/local/bin/pip3 install \
        biopython \
        numpy \
        pathlib2 \
        psutil \
        snakemake

    # install albacore
    /usr/local/bin/pip3 install \
        https://mirror.oxfordnanoportal.com/software/analysis/ont_albacore-2.3.1-cp35-cp35m-manylinux1_x86_64.whl

    # install basecall_wrapper
    /usr/local/bin/pip3 install git+git://github.com/tomharrop/basecall_wrapper.git

    # lanfear QC script
    Rscript -e "install.packages(c( \
        'futile.logger', \
        'optparse'))"

    wget \
        -O /usr/local/bin/MinIONQC.R \
        https://raw.githubusercontent.com/roblanf/minion_qc/master/MinIONQC.R
    chmod 755 /usr/local/bin/MinIONQC.R

    # link R
    ln -s /usr/local/bin/Rscript /usr/bin/Rscript
```

## Collection

 - Name: [TomHarrop/singularity-containers](https://github.com/TomHarrop/singularity-containers)
 - License: None

