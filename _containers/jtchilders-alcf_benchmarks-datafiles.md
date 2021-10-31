---
id: 7949
name: "jtchilders/alcf_benchmarks"
branch: "master"
tag: "datafiles"
commit: "594efa0b069611cb5301b28750f243089639664a"
version: "2a52c3c8db310aa5ce67fef87d077111"
build_date: "2019-03-29T19:18:15.841Z"
size_mb: 11421
size: 10919202847
sif: "https://datasets.datalad.org/shub/jtchilders/alcf_benchmarks/datafiles/2019-03-29-594efa0b-2a52c3c8/2a52c3c8db310aa5ce67fef87d077111.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jtchilders/alcf_benchmarks/datafiles/2019-03-29-594efa0b-2a52c3c8/
recipe: https://datasets.datalad.org/shub/jtchilders/alcf_benchmarks/datafiles/2019-03-29-594efa0b-2a52c3c8/Singularity
collection: jtchilders/alcf_benchmarks
---

# jtchilders/alcf_benchmarks:datafiles

```bash
$ singularity pull shub://jtchilders/alcf_benchmarks:datafiles
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
   python3.6 ./create_datafiles.py -p datafiles -n 10000 -b 1048576

%runscript
   python3.6 /tests/measure_meta_data_ops.py -p /tests/datafiles/
```

## Collection

 - Name: [jtchilders/alcf_benchmarks](https://github.com/jtchilders/alcf_benchmarks)
 - License: [MIT License](https://api.github.com/licenses/mit)

