---
id: 5529
name: "jtchilders/singularity_mpi_test_recipe"
branch: "master"
tag: "devtoolset6"
commit: "1136ccfba1553950037f61b8d6ce2a1526a70f69"
version: "ed461e750668bf1dee4530c3a26f5ec5"
build_date: "2019-01-30T00:38:09.081Z"
size_mb: 853
size: 289353759
sif: "https://datasets.datalad.org/shub/jtchilders/singularity_mpi_test_recipe/devtoolset6/2019-01-30-1136ccfb-ed461e75/ed461e750668bf1dee4530c3a26f5ec5.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jtchilders/singularity_mpi_test_recipe/devtoolset6/2019-01-30-1136ccfb-ed461e75/
recipe: https://datasets.datalad.org/shub/jtchilders/singularity_mpi_test_recipe/devtoolset6/2019-01-30-1136ccfb-ed461e75/Singularity
collection: jtchilders/singularity_mpi_test_recipe
---

# jtchilders/singularity_mpi_test_recipe:devtoolset6

```bash
$ singularity pull shub://jtchilders/singularity_mpi_test_recipe:devtoolset6
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

 - Name: [jtchilders/singularity_mpi_test_recipe](https://github.com/jtchilders/singularity_mpi_test_recipe)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

