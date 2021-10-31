---
id: 9428
name: "bsiranosian/bens_1337_workflows"
branch: "master"
tag: "snippy"
commit: "c882e6fbd9df8d0a1cab243d6c00960b24fc12a4"
version: "77512c05d6cf7f9242e6649a270d4aeb"
build_date: "2020-03-25T19:41:44.928Z"
size_mb: 4520
size: 2086789151
sif: "https://datasets.datalad.org/shub/bsiranosian/bens_1337_workflows/snippy/2020-03-25-c882e6fb-77512c05/77512c05d6cf7f9242e6649a270d4aeb.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bsiranosian/bens_1337_workflows/snippy/2020-03-25-c882e6fb-77512c05/
recipe: https://datasets.datalad.org/shub/bsiranosian/bens_1337_workflows/snippy/2020-03-25-c882e6fb-77512c05/Singularity
collection: bsiranosian/bens_1337_workflows
---

# bsiranosian/bens_1337_workflows:snippy

```bash
$ singularity pull shub://bsiranosian/bens_1337_workflows:snippy
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04


# this command assumes at least singularity 2.3
%environment
    PATH="/usr/local/anaconda/bin:$PATH"

%post 
    apt-get update
    apt-get install -y locales wget build-essential
    # localle update necessary for quast
    locale-gen --purge "en_US.UTF-8"
    update-locale LANG="en_US.UTF-8"

    # install anaconda
    if [ ! -d /usr/local/anaconda ]; then
         wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
            -O ~/anaconda.sh && \
         bash ~/anaconda.sh -b -p /usr/local/anaconda && \
         rm ~/anaconda.sh
    fi
        export PATH="/usr/local/anaconda/bin:$PATH"

    conda install -y -c bioconda -c conda-forge python=2.7 snippy vt vcftools bcftools \
    samtools blast bwa pandas snpeff r-ggplot2 r-rafalib

%runscript
   exec /bin/bash
```

## Collection

 - Name: [bsiranosian/bens_1337_workflows](https://github.com/bsiranosian/bens_1337_workflows)
 - License: None

