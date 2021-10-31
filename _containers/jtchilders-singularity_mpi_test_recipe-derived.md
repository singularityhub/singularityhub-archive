---
id: 3214
name: "jtchilders/singularity_mpi_test_recipe"
branch: "master"
tag: "derived"
commit: "ea686b87780c342f065e0dbeab4299b7f4688300"
version: "163116615de2a6577a1eebdd5906b8ee"
build_date: "2018-06-20T02:46:53.567Z"
size_mb: 774
size: 224743455
sif: "https://datasets.datalad.org/shub/jtchilders/singularity_mpi_test_recipe/derived/2018-06-20-ea686b87-16311661/163116615de2a6577a1eebdd5906b8ee.simg"
url: https://datasets.datalad.org/shub/jtchilders/singularity_mpi_test_recipe/derived/2018-06-20-ea686b87-16311661/
recipe: https://datasets.datalad.org/shub/jtchilders/singularity_mpi_test_recipe/derived/2018-06-20-ea686b87-16311661/Singularity
collection: jtchilders/singularity_mpi_test_recipe
---

# jtchilders/singularity_mpi_test_recipe:derived

```bash
$ singularity pull shub://jtchilders/singularity_mpi_test_recipe:derived
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: jtchilders/singularity_mpi_test_recipe:latest

%setup
   # make directory for test MPI program
   mkdir ${SINGULARITY_ROOTFS}/uselocalmpi
   cp pi.c ${SINGULARITY_ROOTFS}/uselocalmpi/

%post
   # add to local environment to build pi.c
   export PATH=$PATH:/mpich/install/bin
   export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/mpich/install/lib
   env | sort
   cd /uselocalmpi
   mpicc -o pi -fPIC pi.c

%runscript
   /uselocalmpi/pi
```

## Collection

 - Name: [jtchilders/singularity_mpi_test_recipe](https://github.com/jtchilders/singularity_mpi_test_recipe)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

