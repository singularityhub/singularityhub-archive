---
id: 7264
name: "Molmed/summary-report-development"
branch: "master"
tag: "latest"
commit: "4cfe87644b22745b268287c2bee084567ebb4c32"
version: "6665b8b1d0fc627c3d067dd7815be450"
build_date: "2019-02-15T14:17:04.238Z"
size_mb: 558
size: 218681375
sif: "https://datasets.datalad.org/shub/Molmed/summary-report-development/latest/2019-02-15-4cfe8764-6665b8b1/6665b8b1d0fc627c3d067dd7815be450.simg"
url: https://datasets.datalad.org/shub/Molmed/summary-report-development/latest/2019-02-15-4cfe8764-6665b8b1/
recipe: https://datasets.datalad.org/shub/Molmed/summary-report-development/latest/2019-02-15-4cfe8764-6665b8b1/Singularity
collection: Molmed/summary-report-development
---

# Molmed/summary-report-development:latest

```bash
$ singularity pull shub://Molmed/summary-report-development:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:ubuntu:latest

%environment
LC_ALL=C.UTF-8
LANG=C.UTF-8

%post
    apt-get -y update
    apt-get -y install wget

    wget https://repo.continuum.io/miniconda/Miniconda3-3.7.0-Linux-x86_64.sh -O ~/miniconda.sh
    bash ~/miniconda.sh -b -p /opt/miniconda
    export PATH="/opt/miniconda/bin:$PATH"

    conda config --add channels defaults
    conda config --add channels bioconda
    conda config --add channels conda-forge
    conda install -c bioconda illumina-interop


%runscript
    exec /opt/miniconda/bin/interop_summary
```

## Collection

 - Name: [Molmed/summary-report-development](https://github.com/Molmed/summary-report-development)
 - License: None

