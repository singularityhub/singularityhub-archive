---
id: 1075
name: "NBISweden/K9-WGS-Pipeline"
branch: "master"
tag: "bwa-0-7-12"
commit: "fb3c7f5711947ab33cc42105840eb91dc6449c7d"
version: "b6987f9cf51864f580484da2127ad2ad"
build_date: "2017-12-08T10:41:23.910Z"
size_mb: 353
size: 111955999
sif: "https://datasets.datalad.org/shub/NBISweden/K9-WGS-Pipeline/bwa-0-7-12/2017-12-08-fb3c7f57-b6987f9c/b6987f9cf51864f580484da2127ad2ad.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/NBISweden/K9-WGS-Pipeline/bwa-0-7-12/2017-12-08-fb3c7f57-b6987f9c/
recipe: https://datasets.datalad.org/shub/NBISweden/K9-WGS-Pipeline/bwa-0-7-12/2017-12-08-fb3c7f57-b6987f9c/Singularity
collection: NBISweden/K9-WGS-Pipeline
---

# NBISweden/K9-WGS-Pipeline:bwa-0-7-12

```bash
$ singularity pull shub://NBISweden/K9-WGS-Pipeline:bwa-0-7-12
```

## Singularity Recipe

```singularity
Bootstrap:docker
From: conda/miniconda3:latest

%labels
AUTHOR "Johan Viklund"
MAINTAINER "johan.viklund@nbis.se"

%post
conda config --add channels conda-forge
conda config --add channels bioconda
conda install bwa=0.7.12 samtools=1.5

mkdir /pica /proj /scratch /sw /vagrant
```

## Collection

 - Name: [NBISweden/K9-WGS-Pipeline](https://github.com/NBISweden/K9-WGS-Pipeline)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

