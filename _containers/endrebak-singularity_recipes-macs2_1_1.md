---
id: 2067
name: "endrebak/singularity_recipes"
branch: "master"
tag: "macs2_1_1"
commit: "73d60889e6bc670e96bc9666e2d5fdad59f53933"
version: "384280a987c4271a187cc84f5fe7272e"
build_date: "2018-03-14T12:00:59.624Z"
size_mb: 3482
size: 1519775775
sif: "https://datasets.datalad.org/shub/endrebak/singularity_recipes/macs2_1_1/2018-03-14-73d60889-384280a9/384280a987c4271a187cc84f5fe7272e.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/endrebak/singularity_recipes/macs2_1_1/2018-03-14-73d60889-384280a9/
recipe: https://datasets.datalad.org/shub/endrebak/singularity_recipes/macs2_1_1/2018-03-14-73d60889-384280a9/Singularity
collection: endrebak/singularity_recipes
---

# endrebak/singularity_recipes:macs2_1_1

```bash
$ singularity pull shub://endrebak/singularity_recipes:macs2_1_1
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/anaconda

%post

apt-get update && apt-get install -y gcc

export PATH=/opt/conda/bin:${PATH}
echo 'export PATH=/opt/conda/bin:${PATH}' >> $SINGULARITY_ENVIRONMENT

conda config --add channels r
conda config --add channels bioconda
conda config --add channels conda-forge

conda install macs2
```

## Collection

 - Name: [endrebak/singularity_recipes](https://github.com/endrebak/singularity_recipes)
 - License: None

