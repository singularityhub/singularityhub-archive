---
id: 1078
name: "NBISweden/K9-WGS-Pipeline"
branch: "master"
tag: "bwa-0.7.12"
commit: "7d8b390588d34fa52c6079885d549258a93daaff"
version: "93e3fc796f7ee91f478800ecd8ea1470"
build_date: "2020-11-19T06:09:28.279Z"
size_mb: 375
size: 117870623
sif: "https://datasets.datalad.org/shub/NBISweden/K9-WGS-Pipeline/bwa-0.7.12/2020-11-19-7d8b3905-93e3fc79/93e3fc796f7ee91f478800ecd8ea1470.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/NBISweden/K9-WGS-Pipeline/bwa-0.7.12/2020-11-19-7d8b3905-93e3fc79/
recipe: https://datasets.datalad.org/shub/NBISweden/K9-WGS-Pipeline/bwa-0.7.12/2020-11-19-7d8b3905-93e3fc79/Singularity
collection: NBISweden/K9-WGS-Pipeline
---

# NBISweden/K9-WGS-Pipeline:bwa-0.7.12

```bash
$ singularity pull shub://NBISweden/K9-WGS-Pipeline:bwa-0.7.12
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
conda install bwa=0.7.12 samtools=1.5
```

## Collection

 - Name: [NBISweden/K9-WGS-Pipeline](https://github.com/NBISweden/K9-WGS-Pipeline)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

