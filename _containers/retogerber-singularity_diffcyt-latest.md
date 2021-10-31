---
id: 13793
name: "retogerber/singularity_diffcyt"
branch: "master"
tag: "latest"
commit: "681a2f2a1e17dc656f345e5779b7ec19cafa8e05"
version: "54eea9156f8c33d43ebdc2655f9c548c368ce77eccf9e93a02bbc513685775a2"
build_date: "2021-03-31T05:39:59.511Z"
size_mb: 1499.76171875
size: 1572614144
sif: "https://datasets.datalad.org/shub/retogerber/singularity_diffcyt/latest/2021-03-31-681a2f2a-54eea915/54eea9156f8c33d43ebdc2655f9c548c368ce77eccf9e93a02bbc513685775a2.sif"
url: https://datasets.datalad.org/shub/retogerber/singularity_diffcyt/latest/2021-03-31-681a2f2a-54eea915/
recipe: https://datasets.datalad.org/shub/retogerber/singularity_diffcyt/latest/2021-03-31-681a2f2a-54eea915/Singularity
collection: retogerber/singularity_diffcyt
---

# retogerber/singularity_diffcyt:latest

```bash
$ singularity pull shub://retogerber/singularity_diffcyt:latest
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: retogerber/singularity_diffcyt_base

%post
        R -e 'devtools::install_github("retogerber/diffcyt",force=TRUE)'
        R -e 'devtools::install_version("broom",version="0.5.6")'
```

## Collection

 - Name: [retogerber/singularity_diffcyt](https://github.com/retogerber/singularity_diffcyt)
 - License: None

