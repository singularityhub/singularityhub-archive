---
id: 5530
name: "jtchilders/singularity_mpi_test_recipe"
branch: "master"
tag: "devtoolset4"
commit: "1136ccfba1553950037f61b8d6ce2a1526a70f69"
version: "e39c68a3e6111342e91a79e3ec1a375f"
build_date: "2019-01-30T00:38:09.087Z"
size_mb: 1575
size: 781557791
sif: "https://datasets.datalad.org/shub/jtchilders/singularity_mpi_test_recipe/devtoolset4/2019-01-30-1136ccfb-e39c68a3/e39c68a3e6111342e91a79e3ec1a375f.simg"
url: https://datasets.datalad.org/shub/jtchilders/singularity_mpi_test_recipe/devtoolset4/2019-01-30-1136ccfb-e39c68a3/
recipe: https://datasets.datalad.org/shub/jtchilders/singularity_mpi_test_recipe/devtoolset4/2019-01-30-1136ccfb-e39c68a3/Singularity
collection: jtchilders/singularity_mpi_test_recipe
---

# jtchilders/singularity_mpi_test_recipe:devtoolset4

```bash
$ singularity pull shub://jtchilders/singularity_mpi_test_recipe:devtoolset4
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos

%post
   # install development tools
   yum update -y
   yum install -y centos-release-scl
   yum install -y devtoolset-4
   yum install -y java-1.8.0-openjdk-devel.x86_64
```

## Collection

 - Name: [jtchilders/singularity_mpi_test_recipe](https://github.com/jtchilders/singularity_mpi_test_recipe)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

