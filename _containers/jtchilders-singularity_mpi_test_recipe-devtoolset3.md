---
id: 5528
name: "jtchilders/singularity_mpi_test_recipe"
branch: "master"
tag: "devtoolset3"
commit: "1136ccfba1553950037f61b8d6ce2a1526a70f69"
version: "ef8065c96b0b55b575d5d9e777f9557f"
build_date: "2019-01-29T17:36:12.107Z"
size_mb: 1752
size: 820015135
sif: "https://datasets.datalad.org/shub/jtchilders/singularity_mpi_test_recipe/devtoolset3/2019-01-29-1136ccfb-ef8065c9/ef8065c96b0b55b575d5d9e777f9557f.simg"
url: https://datasets.datalad.org/shub/jtchilders/singularity_mpi_test_recipe/devtoolset3/2019-01-29-1136ccfb-ef8065c9/
recipe: https://datasets.datalad.org/shub/jtchilders/singularity_mpi_test_recipe/devtoolset3/2019-01-29-1136ccfb-ef8065c9/Singularity
collection: jtchilders/singularity_mpi_test_recipe
---

# jtchilders/singularity_mpi_test_recipe:devtoolset3

```bash
$ singularity pull shub://jtchilders/singularity_mpi_test_recipe:devtoolset3
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos

%post
   # install development tools
   yum update -y
   yum install -y centos-release-scl
   yum install -y devtoolset-3
   yum install -y java-1.8.0-openjdk-devel.x86_64
```

## Collection

 - Name: [jtchilders/singularity_mpi_test_recipe](https://github.com/jtchilders/singularity_mpi_test_recipe)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

