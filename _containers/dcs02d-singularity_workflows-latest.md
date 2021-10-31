---
id: 1570
name: "dcs02d/singularity_workflows"
branch: "master"
tag: "latest"
commit: "c07e95ffc932e55b918182031c70ed7e39d34832"
version: "c68ef92e076e15afb272f82f79a19cf7"
build_date: "2018-02-02T03:30:19.597Z"
size_mb: 171
size: 54419487
sif: "https://datasets.datalad.org/shub/dcs02d/singularity_workflows/latest/2018-02-02-c07e95ff-c68ef92e/c68ef92e076e15afb272f82f79a19cf7.simg"
url: https://datasets.datalad.org/shub/dcs02d/singularity_workflows/latest/2018-02-02-c07e95ff-c68ef92e/
recipe: https://datasets.datalad.org/shub/dcs02d/singularity_workflows/latest/2018-02-02-c07e95ff-c68ef92e/Singularity
collection: dcs02d/singularity_workflows
---

# dcs02d/singularity_workflows:latest

```bash
$ singularity pull shub://dcs02d/singularity_workflows:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: dcshrum/singularity:cowsay

%help
A first singularity container.  A cow will report the output of sysbench.

%labels
  Maintainer Donny Shrum
  Version v1.1

%post
  mkdir /panfs


%runscript
  echo "My name is $COW_NAME. I am the best cow." | /usr/games/cowsay > /results.txt
  echo "Arguments Received: $*" >> /results.txt
```

## Collection

 - Name: [dcs02d/singularity_workflows](https://github.com/dcs02d/singularity_workflows)
 - License: None

