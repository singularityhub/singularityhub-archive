---
id: 7422
name: "Amjadhpc/R-3.5.1"
branch: "master"
tag: "def"
commit: "624ee41b2d6891b12081af4842f709aada4d6b2a"
version: "7a4e93c1480b04c61c31945c4054c641"
build_date: "2019-07-27T00:03:58.473Z"
size_mb: 932
size: 356556831
sif: "https://datasets.datalad.org/shub/Amjadhpc/R-3.5.1/def/2019-07-27-624ee41b-7a4e93c1/7a4e93c1480b04c61c31945c4054c641.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/Amjadhpc/R-3.5.1/def/2019-07-27-624ee41b-7a4e93c1/
recipe: https://datasets.datalad.org/shub/Amjadhpc/R-3.5.1/def/2019-07-27-624ee41b-7a4e93c1/Singularity
collection: Amjadhpc/R-3.5.1
---

# Amjadhpc/R-3.5.1:def

```bash
$ singularity pull shub://Amjadhpc/R-3.5.1:def
```

## Singularity Recipe

```singularity
BootStrap: shub

From: nickjer/singularity-r:3.5.1



%help
This is singularity 3.0.2  image for  R 3.5.1


%setup


%post
 R --slave -e 'install.packages("BiocManager", repos="https://cloud.r-project.org/")'
 R --slave -e 'BiocManager::install("arrayQualityMetrics", version = "3.8")'
%labels
   AUTHOR  Amjad Syed

   Email  amjadcsu@gmail.com
```

## Collection

 - Name: [Amjadhpc/R-3.5.1](https://github.com/Amjadhpc/R-3.5.1)
 - License: None

