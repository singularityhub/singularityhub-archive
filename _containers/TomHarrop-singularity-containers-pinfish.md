---
id: 9946
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "pinfish"
commit: "79d9773551e1450936f4b48513ad4759ff4b21b1"
version: "88b3fb89dbb4ae5907037545a54226a0"
build_date: "2019-06-21T06:30:04.007Z"
size_mb: 1425
size: 724877343
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/pinfish/2019-06-21-79d97735-88b3fb89/88b3fb89dbb4ae5907037545a54226a0.simg"
url: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/pinfish/2019-06-21-79d97735-88b3fb89/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/pinfish/2019-06-21-79d97735-88b3fb89/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:pinfish

```bash
$ singularity pull shub://TomHarrop/singularity-containers:pinfish
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: TomHarrop/singularity-containers:racon_1.3.2

%help
    ONT Pinfish pipeline dependencies
    https://github.com/nanoporetech/pipeline-pinfish-analysis

%post
    # dependencies
    apt update
    apt install -y \
        cufflinks \
        git \
        python3 \
        python3-pip \
        samtools \
        zlib1g-dev

    # install conda
    wget -O install_miniconda.sh \
        --no-check-certificate \
        https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
    chmod 755 install_miniconda.sh
    ./install_miniconda.sh \
        -b \
        -p /miniconda
    export PATH="${PATH}:/miniconda/bin"
    rm -f install_miniconda.sh

    # install minimap2
    wget -O "minimap2.tar.gz" \
        --no-check-certificate \
        https://github.com/lh3/minimap2/archive/v2.11.tar.gz
    mkdir minimap2
    tar -zxf minimap2.tar.gz \
        -C minimap2 \
        --strip-components 1

    cd minimap2 || exit 1
    make
    mv minimap2 /usr/local/bin/

    cd .. || exit 1
    rm -rf minimap2 minimap2.tar.gz

    # install snakemake
    /usr/bin/pip3 install --upgrade pip
    /usr/local/bin/pip3 install snakemake

    # install pinfish
    git clone \
        --recursive \
        https://github.com/nanoporetech/pipeline-pinfish-analysis.git

%environment
    export PATH="${PATH}:/miniconda/bin"
    export PATH="${PATH}:/pipeline-pinfish-analysis/pinfish/cluster_gff"
    export PATH="${PATH}:/pipeline-pinfish-analysis/pinfish/collapse_partials"
    export PATH="${PATH}:/pipeline-pinfish-analysis/pinfish/polish_clusters"
    export PATH="${PATH}:/pipeline-pinfish-analysis/pinfish/spliced_bam2gff"
```

## Collection

 - Name: [TomHarrop/singularity-containers](https://github.com/TomHarrop/singularity-containers)
 - License: None

