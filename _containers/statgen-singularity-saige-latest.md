---
id: 5786
name: "statgen/singularity-saige"
branch: "master"
tag: "latest"
commit: "0bee795ae7f4c2898ce2252a4aa577629acbc436"
version: "b891f9546bd3e4153725860c9df4babf"
build_date: "2021-04-09T14:42:08.989Z"
size_mb: 1247
size: 392712223
sif: "https://datasets.datalad.org/shub/statgen/singularity-saige/latest/2021-04-09-0bee795a-b891f954/b891f9546bd3e4153725860c9df4babf.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/statgen/singularity-saige/latest/2021-04-09-0bee795a-b891f954/
recipe: https://datasets.datalad.org/shub/statgen/singularity-saige/latest/2021-04-09-0bee795a-b891f954/Singularity
collection: statgen/singularity-saige
---

# statgen/singularity-saige:latest

```bash
$ singularity pull shub://statgen/singularity-saige:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: statgen/docker-saige

%help
  A container for SAIGE.

%environment
  PATH=/usr/local/bin:$PATH

%post
  # post-setup script

  export LC_ALL=C.UTF-8
  export LANG=C.UTF-8
  echo 'export LC_ALL=C.UTF-8' >> $SINGULARITY_ENVIRONMENT
  echo 'export LANG=C.UTF-8' >> $SINGULARITY_ENVIRONMENT
```

## Collection

 - Name: [statgen/singularity-saige](https://github.com/statgen/singularity-saige)
 - License: None

