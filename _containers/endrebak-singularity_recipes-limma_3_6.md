---
id: 1977
name: "endrebak/singularity_recipes"
branch: "master"
tag: "limma_3_6"
commit: "a0668e608f60d563f398f941219af4da55250a2b"
version: "54d5b527ed693fa174163f8a0dc2cf00"
build_date: "2018-03-07T14:12:48.411Z"
size_mb: 689
size: 270262303
sif: "https://datasets.datalad.org/shub/endrebak/singularity_recipes/limma_3_6/2018-03-07-a0668e60-54d5b527/54d5b527ed693fa174163f8a0dc2cf00.simg"
url: https://datasets.datalad.org/shub/endrebak/singularity_recipes/limma_3_6/2018-03-07-a0668e60-54d5b527/
recipe: https://datasets.datalad.org/shub/endrebak/singularity_recipes/limma_3_6/2018-03-07-a0668e60-54d5b527/Singularity
collection: endrebak/singularity_recipes
---

# endrebak/singularity_recipes:limma_3_6

```bash
$ singularity pull shub://endrebak/singularity_recipes:limma_3_6
```

## Singularity Recipe

```singularity
BootStrap: docker
From: r-base

%post
  echo 'source("https://bioconductor.org/biocLite.R"); biocLite("limma"); biocLite("edgeR")' >> /tmp/packages.R
  Rscript /tmp/packages.R
```

## Collection

 - Name: [endrebak/singularity_recipes](https://github.com/endrebak/singularity_recipes)
 - License: None

