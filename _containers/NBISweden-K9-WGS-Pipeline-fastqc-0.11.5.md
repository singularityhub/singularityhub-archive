---
id: 1079
name: "NBISweden/K9-WGS-Pipeline"
branch: "master"
tag: "fastqc-0.11.5"
commit: "3bc6c48dd5b953c4579a1d967540f950d78015e8"
version: "8bad0da004b27b8dc0e18ef663da17a6"
build_date: "2020-11-19T06:02:17.109Z"
size_mb: 760
size: 274526239
sif: "https://datasets.datalad.org/shub/NBISweden/K9-WGS-Pipeline/fastqc-0.11.5/2020-11-19-3bc6c48d-8bad0da0/8bad0da004b27b8dc0e18ef663da17a6.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/NBISweden/K9-WGS-Pipeline/fastqc-0.11.5/2020-11-19-3bc6c48d-8bad0da0/
recipe: https://datasets.datalad.org/shub/NBISweden/K9-WGS-Pipeline/fastqc-0.11.5/2020-11-19-3bc6c48d-8bad0da0/Singularity
collection: NBISweden/K9-WGS-Pipeline
---

# NBISweden/K9-WGS-Pipeline:fastqc-0.11.5

```bash
$ singularity pull shub://NBISweden/K9-WGS-Pipeline:fastqc-0.11.5
```

## Singularity Recipe

```singularity
bootstrap: docker
from: openjdk:8

# This is copied from https://github.com/SciLifeLab/CAW
%labels
AUTHOR Johan Viklund
MAINTAINER johan.viklund@gmail.com

%environment
FASTQC_VERSION=0.11.5

# Install libraries
%post
apt-get update
apt-get install -y --no-install-recommends wget
rm -rf /var/lib/apt/lists/*

# Install FastQC
export FASTQC_VERSION=0.11.5
wget --quiet -O fastqc_v${FASTQC_VERSION}.zip http://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v${FASTQC_VERSION}.zip
unzip fastqc_v${FASTQC_VERSION}.zip -d /opt/
chmod 755 /opt/FastQC/fastqc
ln -s /opt/FastQC/fastqc /usr/local/bin/fastqc
rm fastqc_v${FASTQC_VERSION}.zip
```

## Collection

 - Name: [NBISweden/K9-WGS-Pipeline](https://github.com/NBISweden/K9-WGS-Pipeline)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

