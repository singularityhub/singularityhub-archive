---
id: 8280
name: "jtchilders/alcf_benchmarks"
branch: "master"
tag: "datafiles_10k_1kb"
commit: "33ab90ff97504f1be0db12655e319743024c83b1"
version: "9c47273b66821e50ccb961b1aac0bea5"
build_date: "2019-04-08T19:28:24.218Z"
size_mb: 1421
size: 441462815
sif: "https://datasets.datalad.org/shub/jtchilders/alcf_benchmarks/datafiles_10k_1kb/2019-04-08-33ab90ff-9c47273b/9c47273b66821e50ccb961b1aac0bea5.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jtchilders/alcf_benchmarks/datafiles_10k_1kb/2019-04-08-33ab90ff-9c47273b/
recipe: https://datasets.datalad.org/shub/jtchilders/alcf_benchmarks/datafiles_10k_1kb/2019-04-08-33ab90ff-9c47273b/Singularity
collection: jtchilders/alcf_benchmarks
---

# jtchilders/alcf_benchmarks:datafiles_10k_1kb

```bash
$ singularity pull shub://jtchilders/alcf_benchmarks:datafiles_10k_1kb
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
   python3.6 ./create_datafiles.py -p datafiles -n 10000 -b 1024

%runscript
   python3.6 /tests/measure_meta_data_ops.py -p /tests/datafiles/
```

## Collection

 - Name: [jtchilders/alcf_benchmarks](https://github.com/jtchilders/alcf_benchmarks)
 - License: [MIT License](https://api.github.com/licenses/mit)

