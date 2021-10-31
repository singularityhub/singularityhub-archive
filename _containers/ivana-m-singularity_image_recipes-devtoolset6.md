---
id: 8332
name: "ivana-m/singularity_image_recipes"
branch: "master"
tag: "devtoolset6"
commit: "f408a6aebec003a0d3423092631149b43d41a9f0"
version: "750d19856e370561c84251a3f66ba407"
build_date: "2019-04-10T18:24:19.213Z"
size_mb: 894
size: 303710239
sif: "https://datasets.datalad.org/shub/ivana-m/singularity_image_recipes/devtoolset6/2019-04-10-f408a6ae-750d1985/750d19856e370561c84251a3f66ba407.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ivana-m/singularity_image_recipes/devtoolset6/2019-04-10-f408a6ae-750d1985/
recipe: https://datasets.datalad.org/shub/ivana-m/singularity_image_recipes/devtoolset6/2019-04-10-f408a6ae-750d1985/Singularity
collection: ivana-m/singularity_image_recipes
---

# ivana-m/singularity_image_recipes:devtoolset6

```bash
$ singularity pull shub://ivana-m/singularity_image_recipes:devtoolset6
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos

%post
   # install development tools
   yum update -y
   yum install -y centos-release-scl
   yum install -y devtoolset-6
   yum install -y java-1.8.0-openjdk-devel.x86_64
```

## Collection

 - Name: [ivana-m/singularity_image_recipes](https://github.com/ivana-m/singularity_image_recipes)
 - License: None

