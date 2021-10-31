---
id: 15641
name: "cnoel-sebimer/singularity-orson"
branch: "master"
tag: "latest"
commit: "5ddaa06b67ab7e5176e3abbf25ccc68b642f2a9d"
version: "8e2cd348c3fa13f44fed3aae5b71ac85"
build_date: "2021-03-09T06:40:11.112Z"
size_mb: 772.0
size: 299757599
sif: "https://datasets.datalad.org/shub/cnoel-sebimer/singularity-orson/latest/2021-03-09-5ddaa06b-8e2cd348/8e2cd348c3fa13f44fed3aae5b71ac85.sif"
url: https://datasets.datalad.org/shub/cnoel-sebimer/singularity-orson/latest/2021-03-09-5ddaa06b-8e2cd348/
recipe: https://datasets.datalad.org/shub/cnoel-sebimer/singularity-orson/latest/2021-03-09-5ddaa06b-8e2cd348/Singularity
collection: cnoel-sebimer/singularity-orson
---

# cnoel-sebimer/singularity-orson:latest

```bash
$ singularity pull shub://cnoel-sebimer/singularity-orson:latest
```

## Singularity Recipe

```singularity
Bootstrap : docker
From: ubuntu:16.04

%post
        apt-get -y update
        apt-get -y install wget

        #Installation of BLAST
        cd /opt
        wget https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.10.0/ncbi-blast-2.10.0+-x64-linux.tar.gz
        gunzip ncbi-blast-2.10.0+-x64-linux.tar.gz
        tar -xvf ncbi-blast-2.10.0+-x64-linux.tar
        rm -f /opt/*.gz /opt/*.tar

%environment
        export PATH="/opt/ncbi-blast-2.10.0+/bin:$PATH"
```

## Collection

 - Name: [cnoel-sebimer/singularity-orson](https://github.com/cnoel-sebimer/singularity-orson)
 - License: None

