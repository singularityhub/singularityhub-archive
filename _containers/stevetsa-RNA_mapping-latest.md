---
id: 1891
name: "stevetsa/RNA_mapping"
branch: "master"
tag: "latest"
commit: "ce0973f01b6908b87aa8546888b68ec78eb520bc"
version: "d8664c7e26d17bc9b50dbb629e405714"
build_date: "2020-01-30T16:24:42.730Z"
size_mb: 2691
size: 1426309151
sif: "https://datasets.datalad.org/shub/stevetsa/RNA_mapping/latest/2020-01-30-ce0973f0-d8664c7e/d8664c7e26d17bc9b50dbb629e405714.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/stevetsa/RNA_mapping/latest/2020-01-30-ce0973f0-d8664c7e/
recipe: https://datasets.datalad.org/shub/stevetsa/RNA_mapping/latest/2020-01-30-ce0973f0-d8664c7e/Singularity
collection: stevetsa/RNA_mapping
---

# stevetsa/RNA_mapping:latest

```bash
$ singularity pull shub://stevetsa/RNA_mapping:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: stevetsa/rna_mapping:latest

%runscript

    echo "Runnning doAll.sh"
    exec /RNA_mapping/build/doAll.sh
```

## Collection

 - Name: [stevetsa/RNA_mapping](https://github.com/stevetsa/RNA_mapping)
 - License: None

