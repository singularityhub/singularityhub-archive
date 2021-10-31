---
id: 11386
name: "sschmeier/container-gsea"
branch: "master"
tag: "latest"
commit: "3e10d4fbcad62b02c13e6c506adffcc474fd9a36"
version: "8760326adee1f7eb6893bb1f10a64f11db2a8cebd02778140c400a4180d4bd68"
build_date: "2020-11-23T08:40:46.301Z"
size_mb: 685.3046875
size: 718594048
sif: "https://datasets.datalad.org/shub/sschmeier/container-gsea/latest/2020-11-23-3e10d4fb-8760326a/8760326adee1f7eb6893bb1f10a64f11db2a8cebd02778140c400a4180d4bd68.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/sschmeier/container-gsea/latest/2020-11-23-3e10d4fb-8760326a/
recipe: https://datasets.datalad.org/shub/sschmeier/container-gsea/latest/2020-11-23-3e10d4fb-8760326a/Singularity
collection: sschmeier/container-gsea
---

# sschmeier/container-gsea:latest

```bash
$ singularity pull shub://sschmeier/container-gsea:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: sebio/gsea

%labels
   AUTHOR s.schmeier@protonmail.com

%post
  touch /`date -u -Iseconds`
```

## Collection

 - Name: [sschmeier/container-gsea](https://github.com/sschmeier/container-gsea)
 - License: None

