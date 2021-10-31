---
id: 5080
name: "jtchilders/singularity_mpi_test_recipe"
branch: "master"
tag: "latest"
commit: "cab05a30e2eba4c2544dda8720f449426d50ff1b"
version: "e94c4c402da7e7029d8172216480e591"
build_date: "2020-05-06T07:48:38.320Z"
size_mb: 3789
size: 1146343455
sif: "https://datasets.datalad.org/shub/jtchilders/singularity_mpi_test_recipe/latest/2020-05-06-cab05a30-e94c4c40/e94c4c402da7e7029d8172216480e591.simg"
url: https://datasets.datalad.org/shub/jtchilders/singularity_mpi_test_recipe/latest/2020-05-06-cab05a30-e94c4c40/
recipe: https://datasets.datalad.org/shub/jtchilders/singularity_mpi_test_recipe/latest/2020-05-06-cab05a30-e94c4c40/Singularity
collection: jtchilders/singularity_mpi_test_recipe
---

# jtchilders/singularity_mpi_test_recipe:latest

```bash
$ singularity pull shub://jtchilders/singularity_mpi_test_recipe:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: intelpython/intelpython3_full:latest

%setup
   # make directory for test MPI program
   # mkdir ${SINGULARITY_ROOTFS}/uselocalmpi
   # cp pi.c ${SINGULARITY_ROOTFS}/uselocalmpi/

%post
   # add to local environment to build pi.c
   # export PATH=$PATH:/mpich/install/bin
   # export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/mpich/install/lib
   # env | sort
   # cd /uselocalmpi
   # mpicc -o pi -fPIC pi.c
   export PATH=/opt/conda/bin:$PATH
   conda install -y keras
```

## Collection

 - Name: [jtchilders/singularity_mpi_test_recipe](https://github.com/jtchilders/singularity_mpi_test_recipe)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

