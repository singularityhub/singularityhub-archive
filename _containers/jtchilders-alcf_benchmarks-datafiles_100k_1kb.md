---
id: 8105
name: "jtchilders/alcf_benchmarks"
branch: "master"
tag: "datafiles_100k_1kb"
commit: "be8db050605b23c08966032a11f7f35cf3096997"
version: "6b3e2d6a34caa9eab13b18ca3465de2e"
build_date: "2019-04-03T21:33:11.716Z"
size_mb: 1776
size: 536494111
sif: "https://datasets.datalad.org/shub/jtchilders/alcf_benchmarks/datafiles_100k_1kb/2019-04-03-be8db050-6b3e2d6a/6b3e2d6a34caa9eab13b18ca3465de2e.simg"
url: https://datasets.datalad.org/shub/jtchilders/alcf_benchmarks/datafiles_100k_1kb/2019-04-03-be8db050-6b3e2d6a/
recipe: https://datasets.datalad.org/shub/jtchilders/alcf_benchmarks/datafiles_100k_1kb/2019-04-03-be8db050-6b3e2d6a/Singularity
collection: jtchilders/alcf_benchmarks
---

# jtchilders/alcf_benchmarks:datafiles_100k_1kb

```bash
$ singularity pull shub://jtchilders/alcf_benchmarks:datafiles_100k_1kb
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: jtchilders/singularity_image_recipes:dvs6_py36_mpi33


%setup
   mkdir ${SINGULARITY_ROOTFS}/tests/
   cp create_datafiles.py ${SINGULARITY_ROOTFS}/tests/
   cp measure_meta_data_ops.py ${SINGULARITY_ROOTFS}/tests/

%post
   # setup devtoolset6
   scl enable devtoolset-6 bash

   pip3.6 install numpy
   
   cd /tests
   python3.6 ./create_datafiles.py -p datafiles -n 100000 -b 1024

%runscript
   python3.6 /tests/measure_meta_data_ops.py -p /tests/datafiles/
```

## Collection

 - Name: [jtchilders/alcf_benchmarks](https://github.com/jtchilders/alcf_benchmarks)
 - License: [MIT License](https://api.github.com/licenses/mit)

