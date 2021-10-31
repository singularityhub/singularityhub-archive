---
id: 11745
name: "marchoeppner/metagenomic-profiling"
branch: "devel"
tag: "latest"
commit: "d4cb45600130356edd46d21439a801401fd9f589"
version: "9ccdb3dcc88f43cd2826bbeecd2942408ca802242b2ffb0d4130dbee12af4b11"
build_date: "2019-12-03T14:01:58.574Z"
size_mb: 899.58203125
size: 943280128
sif: "https://datasets.datalad.org/shub/marchoeppner/metagenomic-profiling/latest/2019-12-03-d4cb4560-9ccdb3dc/9ccdb3dcc88f43cd2826bbeecd2942408ca802242b2ffb0d4130dbee12af4b11.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/marchoeppner/metagenomic-profiling/latest/2019-12-03-d4cb4560-9ccdb3dc/
recipe: https://datasets.datalad.org/shub/marchoeppner/metagenomic-profiling/latest/2019-12-03-d4cb4560-9ccdb3dc/Singularity
collection: marchoeppner/metagenomic-profiling
---

# marchoeppner/metagenomic-profiling:latest

```bash
$ singularity pull shub://marchoeppner/metagenomic-profiling:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:nfcore/base

%labels
    MAINTAINER Marc Hoeppner <m.hoeppner@ikmb.uni-kiel.de>
    DESCRIPTION Singularity image containing all requirements for the metagenomics-profile pipeline
    VERSION 1.0

%environment
    PATH=/opt/conda/envs/metagenomics-profiling-1.1/bin:$PATH
    export PATH

%files
    environment.yml /
%post

    /opt/conda/bin/conda env create -f /environment.yml
    /opt/conda/bin/conda clean -a
    mkdir -p /ifs
    apt-get -y install procps unzip
    mkdir -p /opt/trimmomatic && cd /opt/trimmomatic && wget http://www.usadellab.org/cms/uploads/supplementary/Trimmomatic/Trimmomatic-0.36.zip \
        && unzip Trimmomatic-0.36.zip && mv Trimmomatic-0.36 0.36 && rm Trimmomatic-0.36.zip

    cd /opt
    wget https://www.dropbox.com/sh/m4na8wefp53j8ej/AACU1-Nc0q2dUNRmc9pesUi4a/bin/bcftools
```

## Collection

 - Name: [marchoeppner/metagenomic-profiling](https://github.com/marchoeppner/metagenomic-profiling)
 - License: None

