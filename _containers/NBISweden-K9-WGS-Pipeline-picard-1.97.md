---
id: 1077
name: "NBISweden/K9-WGS-Pipeline"
branch: "master"
tag: "picard-1.97"
commit: "3bc6c48dd5b953c4579a1d967540f950d78015e8"
version: "14bb35cd51e36917a4f6b592cfe58ec5"
build_date: "2020-11-19T06:09:28.231Z"
size_mb: 570
size: 265334815
sif: "https://datasets.datalad.org/shub/NBISweden/K9-WGS-Pipeline/picard-1.97/2020-11-19-3bc6c48d-14bb35cd/14bb35cd51e36917a4f6b592cfe58ec5.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/NBISweden/K9-WGS-Pipeline/picard-1.97/2020-11-19-3bc6c48d-14bb35cd/
recipe: https://datasets.datalad.org/shub/NBISweden/K9-WGS-Pipeline/picard-1.97/2020-11-19-3bc6c48d-14bb35cd/Singularity
collection: NBISweden/K9-WGS-Pipeline
---

# NBISweden/K9-WGS-Pipeline:picard-1.97

```bash
$ singularity pull shub://NBISweden/K9-WGS-Pipeline:picard-1.97
```

## Singularity Recipe

```singularity
bootstrap: docker
from: conda/miniconda3:latest

%labels
AUTHOR Johan Viklund
MAINTAINER johan.viklund@nbis.se

%post
conda config --add channels conda-forge
conda config --add channels bioconda
conda install picard=1.97
```

## Collection

 - Name: [NBISweden/K9-WGS-Pipeline](https://github.com/NBISweden/K9-WGS-Pipeline)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

