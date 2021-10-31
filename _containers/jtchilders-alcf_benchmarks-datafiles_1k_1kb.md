---
id: 8246
name: "jtchilders/alcf_benchmarks"
branch: "master"
tag: "datafiles_1k_1kb"
commit: "415b79c3e8f3f5ecb95cd9a5460952b1cea665fc"
version: "290ebb6487f56f4fa7193246866b0b47"
build_date: "2019-04-05T20:03:05.618Z"
size_mb: 1385
size: 431960095
sif: "https://datasets.datalad.org/shub/jtchilders/alcf_benchmarks/datafiles_1k_1kb/2019-04-05-415b79c3-290ebb64/290ebb6487f56f4fa7193246866b0b47.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jtchilders/alcf_benchmarks/datafiles_1k_1kb/2019-04-05-415b79c3-290ebb64/
recipe: https://datasets.datalad.org/shub/jtchilders/alcf_benchmarks/datafiles_1k_1kb/2019-04-05-415b79c3-290ebb64/Singularity
collection: jtchilders/alcf_benchmarks
---

# jtchilders/alcf_benchmarks:datafiles_1k_1kb

```bash
$ singularity pull shub://jtchilders/alcf_benchmarks:datafiles_1k_1kb
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
   python3.6 ./create_datafiles.py -p datafiles -n 1000 -b 1024

%runscript
   python3.6 /tests/measure_meta_data_ops.py -p /tests/datafiles/
```

## Collection

 - Name: [jtchilders/alcf_benchmarks](https://github.com/jtchilders/alcf_benchmarks)
 - License: [MIT License](https://api.github.com/licenses/mit)

