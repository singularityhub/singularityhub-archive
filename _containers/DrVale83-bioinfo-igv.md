---
id: 10165
name: "DrVale83/bioinfo"
branch: "master"
tag: "igv"
commit: "c9a1ea1ba988b21250f62eea895b7d5d01b4dd6b"
version: "ca75b09f6c823cce7a340a5cb9089984"
build_date: "2020-03-16T08:50:10.270Z"
size_mb: 609
size: 256679967
sif: "https://datasets.datalad.org/shub/DrVale83/bioinfo/igv/2020-03-16-c9a1ea1b-ca75b09f/ca75b09f6c823cce7a340a5cb9089984.simg"
url: https://datasets.datalad.org/shub/DrVale83/bioinfo/igv/2020-03-16-c9a1ea1b-ca75b09f/
recipe: https://datasets.datalad.org/shub/DrVale83/bioinfo/igv/2020-03-16-c9a1ea1b-ca75b09f/Singularity
collection: DrVale83/bioinfo
---

# DrVale83/bioinfo:igv

```bash
$ singularity pull shub://DrVale83/bioinfo:igv
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: debian:latest

%post
    apt-get update --fix-missing && apt-get install -y wget openjdk-8-jre unzip
    wget http://data.broadinstitute.org/igv/projects/downloads/2.4/IGV_2.4.18.zip
    unzip IGV_2.4.18.zip

%runscript
    exec /IGV_2.4.18/igv.sh
```

## Collection

 - Name: [DrVale83/bioinfo](https://github.com/DrVale83/bioinfo)
 - License: None

