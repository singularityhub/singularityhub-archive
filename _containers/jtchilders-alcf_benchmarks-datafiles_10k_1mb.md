---
id: 8106
name: "jtchilders/alcf_benchmarks"
branch: "master"
tag: "datafiles_10k_1mb"
commit: "be8db050605b23c08966032a11f7f35cf3096997"
version: "065db612f847f2410239b00bdf884a26"
build_date: "2019-04-03T21:33:11.709Z"
size_mb: 11421
size: 10919202847
sif: "https://datasets.datalad.org/shub/jtchilders/alcf_benchmarks/datafiles_10k_1mb/2019-04-03-be8db050-065db612/065db612f847f2410239b00bdf884a26.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jtchilders/alcf_benchmarks/datafiles_10k_1mb/2019-04-03-be8db050-065db612/
recipe: https://datasets.datalad.org/shub/jtchilders/alcf_benchmarks/datafiles_10k_1mb/2019-04-03-be8db050-065db612/Singularity
collection: jtchilders/alcf_benchmarks
---

# jtchilders/alcf_benchmarks:datafiles_10k_1mb

```bash
$ singularity pull shub://jtchilders/alcf_benchmarks:datafiles_10k_1mb
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

