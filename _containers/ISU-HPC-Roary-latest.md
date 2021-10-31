---
id: 5360
name: "ISU-HPC/Roary"
branch: "master"
tag: "latest"
commit: "c05f2c90a117ecb163f9a874527d6271211a6c72"
version: "151351410db6bfa4f52bf3b71670a56d"
build_date: "2018-10-28T06:48:36.207Z"
size_mb: 1649
size: 532516895
sif: "https://datasets.datalad.org/shub/ISU-HPC/Roary/latest/2018-10-28-c05f2c90-15135141/151351410db6bfa4f52bf3b71670a56d.simg"
url: https://datasets.datalad.org/shub/ISU-HPC/Roary/latest/2018-10-28-c05f2c90-15135141/
recipe: https://datasets.datalad.org/shub/ISU-HPC/Roary/latest/2018-10-28-c05f2c90-15135141/Singularity
collection: ISU-HPC/Roary
---

# ISU-HPC/Roary:latest

```bash
$ singularity pull shub://ISU-HPC/Roary:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:ubuntu:bionic

%labels

MAINTAINER ynanyam@iastate.edu

%post

apt-get update -qq && apt-get install -y roary
```

## Collection

 - Name: [ISU-HPC/Roary](https://github.com/ISU-HPC/Roary)
 - License: None

