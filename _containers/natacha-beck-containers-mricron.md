---
id: 2292
name: "natacha-beck/containers"
branch: "master"
tag: "mricron"
commit: "d3f20836a864dbfdc23ae0f1d933cdc0f867d68b"
version: "82efa943d9c1b4e2abe7800dd8b32765"
build_date: "2018-08-09T15:28:12.799Z"
size_mb: 253
size: 101535775
sif: "https://datasets.datalad.org/shub/natacha-beck/containers/mricron/2018-08-09-d3f20836-82efa943/82efa943d9c1b4e2abe7800dd8b32765.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/natacha-beck/containers/mricron/2018-08-09-d3f20836-82efa943/
recipe: https://datasets.datalad.org/shub/natacha-beck/containers/mricron/2018-08-09-d3f20836-82efa943/Singularity
collection: natacha-beck/containers
---

# natacha-beck/containers:mricron

```bash
$ singularity pull shub://natacha-beck/containers:mricron
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: neurodebian:artful-non-free

%labels
  Maintainer Natacha Beck

%help
This container provides 'dcm2nii' that supports converting DICOM 
and PAR/REC images into the NIfTI format, from the mricron package. 
http://people.cas.sc.edu/rorden/mricron/index.html  

%post
  apt-get update
  apt-get install -y mricron
```

## Collection

 - Name: [natacha-beck/containers](https://github.com/natacha-beck/containers)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

