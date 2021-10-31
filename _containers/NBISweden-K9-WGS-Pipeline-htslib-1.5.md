---
id: 1337
name: "NBISweden/K9-WGS-Pipeline"
branch: "master"
tag: "htslib-1.5"
commit: "3bc6c48dd5b953c4579a1d967540f950d78015e8"
version: "47065cfc9d909359f34c1c18a33cfc6b"
build_date: "2020-11-19T06:02:44.505Z"
size_mb: 367
size: 114085919
sif: "https://datasets.datalad.org/shub/NBISweden/K9-WGS-Pipeline/htslib-1.5/2020-11-19-3bc6c48d-47065cfc/47065cfc9d909359f34c1c18a33cfc6b.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/NBISweden/K9-WGS-Pipeline/htslib-1.5/2020-11-19-3bc6c48d-47065cfc/
recipe: https://datasets.datalad.org/shub/NBISweden/K9-WGS-Pipeline/htslib-1.5/2020-11-19-3bc6c48d-47065cfc/Singularity
collection: NBISweden/K9-WGS-Pipeline
---

# NBISweden/K9-WGS-Pipeline:htslib-1.5

```bash
$ singularity pull shub://NBISweden/K9-WGS-Pipeline:htslib-1.5
```

## Singularity Recipe

```singularity
Bootstrap:docker
From: conda/miniconda3:latest

%labels
AUTHOR Johan Viklund
MAINTAINER johan.viklund@nbis.se

%post
conda config --add channels conda-forge
conda config --add channels bioconda
conda install htslib=1.5
```

## Collection

 - Name: [NBISweden/K9-WGS-Pipeline](https://github.com/NBISweden/K9-WGS-Pipeline)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

