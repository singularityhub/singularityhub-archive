---
id: 281
name: "vsoch/singularity-hello-world"
branch: "master"
tag: "master"
commit: "54c13f6fad7d3365b43758d55f607fffc6dfc512"
version: "7e5f47bb07de3da9105896c1b1a61ea7"
build_date: "2021-04-04T00:03:12.943Z"
size_mb: 331
size: 51599774
sif: "https://datasets.datalad.org/shub/vsoch/singularity-hello-world/master/2021-04-04-54c13f6f-7e5f47bb/7e5f47bb07de3da9105896c1b1a61ea7.img.gz"
datalad_url: https://datasets.datalad.org?dir=/shub/vsoch/singularity-hello-world/master/2021-04-04-54c13f6f-7e5f47bb/
recipe: https://datasets.datalad.org/shub/vsoch/singularity-hello-world/master/2021-04-04-54c13f6f-7e5f47bb/Singularity
collection: vsoch/singularity-hello-world
---

# vsoch/singularity-hello-world:master

```bash
$ singularity pull shub://vsoch/singularity-hello-world:master
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:latest

% runscript

exec echo Hello "$@"
```

## Collection

 - Name: [vsoch/singularity-hello-world](https://github.com/vsoch/singularity-hello-world)
 - License: [MIT License](https://api.github.com/licenses/mit)

