---
id: 4238
name: "DeepLearnPhysics/playground-singularity"
branch: "master"
tag: "ub16.04-step1"
commit: "cc6461e9b4323621bf3a139e91057798f89cc5cb"
version: "d29a65da6603e1860204e3b84feeae0c"
build_date: "2018-08-29T00:42:10.278Z"
size_mb: 173
size: 78782495
sif: "https://datasets.datalad.org/shub/DeepLearnPhysics/playground-singularity/ub16.04-step1/2018-08-29-cc6461e9-d29a65da/d29a65da6603e1860204e3b84feeae0c.simg"
url: https://datasets.datalad.org/shub/DeepLearnPhysics/playground-singularity/ub16.04-step1/2018-08-29-cc6461e9-d29a65da/
recipe: https://datasets.datalad.org/shub/DeepLearnPhysics/playground-singularity/ub16.04-step1/2018-08-29-cc6461e9-d29a65da/Singularity
collection: DeepLearnPhysics/playground-singularity
---

# DeepLearnPhysics/playground-singularity:ub16.04-step1

```bash
$ singularity pull shub://DeepLearnPhysics/playground-singularity:ub16.04-step1
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%help
Ubuntu16.04

To start your container simply try
singularity exec THIS_CONTAINER.simg bash

%labels
Maintainer drinkingkazu
Version ub16.04-step1

%environment
    export ANSWER=42

%post
    apt-get -y update
    apt-get -y install lsb-release
```

## Collection

 - Name: [DeepLearnPhysics/playground-singularity](https://github.com/DeepLearnPhysics/playground-singularity)
 - License: None

