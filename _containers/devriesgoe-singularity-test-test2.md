---
id: 7111
name: "devriesgoe/singularity-test"
branch: "master"
tag: "test2"
commit: "c3360a45407b8ab90d553fb9aff6e6fe14976922"
version: "4ebd238a2557d630c5d40ec59fa0adbb"
build_date: "2019-02-11T21:33:05.403Z"
size_mb: 728
size: 305340447
sif: "https://datasets.datalad.org/shub/devriesgoe/singularity-test/test2/2019-02-11-c3360a45-4ebd238a/4ebd238a2557d630c5d40ec59fa0adbb.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/devriesgoe/singularity-test/test2/2019-02-11-c3360a45-4ebd238a/
recipe: https://datasets.datalad.org/shub/devriesgoe/singularity-test/test2/2019-02-11-c3360a45-4ebd238a/Singularity
collection: devriesgoe/singularity-test
---

# devriesgoe/singularity-test:test2

```bash
$ singularity pull shub://devriesgoe/singularity-test:test2
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%post

apt-get -y update
apt-get -y install python3-pip

pip3 install numpy scipy matplotlib
```

## Collection

 - Name: [devriesgoe/singularity-test](https://github.com/devriesgoe/singularity-test)
 - License: None

