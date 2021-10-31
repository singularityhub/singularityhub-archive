---
id: 3566
name: "mbhall88/Singularity_recipes"
branch: "master"
tag: "template"
commit: "8ee4bdea8783116e87ab373e94524ca3d3aea30b"
version: "81d44fa01af649bc6398d61512ebbdf7"
build_date: "2019-09-24T08:53:04.156Z"
size_mb: 611
size: 222482463
sif: "https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/template/2019-09-24-8ee4bdea-81d44fa0/81d44fa01af649bc6398d61512ebbdf7.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/mbhall88/Singularity_recipes/template/2019-09-24-8ee4bdea-81d44fa0/
recipe: https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/template/2019-09-24-8ee4bdea-81d44fa0/Singularity
collection: mbhall88/Singularity_recipes
---

# mbhall88/Singularity_recipes:template

```bash
$ singularity pull shub://mbhall88/Singularity_recipes:template
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
OSVersion: bionic
MirrorURL: http://us.archive.ubuntu.com/ubuntu/

%post
    apt update
    apt install -y software-properties-common
    apt-add-repository universe
    apt update
    apt install -y git wget build-essential
    export LC_ALL=C.UTF-8
    export LANG=C.UTF-8
    echo 'export LC_ALL=C.UTF-8' >> "$SINGULARITY_ENVIRONMENT"
    echo 'export LANG=C.UTF-8' >> "$SINGULARITY_ENVIRONMENT"
    echo "export PATH=/usr/local:/usr/local/bin:$PATH" >> "$SINGULARITY_ENVIRONMENT"

    # ================================
    # INSTALL <program>
    # ================================
```

## Collection

 - Name: [mbhall88/Singularity_recipes](https://github.com/mbhall88/Singularity_recipes)
 - License: [MIT License](https://api.github.com/licenses/mit)

