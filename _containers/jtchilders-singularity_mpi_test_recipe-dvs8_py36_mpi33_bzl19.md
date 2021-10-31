---
id: 8279
name: "jtchilders/singularity_mpi_test_recipe"
branch: "master"
tag: "dvs8_py36_mpi33_bzl19"
commit: "d6dd5aac62ff37f7b705732d27937be241082d7e"
version: "49a88cd0e9d95ebb7cd7561c8fa7d429"
build_date: "2019-04-08T19:28:20.986Z"
size_mb: 1823
size: 716328991
sif: "https://datasets.datalad.org/shub/jtchilders/singularity_mpi_test_recipe/dvs8_py36_mpi33_bzl19/2019-04-08-d6dd5aac-49a88cd0/49a88cd0e9d95ebb7cd7561c8fa7d429.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jtchilders/singularity_mpi_test_recipe/dvs8_py36_mpi33_bzl19/2019-04-08-d6dd5aac-49a88cd0/
recipe: https://datasets.datalad.org/shub/jtchilders/singularity_mpi_test_recipe/dvs8_py36_mpi33_bzl19/2019-04-08-d6dd5aac-49a88cd0/Singularity
collection: jtchilders/singularity_mpi_test_recipe
---

# jtchilders/singularity_mpi_test_recipe:dvs8_py36_mpi33_bzl19

```bash
$ singularity pull shub://jtchilders/singularity_mpi_test_recipe:dvs8_py36_mpi33_bzl19
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: jtchilders/singularity_mpi_test_recipe:dvs8_py36_mpi33

%post
   echo setting up devtoolset8
   # setup devtoolset8
   scl enable devtoolset-8 bash
   
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

