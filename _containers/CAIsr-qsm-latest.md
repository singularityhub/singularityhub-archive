---
id: 1631
name: "CAIsr/qsm"
branch: "v1.2.3"
tag: "latest"
commit: "fc23912ad565d90d741e48bd7a41074f095296c1"
version: "74072801f86874d12088ff3003ac317d"
build_date: "2020-09-28T07:08:33.813Z"
size_mb: 924
size: 424931359
sif: "https://datasets.datalad.org/shub/CAIsr/qsm/latest/2020-09-28-fc23912a-74072801/74072801f86874d12088ff3003ac317d.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/CAIsr/qsm/latest/2020-09-28-fc23912a-74072801/
recipe: https://datasets.datalad.org/shub/CAIsr/qsm/latest/2020-09-28-fc23912a-74072801/Singularity
collection: CAIsr/qsm
---

# CAIsr/qsm:latest

```bash
$ singularity pull shub://CAIsr/qsm:latest
```

## Singularity Recipe

```singularity
BootStrap:docker
From:caid/qsm

%files

%labels
MAINTAINER Steffen.Bollmann@cai.uq.edu.au

%environment

%runscript
echo "This gets run when you run the image!"

%post
echo "This section happens once after bootstrap to build the image."
```

## Collection

 - Name: [CAIsr/qsm](https://github.com/CAIsr/qsm)
 - License: None

