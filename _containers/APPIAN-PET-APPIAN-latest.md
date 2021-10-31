---
id: 10758
name: "APPIAN-PET/APPIAN"
branch: "master"
tag: "latest"
commit: "42ddc5ffc81c8d2c697c96b829e6b538a529f204"
version: "75f42a3ff6aaba34748cae232882e801"
build_date: "2021-02-26T15:36:39.748Z"
size_mb: 3765.0
size: 1793687583
sif: "https://datasets.datalad.org/shub/APPIAN-PET/APPIAN/latest/2021-02-26-42ddc5ff-75f42a3f/75f42a3ff6aaba34748cae232882e801.sif"
url: https://datasets.datalad.org/shub/APPIAN-PET/APPIAN/latest/2021-02-26-42ddc5ff-75f42a3f/
recipe: https://datasets.datalad.org/shub/APPIAN-PET/APPIAN/latest/2021-02-26-42ddc5ff-75f42a3f/Singularity
collection: APPIAN-PET/APPIAN
---

# APPIAN-PET/APPIAN:latest

```bash
$ singularity pull shub://APPIAN-PET/APPIAN:latest
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: APPIAN-PET/APPIAN:base

%post
cd /opt
git clone http://www.github.com/APPIAN-PET/APPIAN 

%environment

%runscript
```

## Collection

 - Name: [APPIAN-PET/APPIAN](https://github.com/APPIAN-PET/APPIAN)
 - License: [MIT License](https://api.github.com/licenses/mit)

