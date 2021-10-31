---
id: 4109
name: "LSSTDESC/drp-stack"
branch: "master"
tag: "drp"
commit: "d368735f82bd72fe487c299d5f7b75fe32c8ac0b"
version: "70a266fce3f1704bf290e228bbe69b5b"
build_date: "2018-09-14T11:36:51.601Z"
size_mb: 5105
size: 1837293599
sif: "https://datasets.datalad.org/shub/LSSTDESC/drp-stack/drp/2018-09-14-d368735f-70a266fc/70a266fce3f1704bf290e228bbe69b5b.simg"
url: https://datasets.datalad.org/shub/LSSTDESC/drp-stack/drp/2018-09-14-d368735f-70a266fc/
recipe: https://datasets.datalad.org/shub/LSSTDESC/drp-stack/drp/2018-09-14-d368735f-70a266fc/Singularity
collection: LSSTDESC/drp-stack
---

# LSSTDESC/drp-stack:drp

```bash
$ singularity pull shub://LSSTDESC/drp-stack:drp
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: lsstsqre/centos:7-stack-lsst_distrib-w_2018_35
# DRP Singularity Image

%post
   set +e
   yum install -y time
   source scl_source enable devtoolset-6
   set -e
   source /opt/lsst/software/stack/loadLSST.bash
   setup lsst_distrib
   mkdir /DC2
   cd /DC2
   git clone https://github.com/lsst/obs_lsstCam.git
   cd obs_lsstCam
   git checkout dc2/run1.2i
   setup -r . -j
   scons
   cd ..
   git clone https://github.com/LSSTDESC/ImageProcessingPipelines.git
   cd ImageProcessingPipelines
   git checkout u/heather999/dev
   cd ../..
 

%environment
   source /opt/lsst/software/stack/loadLSST.bash
   setup lsst_distrib
   cd /DC2
   setup -r obs_lsstCam -j
   cd
   export OMP_NUM_THREADS=1
```

## Collection

 - Name: [LSSTDESC/drp-stack](https://github.com/LSSTDESC/drp-stack)
 - License: [BSD 3-Clause "New" or "Revised" License](https://api.github.com/licenses/bsd-3-clause)

