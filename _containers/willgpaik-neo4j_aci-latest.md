---
id: 10364
name: "willgpaik/neo4j_aci"
branch: "master"
tag: "latest"
commit: "c5cbbe11ce715660c10379874564d993bb01cd2b"
version: "4c57c0fac18e17ec28e6872039e0ec8d"
build_date: "2020-10-30T21:06:23.599Z"
size_mb: 3115.0
size: 1059958815
sif: "https://datasets.datalad.org/shub/willgpaik/neo4j_aci/latest/2020-10-30-c5cbbe11-4c57c0fa/4c57c0fac18e17ec28e6872039e0ec8d.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/willgpaik/neo4j_aci/latest/2020-10-30-c5cbbe11-4c57c0fa/
recipe: https://datasets.datalad.org/shub/willgpaik/neo4j_aci/latest/2020-10-30-c5cbbe11-4c57c0fa/Singularity
collection: willgpaik/neo4j_aci
---

# willgpaik/neo4j_aci:latest

```bash
$ singularity pull shub://willgpaik/neo4j_aci:latest
```

## Singularity Recipe

```singularity
BootStrap: shub
From: willgpaik/centos7_aci

%setup

%files

%environment

%runscript

%post
    yum -y install firefox java-11-openjdk-devel
    yum -y update
```

## Collection

 - Name: [willgpaik/neo4j_aci](https://github.com/willgpaik/neo4j_aci)
 - License: None

