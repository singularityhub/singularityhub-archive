---
id: 11322
name: "peterk87/nf-biohansel-snippy-comparison"
branch: "master"
tag: "latest"
commit: "d063929c5631c5f55cf2cf83ee5775d3b02f52ec"
version: "ec3f1588ecce2e423d0f80441e326139"
build_date: "2019-10-21T15:46:11.674Z"
size_mb: 3068.0
size: 1035694111
sif: "https://datasets.datalad.org/shub/peterk87/nf-biohansel-snippy-comparison/latest/2019-10-21-d063929c-ec3f1588/ec3f1588ecce2e423d0f80441e326139.sif"
url: https://datasets.datalad.org/shub/peterk87/nf-biohansel-snippy-comparison/latest/2019-10-21-d063929c-ec3f1588/
recipe: https://datasets.datalad.org/shub/peterk87/nf-biohansel-snippy-comparison/latest/2019-10-21-d063929c-ec3f1588/Singularity
collection: peterk87/nf-biohansel-snippy-comparison
---

# peterk87/nf-biohansel-snippy-comparison:latest

```bash
$ singularity pull shub://peterk87/nf-biohansel-snippy-comparison:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:continuumio/miniconda3:4.6.14

%labels
    MAINTAINER Peter Kruczkiewicz
    DESCRIPTION Singularity image containing all requirements for the peterk87/nf-biohansel-snippy-comparison pipeline
    VERSION 1.0.0

%environment
    #export LC_ALL=C
    export PATH=/opt/conda/envs/nf-biohansel-snippy-comparison-1.0.0/bin:$PATH

%files
    environment.yml /

%post
    export PATH=/opt/conda/bin:$PATH
    conda info
    apt-get update --fix-missing && apt-get install -y procps curl locales && apt-get clean -y
    sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
        echo 'LANG="en_US.UTF-8"'>/etc/default/locale && \
        dpkg-reconfigure --frontend=noninteractive locales && \
        update-locale LANG=en_US.UTF-8
    locale
    conda install conda=4.7.12
    conda env create -f /environment.yml
    conda clean -a
```

## Collection

 - Name: [peterk87/nf-biohansel-snippy-comparison](https://github.com/peterk87/nf-biohansel-snippy-comparison)
 - License: None

