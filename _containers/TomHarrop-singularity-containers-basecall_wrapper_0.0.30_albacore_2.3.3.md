---
id: 5484
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "basecall_wrapper_0.0.30_albacore_2.3.3"
commit: "f37a45ad19bc4fe97b960e27d6a589f917b78919"
version: "2bdb1bca9dc9f3481946b59e67ca72c0"
build_date: "2018-11-06T09:27:21.090Z"
size_mb: 2405
size: 898101279
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/basecall_wrapper_0.0.30_albacore_2.3.3/2018-11-06-f37a45ad-2bdb1bca/2bdb1bca9dc9f3481946b59e67ca72c0.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/singularity-containers/basecall_wrapper_0.0.30_albacore_2.3.3/2018-11-06-f37a45ad-2bdb1bca/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/basecall_wrapper_0.0.30_albacore_2.3.3/2018-11-06-f37a45ad-2bdb1bca/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:basecall_wrapper_0.0.30_albacore_2.3.3

```bash
$ singularity pull shub://TomHarrop/singularity-containers:basecall_wrapper_0.0.30_albacore_2.3.3
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: rocker/tidyverse:3.5.1

%help

    basecall_wrapper 0.0.30 with Python 3.5.3 and albacore 2.3.3
    
%labels

    MAINTAINER "Tom Harrop (twharrop@gmail.com) "
    VERSION "basecall_wrapper 0.0.30 with albacore 2.3.3"

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
        https://mirror.oxfordnanoportal.com/software/analysis/ont_albacore-2.3.3-cp35-cp35m-manylinux1_x86_64.whl

    # install basecall_wrapper
    /usr/local/bin/pip3 install git+git://github.com/tomharrop/basecall_wrapper.git

    # lanfear QC script
    Rscript -e "install.packages(c( \
        'futile.logger', \
        'optparse', \
        'viridis'))"

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

