---
id: 9329
name: "ohsu-cedar-comp-hub/Bulk-RNA-seq-pipeline-SE"
branch: "master"
tag: "glimma_env"
commit: "6cf58e9d84080805a3beaf08bca0e547abe6152c"
version: "460ca1f402e574ffc79e7c5dbb217b98"
build_date: "2019-05-28T18:44:44.570Z"
size_mb: 2149
size: 961736735
sif: "https://datasets.datalad.org/shub/ohsu-cedar-comp-hub/Bulk-RNA-seq-pipeline-SE/glimma_env/2019-05-28-6cf58e9d-460ca1f4/460ca1f402e574ffc79e7c5dbb217b98.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ohsu-cedar-comp-hub/Bulk-RNA-seq-pipeline-SE/glimma_env/2019-05-28-6cf58e9d-460ca1f4/
recipe: https://datasets.datalad.org/shub/ohsu-cedar-comp-hub/Bulk-RNA-seq-pipeline-SE/glimma_env/2019-05-28-6cf58e9d-460ca1f4/Singularity
collection: ohsu-cedar-comp-hub/Bulk-RNA-seq-pipeline-SE
---

# ohsu-cedar-comp-hub/Bulk-RNA-seq-pipeline-SE:glimma_env

```bash
$ singularity pull shub://ohsu-cedar-comp-hub/Bulk-RNA-seq-pipeline-SE:glimma_env
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: continuumio/miniconda3

%files
    glimma_env.yaml

%environment
    PATH=/opt/conda/envs/$(head -1 glimma_env.yaml | cut -d' ' -f2)/bin:$PATH

%post
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc
    echo "source activate $(head -1 glimma_env.yaml | cut -d' ' -f2)" > ~/.bashrc
    /opt/conda/bin/conda env create -f glimma_env.yaml

%runscript
    exec /bin/bash
```

## Collection

 - Name: [ohsu-cedar-comp-hub/Bulk-RNA-seq-pipeline-SE](https://github.com/ohsu-cedar-comp-hub/Bulk-RNA-seq-pipeline-SE)
 - License: None

