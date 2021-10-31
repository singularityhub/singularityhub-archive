---
id: 8260
name: "jtchilders/singularity_mpi_test_recipe"
branch: "master"
tag: "dvs6_py36_mpi33_bzl241"
commit: "c65d8b89d17d0122b5b2157a33582677503ce63a"
version: "692d252ac45d3ddeccce23c6e6010b62"
build_date: "2019-04-06T03:03:32.271Z"
size_mb: 1880
size: 804610079
sif: "https://datasets.datalad.org/shub/jtchilders/singularity_mpi_test_recipe/dvs6_py36_mpi33_bzl241/2019-04-06-c65d8b89-692d252a/692d252ac45d3ddeccce23c6e6010b62.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jtchilders/singularity_mpi_test_recipe/dvs6_py36_mpi33_bzl241/2019-04-06-c65d8b89-692d252a/
recipe: https://datasets.datalad.org/shub/jtchilders/singularity_mpi_test_recipe/dvs6_py36_mpi33_bzl241/2019-04-06-c65d8b89-692d252a/Singularity
collection: jtchilders/singularity_mpi_test_recipe
---

# jtchilders/singularity_mpi_test_recipe:dvs6_py36_mpi33_bzl241

```bash
$ singularity pull shub://jtchilders/singularity_mpi_test_recipe:dvs6_py36_mpi33_bzl241
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
   BAZEL_VERSION=0.24.1


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

