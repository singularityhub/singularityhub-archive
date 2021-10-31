---
id: 9327
name: "ohsu-cedar-comp-hub/Bulk-RNA-seq-pipeline-SE"
branch: "master"
tag: "fastqc"
commit: "6cf58e9d84080805a3beaf08bca0e547abe6152c"
version: "f7e584bb654ccc8cba662e38472cbcdb"
build_date: "2019-05-28T19:47:16.736Z"
size_mb: 1226
size: 496459807
sif: "https://datasets.datalad.org/shub/ohsu-cedar-comp-hub/Bulk-RNA-seq-pipeline-SE/fastqc/2019-05-28-6cf58e9d-f7e584bb/f7e584bb654ccc8cba662e38472cbcdb.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ohsu-cedar-comp-hub/Bulk-RNA-seq-pipeline-SE/fastqc/2019-05-28-6cf58e9d-f7e584bb/
recipe: https://datasets.datalad.org/shub/ohsu-cedar-comp-hub/Bulk-RNA-seq-pipeline-SE/fastqc/2019-05-28-6cf58e9d-f7e584bb/Singularity
collection: ohsu-cedar-comp-hub/Bulk-RNA-seq-pipeline-SE
---

# ohsu-cedar-comp-hub/Bulk-RNA-seq-pipeline-SE:fastqc

```bash
$ singularity pull shub://ohsu-cedar-comp-hub/Bulk-RNA-seq-pipeline-SE:fastqc
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: continuumio/miniconda3

%files
    fastqc.yaml

%environment
    PATH=/opt/conda/envs/$(head -1 fastqc.yaml | cut -d' ' -f2)/bin:$PATH

%post
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc
    echo "source activate $(head -1 fastqc.yaml | cut -d' ' -f2)" > ~/.bashrc
    /opt/conda/bin/conda env create -f fastqc.yaml

%runscript
    exec /bin/bash
```

## Collection

 - Name: [ohsu-cedar-comp-hub/Bulk-RNA-seq-pipeline-SE](https://github.com/ohsu-cedar-comp-hub/Bulk-RNA-seq-pipeline-SE)
 - License: None

