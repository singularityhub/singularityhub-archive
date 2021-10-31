---
id: 7195
name: "jtchilders/singularity_mpi_test_recipe"
branch: "master"
tag: "dvs6_py36_basel16"
commit: "3b23cde19305de163a25a546676e2e557dc30b53"
version: "8efa73c46daf74e5d5d96bc7c0ab0a14"
build_date: "2019-02-13T20:23:54.946Z"
size_mb: 1001
size: 331821087
sif: "https://datasets.datalad.org/shub/jtchilders/singularity_mpi_test_recipe/dvs6_py36_basel16/2019-02-13-3b23cde1-8efa73c4/8efa73c46daf74e5d5d96bc7c0ab0a14.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jtchilders/singularity_mpi_test_recipe/dvs6_py36_basel16/2019-02-13-3b23cde1-8efa73c4/
recipe: https://datasets.datalad.org/shub/jtchilders/singularity_mpi_test_recipe/dvs6_py36_basel16/2019-02-13-3b23cde1-8efa73c4/Singularity
collection: jtchilders/singularity_mpi_test_recipe
---

# jtchilders/singularity_mpi_test_recipe:dvs6_py36_basel16

```bash
$ singularity pull shub://jtchilders/singularity_mpi_test_recipe:dvs6_py36_basel16
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: jtchilders/singularity_mpi_test_recipe:dvs6_py36

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

