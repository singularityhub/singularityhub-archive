---
id: 3761
name: "idot/Singularity_recipes"
branch: "master"
tag: "template"
commit: "ba33d859f9ac34aa7ba572d0af2587d6afcce99f"
version: "d3698275bb4a120587a0ea06540e6fbd"
build_date: "2018-07-30T16:14:05.760Z"
size_mb: 611
size: 222482463
sif: "https://datasets.datalad.org/shub/idot/Singularity_recipes/template/2018-07-30-ba33d859-d3698275/d3698275bb4a120587a0ea06540e6fbd.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/idot/Singularity_recipes/template/2018-07-30-ba33d859-d3698275/
recipe: https://datasets.datalad.org/shub/idot/Singularity_recipes/template/2018-07-30-ba33d859-d3698275/Singularity
collection: idot/Singularity_recipes
---

# idot/Singularity_recipes:template

```bash
$ singularity pull shub://idot/Singularity_recipes:template
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
OSVersion: bionic
MirrorURL: http://us.archive.ubuntu.com/ubuntu/

%environment
  PATH=/usr/local/bin:$PATH

%post
    apt update
    apt install -y software-properties-common
    apt-add-repository universe
    apt update
    apt install -y git wget build-essential
    export LC_ALL=C.UTF-8
    export LANG=C.UTF-8
    echo 'export LC_ALL=C.UTF-8' >> $SINGULARITY_ENVIRONMENT
    echo 'export LANG=C.UTF-8' >> $SINGULARITY_ENVIRONMENT
```

## Collection

 - Name: [idot/Singularity_recipes](https://github.com/idot/Singularity_recipes)
 - License: [MIT License](https://api.github.com/licenses/mit)

