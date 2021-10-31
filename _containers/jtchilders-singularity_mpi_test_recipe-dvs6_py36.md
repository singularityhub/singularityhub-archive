---
id: 7191
name: "jtchilders/singularity_mpi_test_recipe"
branch: "master"
tag: "dvs6_py36"
commit: "083813faeb1c44925be0d2e9e3e8a18677c09b0a"
version: "f6a511fae087f760b7c62b3ecb971633"
build_date: "2019-02-13T20:23:54.957Z"
size_mb: 1001
size: 331821087
sif: "https://datasets.datalad.org/shub/jtchilders/singularity_mpi_test_recipe/dvs6_py36/2019-02-13-083813fa-f6a511fa/f6a511fae087f760b7c62b3ecb971633.simg"
url: https://datasets.datalad.org/shub/jtchilders/singularity_mpi_test_recipe/dvs6_py36/2019-02-13-083813fa-f6a511fa/
recipe: https://datasets.datalad.org/shub/jtchilders/singularity_mpi_test_recipe/dvs6_py36/2019-02-13-083813fa-f6a511fa/Singularity
collection: jtchilders/singularity_mpi_test_recipe
---

# jtchilders/singularity_mpi_test_recipe:dvs6_py36

```bash
$ singularity pull shub://jtchilders/singularity_mpi_test_recipe:dvs6_py36
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: jtchilders/singularity_mpi_test_recipe:devtoolset6

%post
   # install python36
   yum install -y https://centos7.iuscommunity.org/ius-release.rpm
   yum update -y
   yum install -y python36u python36u-libs python36u-devel python36u-pip
```

## Collection

 - Name: [jtchilders/singularity_mpi_test_recipe](https://github.com/jtchilders/singularity_mpi_test_recipe)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

