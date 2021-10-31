---
id: 7210
name: "jtchilders/singularity_mpi_test_recipe"
branch: "master"
tag: "dvs6_py36_mpi33_bzl19"
commit: "dd6591cbc569b38777dfd7d74570cd1231c31efb"
version: "9c1016012af6e9b5c4f4ade0547f2642"
build_date: "2019-02-14T08:45:01.831Z"
size_mb: 1757
size: 680423455
sif: "https://datasets.datalad.org/shub/jtchilders/singularity_mpi_test_recipe/dvs6_py36_mpi33_bzl19/2019-02-14-dd6591cb-9c101601/9c1016012af6e9b5c4f4ade0547f2642.simg"
url: https://datasets.datalad.org/shub/jtchilders/singularity_mpi_test_recipe/dvs6_py36_mpi33_bzl19/2019-02-14-dd6591cb-9c101601/
recipe: https://datasets.datalad.org/shub/jtchilders/singularity_mpi_test_recipe/dvs6_py36_mpi33_bzl19/2019-02-14-dd6591cb-9c101601/Singularity
collection: jtchilders/singularity_mpi_test_recipe
---

# jtchilders/singularity_mpi_test_recipe:dvs6_py36_mpi33_bzl19

```bash
$ singularity pull shub://jtchilders/singularity_mpi_test_recipe:dvs6_py36_mpi33_bzl19
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: jtchilders/singularity_mpi_test_recipe:dvs6_py36_mpi

%post
   echo setting up devtoolset6
   # setup devtoolset6
   scl enable devtoolset-6 bash
   
   export JAVA_VERSION=1.8
   BAZEL_VERSION=0.19.0


   echo checking out and building bazel version $BAZEL_VERSION
   mkdir /bazel
   cd /bazel
   wget https://github.com/bazelbuild/bazel/releases/download/$BAZEL_VERSION/bazel-$BAZEL_VERSION-dist.zip
   mkdir bazel-$BAZEL_VERSION
   cd bazel-$BAZEL_VERSION
   unzip ../bazel-$BAZEL_VERSION-dist.zip
   ./compile.sh
   echo done building bazel container
```

## Collection

 - Name: [jtchilders/singularity_mpi_test_recipe](https://github.com/jtchilders/singularity_mpi_test_recipe)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

