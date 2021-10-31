---
id: 9987
name: "merckey/Singularity"
branch: "master"
tag: "snakemake"
commit: "0fc0b977c96581c8607ff214e7f5a9656c746182"
version: "02b318f3c2057fd50003c713b06a5cdb"
build_date: "2019-06-23T23:32:47.644Z"
size_mb: 1024
size: 376061983
sif: "https://datasets.datalad.org/shub/merckey/Singularity/snakemake/2019-06-23-0fc0b977-02b318f3/02b318f3c2057fd50003c713b06a5cdb.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/merckey/Singularity/snakemake/2019-06-23-0fc0b977-02b318f3/
recipe: https://datasets.datalad.org/shub/merckey/Singularity/snakemake/2019-06-23-0fc0b977-02b318f3/Singularity
collection: merckey/Singularity
---

# merckey/Singularity:snakemake

```bash
$ singularity pull shub://merckey/Singularity:snakemake
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3


%environment
    export PATH=/opt/conda/bin:$PATH

%post
    /opt/conda/bin/conda install --yes -c bioconda -c conda-forge snakemake==4.4.0
```

## Collection

 - Name: [merckey/Singularity](https://github.com/merckey/Singularity)
 - License: None

