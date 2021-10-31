---
id: 6705
name: "maehler/bcftools-singularity"
branch: "master"
tag: "latest"
commit: "9fbc42bb7116ba2131c84d5efa5b614c4f745731"
version: "bcafba089e026e6a39b443e40181f156"
build_date: "2020-06-26T11:40:56.780Z"
size_mb: 430
size: 163569695
sif: "https://datasets.datalad.org/shub/maehler/bcftools-singularity/latest/2020-06-26-9fbc42bb-bcafba08/bcafba089e026e6a39b443e40181f156.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/maehler/bcftools-singularity/latest/2020-06-26-9fbc42bb-bcafba08/
recipe: https://datasets.datalad.org/shub/maehler/bcftools-singularity/latest/2020-06-26-9fbc42bb-bcafba08/Singularity
collection: maehler/bcftools-singularity
---

# maehler/bcftools-singularity:latest

```bash
$ singularity pull shub://maehler/bcftools-singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:latest

%post
    apt-get update && \
        apt-get install -y \
            build-essential \
            libz-dev \
            libbz2-dev \
            liblzma-dev \
            git
    git clone git://github.com/samtools/htslib.git
    git clone git://github.com/samtools/bcftools.git
    cd bcftools
    git checkout 1.9
    make && make install
```

## Collection

 - Name: [maehler/bcftools-singularity](https://github.com/maehler/bcftools-singularity)
 - License: None

