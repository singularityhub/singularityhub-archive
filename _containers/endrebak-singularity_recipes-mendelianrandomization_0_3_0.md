---
id: 2070
name: "endrebak/singularity_recipes"
branch: "master"
tag: "mendelianrandomization_0_3_0"
commit: "a759e97177a907eff080520285d2492b623c0c99"
version: "93202988eff8e6ebd7d4b70782bce0db"
build_date: "2018-03-14T15:22:05.472Z"
size_mb: 1032
size: 363659295
sif: "https://datasets.datalad.org/shub/endrebak/singularity_recipes/mendelianrandomization_0_3_0/2018-03-14-a759e971-93202988/93202988eff8e6ebd7d4b70782bce0db.simg"
url: https://datasets.datalad.org/shub/endrebak/singularity_recipes/mendelianrandomization_0_3_0/2018-03-14-a759e971-93202988/
recipe: https://datasets.datalad.org/shub/endrebak/singularity_recipes/mendelianrandomization_0_3_0/2018-03-14-a759e971-93202988/Singularity
collection: endrebak/singularity_recipes
---

# endrebak/singularity_recipes:mendelianrandomization_0_3_0

```bash
$ singularity pull shub://endrebak/singularity_recipes:mendelianrandomization_0_3_0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%post

apt-get update && apt-get install -y software-properties-common apt-transport-https
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
add-apt-repository 'deb [arch=amd64,i386] https://cran.rstudio.com/bin/linux/ubuntu xenial/'
apt-get update && apt-get install -y r-base libgmp3-dev

echo 'install.packages(c("MendelianRandomization"), repos = "http://cran.us.r-project.org")' > /tmp/packages.R

Rscript /tmp/packages.R
```

## Collection

 - Name: [endrebak/singularity_recipes](https://github.com/endrebak/singularity_recipes)
 - License: None

