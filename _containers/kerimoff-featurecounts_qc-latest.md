---
id: 8727
name: "kerimoff/featurecounts_qc"
branch: "master"
tag: "latest"
commit: "b9a7ebb6534eccc20b1cf7a866167e405e2f2158"
version: "51e09b768cca5c7b925adee275fa0e80"
build_date: "2019-05-01T22:22:28.889Z"
size_mb: 1860
size: 603545631
sif: "https://datasets.datalad.org/shub/kerimoff/featurecounts_qc/latest/2019-05-01-b9a7ebb6-51e09b76/51e09b768cca5c7b925adee275fa0e80.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/kerimoff/featurecounts_qc/latest/2019-05-01-b9a7ebb6-51e09b76/
recipe: https://datasets.datalad.org/shub/kerimoff/featurecounts_qc/latest/2019-05-01-b9a7ebb6-51e09b76/Singularity
collection: kerimoff/featurecounts_qc
---

# kerimoff/featurecounts_qc:latest

```bash
$ singularity pull shub://kerimoff/featurecounts_qc:latest
```

## Singularity Recipe

```singularity
From:nfcore/base
Bootstrap:docker

%labels
    MAINTAINER Nurlan Kerimov
    DESCRIPTION Singularity image containing all requirements for featureCounts QC steps
    VERSION 1.0dev

%environment
    PATH=/opt/conda/envs/feature_counts_qc/bin:$PATH
    export PATH

%files
    environment.yml /

%post
    /opt/conda/bin/conda env create -f /environment.yml
    /opt/conda/bin/conda clean -a
```

## Collection

 - Name: [kerimoff/featurecounts_qc](https://github.com/kerimoff/featurecounts_qc)
 - License: None

