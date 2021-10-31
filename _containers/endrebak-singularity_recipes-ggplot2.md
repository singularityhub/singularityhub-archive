---
id: 1451
name: "endrebak/singularity_recipes"
branch: "master"
tag: "ggplot2"
commit: "73627a05ce9e0b0aebd6149c459331c3f6c84591"
version: "d75eecbddd89cdf907f8a756c5c2dd27"
build_date: "2018-02-15T09:08:03.775Z"
size_mb: 892
size: 317562911
sif: "https://datasets.datalad.org/shub/endrebak/singularity_recipes/ggplot2/2018-02-15-73627a05-d75eecbd/d75eecbddd89cdf907f8a756c5c2dd27.simg"
url: https://datasets.datalad.org/shub/endrebak/singularity_recipes/ggplot2/2018-02-15-73627a05-d75eecbd/
recipe: https://datasets.datalad.org/shub/endrebak/singularity_recipes/ggplot2/2018-02-15-73627a05-d75eecbd/Singularity
collection: endrebak/singularity_recipes
---

# endrebak/singularity_recipes:ggplot2

```bash
$ singularity pull shub://endrebak/singularity_recipes:ggplot2
```

## Singularity Recipe

```singularity
BootStrap: docker
From: r-base

%post
    echo 'install.packages(c("ggplot2",  "RColorBrewer", "plotrix"), repos="http://cran.us.r-project.org", dependencies=TRUE)' > /tmp/packages.R \
&& Rscript /tmp/packages.R
```

## Collection

 - Name: [endrebak/singularity_recipes](https://github.com/endrebak/singularity_recipes)
 - License: None

