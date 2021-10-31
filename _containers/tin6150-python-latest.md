---
id: 11533
name: "tin6150/python"
branch: "3.8"
tag: "latest"
commit: "3e3bf2f72d34304f5268210c1d1dc40dacba2deb"
version: "797c40f219723d03e5a1e357691adfff"
build_date: "2019-11-08T17:49:22.687Z"
size_mb: 117.0
size: 36007967
sif: "https://datasets.datalad.org/shub/tin6150/python/latest/2019-11-08-3e3bf2f7-797c40f2/797c40f219723d03e5a1e357691adfff.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/tin6150/python/latest/2019-11-08-3e3bf2f7-797c40f2/
recipe: https://datasets.datalad.org/shub/tin6150/python/latest/2019-11-08-3e3bf2f7-797c40f2/Singularity
collection: tin6150/python
---

# tin6150/python:latest

```bash
$ singularity pull shub://tin6150/python:latest
```

## Singularity Recipe

```singularity
# singularity container definition for
# python (3.8 in this branch)
# essentially a straight conversion from docker
# cuz somehow
# singularity pull py38.sif docker://python:3.8-alpine
# generated an error 
#
# https://singularity-hub.org/collections/3767


# container size is about 35 MB

BootStrap: docker
From: python:3.8-alpine

%post
      touch "_ROOT_DIR_OF_CONTAINER_" ## have a flag file for easy identification it is inside a container world
      date >> _ROOT_DIR_OF_CONTAINER_


%runscript
      python3 "$@"

%help
      python3 computer programming language enviroment (from docker container)
```

## Collection

 - Name: [tin6150/python](https://github.com/tin6150/python)
 - License: None

