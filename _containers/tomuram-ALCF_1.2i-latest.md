---
id: 4191
name: "tomuram/ALCF_1.2i"
branch: "master"
tag: "latest"
commit: "0d0b894825d6510a36d53126f48acc68cc0e2dc3"
version: "140d01dd2bf951cc323acb95b141a14e"
build_date: "2018-10-20T06:03:23.697Z"
size_mb: 6601
size: 3120554015
sif: "https://datasets.datalad.org/shub/tomuram/ALCF_1.2i/latest/2018-10-20-0d0b8948-140d01dd/140d01dd2bf951cc323acb95b141a14e.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/tomuram/ALCF_1.2i/latest/2018-10-20-0d0b8948-140d01dd/
recipe: https://datasets.datalad.org/shub/tomuram/ALCF_1.2i/latest/2018-10-20-0d0b8948-140d01dd/Singularity
collection: tomuram/ALCF_1.2i
---

# tomuram/ALCF_1.2i:latest

```bash
$ singularity pull shub://tomuram/ALCF_1.2i:latest
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
   git clone https://github.com/lsst/sims_photUtils.git
   git clone https://github.com/lsst/sims_skybrightness.git
   git clone https://github.com/lsst/sims_GalSimInterface.git
   git clone https://github.com/LSSTDESC/imSim.git
   git clone https://github.com/lsst/obs_lsstCam.git
   setup -r sims_photUtils -j
   setup -r sims_skybrightness -j
   setup -r sims_GalSimInterface -j
   setup -r imSim -j
   setup -r obs_lsstCam -j
   cd sims_photUtils
   git checkout ba5b942a9359e7eceea918e8663e6225cfb49dfc
   set +e
   scons
   set -e
   cd ../sims_skybrightness
   git checkout fdd58c7eb0414e89f5c7fa12eccf8809acabcf92
   set +e
   scons
   set -e
   cd ../sims_GalSimInterface
   git checkout u/jchiang/rmjarvis/simple_faint
   set +e
   scons
   set -e
   cd ../imSim
   git checkout dc2_run2.0_rc
   scons
   cd ../obs_lsstCam
   git checkout imsim-0.1.0
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
   setup -r obs_lsstCam -j
   cd
   export OMP_NUM_THREADS=1

%runscript
   exec python /DC2/ALCF_1.2i/scripts/run_imsim.py "$@"
```

## Collection

 - Name: [tomuram/ALCF_1.2i](https://github.com/tomuram/ALCF_1.2i)
 - License: None

