---
id: 9188
name: "ohsu-cedar-comp-hub/Bulk-RNA-seq-pipeline-SE"
branch: "master"
tag: "deseq2"
commit: "6cf58e9d84080805a3beaf08bca0e547abe6152c"
version: "5df41eb82b4f2194fd4c17ea38658701"
build_date: "2019-05-28T19:46:49.857Z"
size_mb: 2158
size: 965554207
sif: "https://datasets.datalad.org/shub/ohsu-cedar-comp-hub/Bulk-RNA-seq-pipeline-SE/deseq2/2019-05-28-6cf58e9d-5df41eb8/5df41eb82b4f2194fd4c17ea38658701.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ohsu-cedar-comp-hub/Bulk-RNA-seq-pipeline-SE/deseq2/2019-05-28-6cf58e9d-5df41eb8/
recipe: https://datasets.datalad.org/shub/ohsu-cedar-comp-hub/Bulk-RNA-seq-pipeline-SE/deseq2/2019-05-28-6cf58e9d-5df41eb8/Singularity
collection: ohsu-cedar-comp-hub/Bulk-RNA-seq-pipeline-SE
---

# ohsu-cedar-comp-hub/Bulk-RNA-seq-pipeline-SE:deseq2

```bash
$ singularity pull shub://ohsu-cedar-comp-hub/Bulk-RNA-seq-pipeline-SE:deseq2
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: continuumio/miniconda3

%files
    deseq2.yaml

%environment
    PATH=/opt/conda/envs/$(head -1 deseq2.yaml | cut -d' ' -f2)/bin:$PATH

%post
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc
    echo "source activate $(head -1 deseq2.yaml | cut -d' ' -f2)" > ~/.bashrc
    /opt/conda/bin/conda env create -f deseq2.yaml

%runscript
    exec /bin/bash
```

## Collection

 - Name: [ohsu-cedar-comp-hub/Bulk-RNA-seq-pipeline-SE](https://github.com/ohsu-cedar-comp-hub/Bulk-RNA-seq-pipeline-SE)
 - License: None

