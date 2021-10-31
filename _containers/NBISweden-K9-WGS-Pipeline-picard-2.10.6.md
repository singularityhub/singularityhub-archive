---
id: 2314
name: "NBISweden/K9-WGS-Pipeline"
branch: "master"
tag: "picard-2.10.6"
commit: "bb81f65dafd5fe8a6405c64e0c11f8c7dd948484"
version: "ca94ee21419c76a1c177ab8eef3f19c9"
build_date: "2020-11-19T06:02:36.617Z"
size_mb: 673
size: 323936287
sif: "https://datasets.datalad.org/shub/NBISweden/K9-WGS-Pipeline/picard-2.10.6/2020-11-19-bb81f65d-ca94ee21/ca94ee21419c76a1c177ab8eef3f19c9.simg"
url: https://datasets.datalad.org/shub/NBISweden/K9-WGS-Pipeline/picard-2.10.6/2020-11-19-bb81f65d-ca94ee21/
recipe: https://datasets.datalad.org/shub/NBISweden/K9-WGS-Pipeline/picard-2.10.6/2020-11-19-bb81f65d-ca94ee21/Singularity
collection: NBISweden/K9-WGS-Pipeline
---

# NBISweden/K9-WGS-Pipeline:picard-2.10.6

```bash
$ singularity pull shub://NBISweden/K9-WGS-Pipeline:picard-2.10.6
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
conda install picard=2.10.6 samtools=1.5
```

## Collection

 - Name: [NBISweden/K9-WGS-Pipeline](https://github.com/NBISweden/K9-WGS-Pipeline)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

