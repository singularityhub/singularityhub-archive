---
id: 4237
name: "DeepLearnPhysics/playground-singularity"
branch: "master"
tag: "ub16.04-step0"
commit: "d01e09be306c2b271e5e63801dc26457515a929e"
version: "cba9dc8864733df8801a2b4f6dcd162c"
build_date: "2018-08-29T00:42:10.286Z"
size_mb: 173
size: 78778399
sif: "https://datasets.datalad.org/shub/DeepLearnPhysics/playground-singularity/ub16.04-step0/2018-08-29-d01e09be-cba9dc88/cba9dc8864733df8801a2b4f6dcd162c.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/DeepLearnPhysics/playground-singularity/ub16.04-step0/2018-08-29-d01e09be-cba9dc88/
recipe: https://datasets.datalad.org/shub/DeepLearnPhysics/playground-singularity/ub16.04-step0/2018-08-29-d01e09be-cba9dc88/Singularity
collection: DeepLearnPhysics/playground-singularity
---

# DeepLearnPhysics/playground-singularity:ub16.04-step0

```bash
$ singularity pull shub://DeepLearnPhysics/playground-singularity:ub16.04-step0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%post
	apt-get -y update
	apt-get -y install lsb-release
```

## Collection

 - Name: [DeepLearnPhysics/playground-singularity](https://github.com/DeepLearnPhysics/playground-singularity)
 - License: None

