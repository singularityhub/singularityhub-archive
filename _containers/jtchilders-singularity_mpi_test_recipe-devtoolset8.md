---
id: 8269
name: "jtchilders/singularity_mpi_test_recipe"
branch: "master"
tag: "devtoolset8"
commit: "9cadbeea866d4e491d890ee94f2ba2cac6bb3f80"
version: "de2dfc92931b47d15b9e833cf3034aea"
build_date: "2019-04-08T08:50:10.990Z"
size_mb: 976
size: 339816479
sif: "https://datasets.datalad.org/shub/jtchilders/singularity_mpi_test_recipe/devtoolset8/2019-04-08-9cadbeea-de2dfc92/de2dfc92931b47d15b9e833cf3034aea.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jtchilders/singularity_mpi_test_recipe/devtoolset8/2019-04-08-9cadbeea-de2dfc92/
recipe: https://datasets.datalad.org/shub/jtchilders/singularity_mpi_test_recipe/devtoolset8/2019-04-08-9cadbeea-de2dfc92/Singularity
collection: jtchilders/singularity_mpi_test_recipe
---

# jtchilders/singularity_mpi_test_recipe:devtoolset8

```bash
$ singularity pull shub://jtchilders/singularity_mpi_test_recipe:devtoolset8
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos

%post
   # install development tools
   yum update -y
   yum install -y centos-release-scl
   yum install -y devtoolset-8
   yum install -y java-1.8.0-openjdk-devel.x86_64
   yum install -y git wget
```

## Collection

 - Name: [jtchilders/singularity_mpi_test_recipe](https://github.com/jtchilders/singularity_mpi_test_recipe)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

