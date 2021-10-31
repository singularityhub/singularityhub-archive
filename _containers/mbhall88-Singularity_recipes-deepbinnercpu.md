---
id: 6933
name: "mbhall88/Singularity_recipes"
branch: "master"
tag: "deepbinnercpu"
commit: "62a243ed71e93f76da8cc20fa12874f77fe9d8a6"
version: "e4b1f8c8539516b85a765cce97ce0422"
build_date: "2019-08-27T13:13:29.795Z"
size_mb: 1238
size: 501461023
sif: "https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/deepbinnercpu/2019-08-27-62a243ed-e4b1f8c8/e4b1f8c8539516b85a765cce97ce0422.simg"
url: https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/deepbinnercpu/2019-08-27-62a243ed-e4b1f8c8/
recipe: https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/deepbinnercpu/2019-08-27-62a243ed-e4b1f8c8/Singularity
collection: mbhall88/Singularity_recipes
---

# mbhall88/Singularity_recipes:deepbinnercpu

```bash
$ singularity pull shub://mbhall88/Singularity_recipes:deepbinnercpu
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tensorflow/tensorflow:latest-py3

%post
    echo 'export LC_ALL=C.UTF-8' >> /environment
    echo 'export LANG=C.UTF-8' >> /environment
    export LC_ALL=C.UTF-8
    export LANG=C.UTF-8
    apt update
    apt install -y git wget

    # pip3 seems to be broken in this container - fix
    python3 -m pip uninstall -y pip && apt install -y python3-pip --reinstall

    # ========================
    # INSTALL Deepbinner
    # ========================
    pip3 install git+https://github.com/rrwick/Deepbinner.git

%test
    deepbinner --help
```

## Collection

 - Name: [mbhall88/Singularity_recipes](https://github.com/mbhall88/Singularity_recipes)
 - License: [MIT License](https://api.github.com/licenses/mit)

