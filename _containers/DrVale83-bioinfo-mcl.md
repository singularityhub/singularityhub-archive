---
id: 10184
name: "DrVale83/bioinfo"
branch: "master"
tag: "mcl"
commit: "78246d7fb1f3edeeca914f2ebf68b6e41b9f5221"
version: "6a5cedd289be7c60ee829af662ec4283"
build_date: "2019-07-03T13:50:46.941Z"
size_mb: 131
size: 56823839
sif: "https://datasets.datalad.org/shub/DrVale83/bioinfo/mcl/2019-07-03-78246d7f-6a5cedd2/6a5cedd289be7c60ee829af662ec4283.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/DrVale83/bioinfo/mcl/2019-07-03-78246d7f-6a5cedd2/
recipe: https://datasets.datalad.org/shub/DrVale83/bioinfo/mcl/2019-07-03-78246d7f-6a5cedd2/Singularity
collection: DrVale83/bioinfo
---

# DrVale83/bioinfo:mcl

```bash
$ singularity pull shub://DrVale83/bioinfo:mcl
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: debian:latest

%post
    apt-get update --fix-missing && apt-get install -y mcl

%runscript
    exec "$@"
```

## Collection

 - Name: [DrVale83/bioinfo](https://github.com/DrVale83/bioinfo)
 - License: None

