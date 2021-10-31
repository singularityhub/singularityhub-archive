---
id: 7198
name: "jtchilders/singularity_mpi_test_recipe"
branch: "master"
tag: "dvs6_py36_mpi33_bzl16"
commit: "afc79d9a29f34dabf384d1fc733c69824546b6a5"
version: "10f7a4ec9bcfb6d67f292fa03998ace6"
build_date: "2019-02-13T20:23:54.933Z"
size_mb: 1717
size: 670502943
sif: "https://datasets.datalad.org/shub/jtchilders/singularity_mpi_test_recipe/dvs6_py36_mpi33_bzl16/2019-02-13-afc79d9a-10f7a4ec/10f7a4ec9bcfb6d67f292fa03998ace6.simg"
url: https://datasets.datalad.org/shub/jtchilders/singularity_mpi_test_recipe/dvs6_py36_mpi33_bzl16/2019-02-13-afc79d9a-10f7a4ec/
recipe: https://datasets.datalad.org/shub/jtchilders/singularity_mpi_test_recipe/dvs6_py36_mpi33_bzl16/2019-02-13-afc79d9a-10f7a4ec/Singularity
collection: jtchilders/singularity_mpi_test_recipe
---

# jtchilders/singularity_mpi_test_recipe:dvs6_py36_mpi33_bzl16

```bash
$ singularity pull shub://jtchilders/singularity_mpi_test_recipe:dvs6_py36_mpi33_bzl16
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: jtchilders/singularity_mpi_test_recipe:dvs6_py36_mpi

%post
   echo setting up devtoolset6
   # setup devtoolset6
   scl enable devtoolset-6 bash
   echo make alias for python 3.6
   # alias python3.6
   alias python="python3.6"
   
   export JAVA_VERSION=1.8

   echo checking out and building bazel version 0.16.0
   mkdir /bazel
   cd /bazel
   wget https://github.com/bazelbuild/bazel/releases/download/0.16.0/bazel-0.16.0-dist.zip
   mkdir bazel-0.16.0
   cd bazel-0.16.0
   mv ../bazel-0.16.0-dist.zip ./

   unzip bazel-0.16.0-dist.zip
   bash ./compile.sh
   echo done building bazel container
```

## Collection

 - Name: [jtchilders/singularity_mpi_test_recipe](https://github.com/jtchilders/singularity_mpi_test_recipe)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

