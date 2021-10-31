---
id: 9328
name: "ohsu-cedar-comp-hub/Bulk-RNA-seq-pipeline-SE"
branch: "master"
tag: "fastqscreen"
commit: "6cf58e9d84080805a3beaf08bca0e547abe6152c"
version: "d0245dda623cf13e885a81ab0f5c866b"
build_date: "2019-05-28T19:47:19.970Z"
size_mb: 1231
size: 465596447
sif: "https://datasets.datalad.org/shub/ohsu-cedar-comp-hub/Bulk-RNA-seq-pipeline-SE/fastqscreen/2019-05-28-6cf58e9d-d0245dda/d0245dda623cf13e885a81ab0f5c866b.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ohsu-cedar-comp-hub/Bulk-RNA-seq-pipeline-SE/fastqscreen/2019-05-28-6cf58e9d-d0245dda/
recipe: https://datasets.datalad.org/shub/ohsu-cedar-comp-hub/Bulk-RNA-seq-pipeline-SE/fastqscreen/2019-05-28-6cf58e9d-d0245dda/Singularity
collection: ohsu-cedar-comp-hub/Bulk-RNA-seq-pipeline-SE
---

# ohsu-cedar-comp-hub/Bulk-RNA-seq-pipeline-SE:fastqscreen

```bash
$ singularity pull shub://ohsu-cedar-comp-hub/Bulk-RNA-seq-pipeline-SE:fastqscreen
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: continuumio/miniconda3

%files
    fastqscreen.yaml

%environment
    PATH=/opt/conda/envs/$(head -1 fastqscreen.yaml | cut -d' ' -f2)/bin:$PATH

%post
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc
    echo "source activate $(head -1 fastqscreen.yaml | cut -d' ' -f2)" > ~/.bashrc
    /opt/conda/bin/conda env create -f fastqscreen.yaml

%runscript
    exec /bin/bash
```

## Collection

 - Name: [ohsu-cedar-comp-hub/Bulk-RNA-seq-pipeline-SE](https://github.com/ohsu-cedar-comp-hub/Bulk-RNA-seq-pipeline-SE)
 - License: None

