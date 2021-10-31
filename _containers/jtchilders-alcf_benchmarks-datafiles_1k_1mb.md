---
id: 8245
name: "jtchilders/alcf_benchmarks"
branch: "master"
tag: "datafiles_1k_1mb"
commit: "a569fc09aed0cc5c316f68748facb54378a09249"
version: "8b0fa1a20afda82465bec040600d0f4a"
build_date: "2019-04-05T20:03:05.624Z"
size_mb: 2385
size: 1479729183
sif: "https://datasets.datalad.org/shub/jtchilders/alcf_benchmarks/datafiles_1k_1mb/2019-04-05-a569fc09-8b0fa1a2/8b0fa1a20afda82465bec040600d0f4a.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jtchilders/alcf_benchmarks/datafiles_1k_1mb/2019-04-05-a569fc09-8b0fa1a2/
recipe: https://datasets.datalad.org/shub/jtchilders/alcf_benchmarks/datafiles_1k_1mb/2019-04-05-a569fc09-8b0fa1a2/Singularity
collection: jtchilders/alcf_benchmarks
---

# jtchilders/alcf_benchmarks:datafiles_1k_1mb

```bash
$ singularity pull shub://jtchilders/alcf_benchmarks:datafiles_1k_1mb
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
   python3.6 ./create_datafiles.py -p datafiles -n 1000 -b 1048576

%runscript
   python3.6 /tests/measure_meta_data_ops.py -p /tests/datafiles/
```

## Collection

 - Name: [jtchilders/alcf_benchmarks](https://github.com/jtchilders/alcf_benchmarks)
 - License: [MIT License](https://api.github.com/licenses/mit)

