---
id: 2735
name: "fenz/singularity-images"
branch: "master"
tag: "centos"
commit: "c82b4783d167ff3b7fa2a7df37b66754043d03f1"
version: "88e661d1bf3570e8535d187a965faa4f"
build_date: "2018-05-08T13:50:24.793Z"
size_mb: 279
size: 83025951
sif: "https://datasets.datalad.org/shub/fenz/singularity-images/centos/2018-05-08-c82b4783-88e661d1/88e661d1bf3570e8535d187a965faa4f.simg"
url: https://datasets.datalad.org/shub/fenz/singularity-images/centos/2018-05-08-c82b4783-88e661d1/
recipe: https://datasets.datalad.org/shub/fenz/singularity-images/centos/2018-05-08-c82b4783-88e661d1/Singularity
collection: fenz/singularity-images
---

# fenz/singularity-images:centos

```bash
$ singularity pull shub://fenz/singularity-images:centos
```

## Singularity Recipe

```singularity
BootStrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/
Include: yum
```

## Collection

 - Name: [fenz/singularity-images](https://github.com/fenz/singularity-images)
 - License: None

