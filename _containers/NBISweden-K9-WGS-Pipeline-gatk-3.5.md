---
id: 1080
name: "NBISweden/K9-WGS-Pipeline"
branch: "master"
tag: "gatk-3.5"
commit: "3bc6c48dd5b953c4579a1d967540f950d78015e8"
version: "8fb5f4df47cedf6c81b10f141415cdd3"
build_date: "2020-11-19T06:02:29.263Z"
size_mb: 867
size: 346837023
sif: "https://datasets.datalad.org/shub/NBISweden/K9-WGS-Pipeline/gatk-3.5/2020-11-19-3bc6c48d-8fb5f4df/8fb5f4df47cedf6c81b10f141415cdd3.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/NBISweden/K9-WGS-Pipeline/gatk-3.5/2020-11-19-3bc6c48d-8fb5f4df/
recipe: https://datasets.datalad.org/shub/NBISweden/K9-WGS-Pipeline/gatk-3.5/2020-11-19-3bc6c48d-8fb5f4df/Singularity
collection: NBISweden/K9-WGS-Pipeline
---

# NBISweden/K9-WGS-Pipeline:gatk-3.5

```bash
$ singularity pull shub://NBISweden/K9-WGS-Pipeline:gatk-3.5
```

## Singularity Recipe

```singularity
bootstrap: docker
from:broadinstitute/gatk3:3.5-0

%labels
AUTHOR Johan Viklund
MAINTAINER johan.viklund@nbis.se

%post
apt-get install pkg-config

curl -LO https://github.com/vcftools/vcftools/releases/download/v0.1.15/vcftools-0.1.15.tar.gz
tar xzf vcftools-0.1.15.tar.gz
cd vcftools-0.1.15
./configure
make
make install
```

## Collection

 - Name: [NBISweden/K9-WGS-Pipeline](https://github.com/NBISweden/K9-WGS-Pipeline)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

