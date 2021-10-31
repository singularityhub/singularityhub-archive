---
id: 7192
name: "jtchilders/singularity_mpi_test_recipe"
branch: "master"
tag: "dvs6_py36_basel"
commit: "b643455cfa86b2eb0cca51a816e9e0590edf7766"
version: "c3fbceb1fe1ec907d385567412c30b0f"
build_date: "2019-02-13T20:23:54.951Z"
size_mb: 1001
size: 331821087
sif: "https://datasets.datalad.org/shub/jtchilders/singularity_mpi_test_recipe/dvs6_py36_basel/2019-02-13-b643455c-c3fbceb1/c3fbceb1fe1ec907d385567412c30b0f.simg"
url: https://datasets.datalad.org/shub/jtchilders/singularity_mpi_test_recipe/dvs6_py36_basel/2019-02-13-b643455c-c3fbceb1/
recipe: https://datasets.datalad.org/shub/jtchilders/singularity_mpi_test_recipe/dvs6_py36_basel/2019-02-13-b643455c-c3fbceb1/Singularity
collection: jtchilders/singularity_mpi_test_recipe
---

# jtchilders/singularity_mpi_test_recipe:dvs6_py36_basel

```bash
$ singularity pull shub://jtchilders/singularity_mpi_test_recipe:dvs6_py36_basel
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

