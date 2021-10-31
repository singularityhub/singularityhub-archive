---
id: 6438
name: "mbhall88/Singularity_recipes"
branch: "master"
tag: "deepbinnergpu"
commit: "0a737380d0203675915d126b277b272870941233"
version: "4b9b1b107c50b155e6a807c181982973"
build_date: "2020-02-19T02:40:15.870Z"
size_mb: 3303
size: 1629020191
sif: "https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/deepbinnergpu/2020-02-19-0a737380-4b9b1b10/4b9b1b107c50b155e6a807c181982973.simg"
url: https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/deepbinnergpu/2020-02-19-0a737380-4b9b1b10/
recipe: https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/deepbinnergpu/2020-02-19-0a737380-4b9b1b10/Singularity
collection: mbhall88/Singularity_recipes
---

# mbhall88/Singularity_recipes:deepbinnergpu

```bash
$ singularity pull shub://mbhall88/Singularity_recipes:deepbinnergpu
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tensorflow/tensorflow:latest-gpu-py3

%post
    echo 'export LC_ALL=C.UTF-8' >> /environment
    echo 'export LANG=C.UTF-8' >> /environment
    export LC_ALL=C.UTF-8
    export LANG=C.UTF-8
    apt update
    apt install -y git wget

    pip3 install git+https://github.com/rrwick/Deepbinner.git
```

## Collection

 - Name: [mbhall88/Singularity_recipes](https://github.com/mbhall88/Singularity_recipes)
 - License: [MIT License](https://api.github.com/licenses/mit)

