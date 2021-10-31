---
id: 7594
name: "chrarnold/Singularity_images"
branch: "master"
tag: "variant-calling_r"
commit: "f7a02b158ba8b5c5372644c873d9dc006952d571"
version: "0a1d1c34809b285e67468663b1b51791"
build_date: "2019-03-06T12:46:32.643Z"
size_mb: 2293
size: 809537567
sif: "https://datasets.datalad.org/shub/chrarnold/Singularity_images/variant-calling_r/2019-03-06-f7a02b15-0a1d1c34/0a1d1c34809b285e67468663b1b51791.simg"
url: https://datasets.datalad.org/shub/chrarnold/Singularity_images/variant-calling_r/2019-03-06-f7a02b15-0a1d1c34/
recipe: https://datasets.datalad.org/shub/chrarnold/Singularity_images/variant-calling_r/2019-03-06-f7a02b15-0a1d1c34/Singularity
collection: chrarnold/Singularity_images
---

# chrarnold/Singularity_images:variant-calling_r

```bash
$ singularity pull shub://chrarnold/Singularity_images:variant-calling_r
```

## Singularity Recipe

```singularity
Bootstrap: docker
FROM: bioconductor/release_core2

%labels
  Version v1.0

%help
  Singularity image for the variant calling pipeline (R 3.5.1 + all packages + java)



%post

  R --slave -e "install.packages('tools')"
  R --slave -e "install.packages('tidyverse')"
  R --slave -e "install.packages('grid')"
  R --slave -e "install.packages('gplots')"
  R --slave -e "install.packages('reshape')"
  R --slave -e "install.packages('gsalib')"
  apt update
  apt install --yes default-jre

%environment

%test
  R --version
```

## Collection

 - Name: [chrarnold/Singularity_images](https://github.com/chrarnold/Singularity_images)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

