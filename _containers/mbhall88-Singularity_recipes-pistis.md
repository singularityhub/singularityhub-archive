---
id: 7359
name: "mbhall88/Singularity_recipes"
branch: "master"
tag: "pistis"
commit: "af7b5cd9434e608fae1e1da94fd197c97bf367df"
version: "c0161afb485b937f58e38f7bf16c7966"
build_date: "2019-02-21T11:20:56.833Z"
size_mb: 1022
size: 416387103
sif: "https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/pistis/2019-02-21-af7b5cd9-c0161afb/c0161afb485b937f58e38f7bf16c7966.simg"
url: https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/pistis/2019-02-21-af7b5cd9-c0161afb/
recipe: https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/pistis/2019-02-21-af7b5cd9-c0161afb/Singularity
collection: mbhall88/Singularity_recipes
---

# mbhall88/Singularity_recipes:pistis

```bash
$ singularity pull shub://mbhall88/Singularity_recipes:pistis
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: mbhall88/Singularity_recipes:template

%post
    apt update
    apt install -y python3-pip
    # ================================
    # INSTALL pistis
    # ================================
    VERSION="0.3.3"
    pip3 install pistis=="$VERSION"

%test
    command -v pistis || exit 1
```

## Collection

 - Name: [mbhall88/Singularity_recipes](https://github.com/mbhall88/Singularity_recipes)
 - License: [MIT License](https://api.github.com/licenses/mit)

