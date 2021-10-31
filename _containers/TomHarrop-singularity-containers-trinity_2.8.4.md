---
id: 5474
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "trinity_2.8.4"
commit: "e857a912ef8a2f687bdbe8f06945a042ee8996eb"
version: "e6429ab90aa77111a57de0354c5383c3"
build_date: "2020-02-23T22:58:11.770Z"
size_mb: 1646
size: 507334687
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/trinity_2.8.4/2020-02-23-e857a912-e6429ab9/e6429ab90aa77111a57de0354c5383c3.simg"
url: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/trinity_2.8.4/2020-02-23-e857a912-e6429ab9/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/trinity_2.8.4/2020-02-23-e857a912-e6429ab9/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:trinity_2.8.4

```bash
$ singularity pull shub://TomHarrop/singularity-containers:trinity_2.8.4
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: combinelab/salmon:0.11.3

%help

    Container for Trinity 2.8.4
    https://github.com/trinityrnaseq/trinityrnaseq/releases

%labels

    VERSION "Trinity 2.8.4"

%post
    
    # dependencies
    apt-get update
    apt-get install -y \
        bowtie2 \
        jellyfish \
        language-pack-en \
        openjdk-8-jre \
        python-numpy \
        rsync \
        samtools \
        wget

        # python-pip \

    # update pip and reinstall numpy
    # /usr/bin/pip install --upgrade pip
    # /usr/local/bin/pip install numpy

    # install RSEM
    mkdir rsem-install
    wget -O "rsem.tar.gz" \
        https://github.com/deweylab/RSEM/archive/v1.3.0.tar.gz
    tar -zxf rsem.tar.gz \
        -C rsem-install \
        --strip-components 1
    cd rsem-install
    make && make install
    cd ..
    rm -rf rsem.tar.gz rsem-install

    # choose java 8
    update-java-alternatives --set java-1.8.0-openjdk-amd64

    # download trinity
    mkdir trinityrnaseq
    wget -O "trinityrnaseq.tar.gz" \
        https://github.com/trinityrnaseq/trinityrnaseq/archive/Trinity-v2.8.4.tar.gz
    tar -zxf trinityrnaseq.tar.gz \
        -C trinityrnaseq \
        --strip-components 1
    cd trinityrnaseq || exit 1
    make && make plugins && make install
    cd .. || exit 1
    rm -rf trinityrnaseq.tar.gz trinityrnaseq

%environment

    export PATH="${PATH}:/usr/local/bin/trinityrnaseq:/usr/local/bin/trinityrnaseq/util:/usr/local/bin/trinityrnaseq/util/support_scripts:/usr/local/bin/trinityrnaseq/util/misc"
    export TRINITY_HOME="/usr/local/bin/trinityrnaseq"

%runscript

    exec /usr/local/bin/trinityrnaseq/Trinity "$@"
```

## Collection

 - Name: [TomHarrop/singularity-containers](https://github.com/TomHarrop/singularity-containers)
 - License: None

