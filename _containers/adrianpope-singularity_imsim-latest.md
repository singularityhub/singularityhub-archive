---
id: 3720
name: "adrianpope/singularity_imsim"
branch: "master"
tag: "latest"
commit: "025b48b4b99f53634d926b1fbdcaf6847c33ed4c"
version: "7d94a9b380d4aae47e27ad9bcef14544"
build_date: "2018-08-11T19:03:39.659Z"
size_mb: 6481
size: 3072102431
sif: "https://datasets.datalad.org/shub/adrianpope/singularity_imsim/latest/2018-08-11-025b48b4-7d94a9b3/7d94a9b380d4aae47e27ad9bcef14544.simg"
url: https://datasets.datalad.org/shub/adrianpope/singularity_imsim/latest/2018-08-11-025b48b4-7d94a9b3/
recipe: https://datasets.datalad.org/shub/adrianpope/singularity_imsim/latest/2018-08-11-025b48b4-7d94a9b3/Singularity
collection: adrianpope/singularity_imsim
---

# adrianpope/singularity_imsim:latest

```bash
$ singularity pull shub://adrianpope/singularity_imsim:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: lsstdesc/stack-sims:w_2018_26-sims_2_9_0

%post
   set +e
   source scl_source enable devtoolset-6
   set -e
   source /opt/lsst/software/stack/loadLSST.bash
   setup lsst_sims
   mkdir /DC2
   cd /DC2
   git clone https://github.com/lsst/sims_GalSimInterface.git
   git clone https://github.com/LSSTDESC/imSim.git
   setup -r sims_GalSimInterface -j
   setup -r imSim -j
   cd sims_GalSimInterface
   set +e
   scons
   set -e
   cd ../imSim
   scons
   cd ..
   git clone https://github.com/LSSTDESC/ALCF_1.2i.git
   #set +e
   #py.test
   #set -e

%environment
   source /opt/lsst/software/stack/loadLSST.bash
   setup lsst_sims
   cd /DC2
   setup -r sims_GalSimInterface -j
   setup -r imSim -j
   cd
   export OMP_NUM_THREADS=1

%runscript
   exec python /DC2/ALCF_1.2i/scripts/run_imsim.py "$@"
```

## Collection

 - Name: [adrianpope/singularity_imsim](https://github.com/adrianpope/singularity_imsim)
 - License: [BSD 3-Clause "New" or "Revised" License](https://api.github.com/licenses/bsd-3-clause)

