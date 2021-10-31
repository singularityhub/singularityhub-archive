---
id: 1915
name: "sachinbeepathEC/Singularity"
branch: "master"
tag: "latest"
commit: "97fba96c5e7552d8e6539cbd351294d08340c0c0"
version: "5090179bae4d571514752ac511bf39ca"
build_date: "2018-03-02T21:00:31.544Z"
size_mb: 279
size: 83030047
sif: "https://datasets.datalad.org/shub/sachinbeepathEC/Singularity/latest/2018-03-02-97fba96c-5090179b/5090179bae4d571514752ac511bf39ca.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/sachinbeepathEC/Singularity/latest/2018-03-02-97fba96c-5090179b/
recipe: https://datasets.datalad.org/shub/sachinbeepathEC/Singularity/latest/2018-03-02-97fba96c-5090179b/Singularity
collection: sachinbeepathEC/Singularity
---

# sachinbeepathEC/Singularity:latest

```bash
$ singularity pull shub://sachinbeepathEC/Singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/
Include: yum

%runscript
    echo "testing"
```

## Collection

 - Name: [sachinbeepathEC/Singularity](https://github.com/sachinbeepathEC/Singularity)
 - License: None

