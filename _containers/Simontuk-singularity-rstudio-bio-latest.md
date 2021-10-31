---
id: 10674
name: "Simontuk/singularity-rstudio-bio"
branch: "master"
tag: "latest"
commit: "6d85fb51fdf2278d4748bff275f29edb839be540"
version: "3087c94b25d3e8016269e8bf96b288b7572b43d7b0df3f7379f1b16a9090b6be"
build_date: "2019-08-20T15:34:00.554Z"
size_mb: 1251.0
size: 720220160
sif: "https://datasets.datalad.org/shub/Simontuk/singularity-rstudio-bio/latest/2019-08-20-6d85fb51-3087c94b/3087c94b25d3e8016269e8bf96b288b7572b43d7b0df3f7379f1b16a9090b6be.sif"
url: https://datasets.datalad.org/shub/Simontuk/singularity-rstudio-bio/latest/2019-08-20-6d85fb51-3087c94b/
recipe: https://datasets.datalad.org/shub/Simontuk/singularity-rstudio-bio/latest/2019-08-20-6d85fb51-3087c94b/Singularity
collection: Simontuk/singularity-rstudio-bio
---

# Simontuk/singularity-rstudio-bio:latest

```bash
$ singularity pull shub://Simontuk/singularity-rstudio-bio:latest
```

## Singularity Recipe

```singularity
BootStrap: shub
From: Simontuk/singularity-rstudio

%labels
  Maintainer Simon Steiger
  RStudio_Version 1.2.1335

%help
  This will run RStudio Server

%apprun rserver
  exec rserver "${@}"

%runscript
  exec rserver "${@}"

%environment
  export PATH=/usr/lib/rstudio-server/bin:${PATH}

%post
  Rscript -e "install.packages(c('devtools','tidyverse','ape','cowplot','Seurat','reticulate'))"
```

## Collection

 - Name: [Simontuk/singularity-rstudio-bio](https://github.com/Simontuk/singularity-rstudio-bio)
 - License: None

