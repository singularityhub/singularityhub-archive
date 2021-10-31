---
id: 4209
name: "LSSTDESC/drp-stack"
branch: "master"
tag: "imsim"
commit: "4ed30f6ad9b36e704519abf9757faa1696997e3d"
version: "d847727157c423d1f6e8abca7405e133"
build_date: "2018-08-28T16:37:58.999Z"
size_mb: 6583
size: 3128414239
sif: "https://datasets.datalad.org/shub/LSSTDESC/drp-stack/imsim/2018-08-28-4ed30f6a-d8477271/d847727157c423d1f6e8abca7405e133.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/LSSTDESC/drp-stack/imsim/2018-08-28-4ed30f6a-d8477271/
recipe: https://datasets.datalad.org/shub/LSSTDESC/drp-stack/imsim/2018-08-28-4ed30f6a-d8477271/Singularity
collection: LSSTDESC/drp-stack
---

# LSSTDESC/drp-stack:imsim

```bash
$ singularity pull shub://LSSTDESC/drp-stack:imsim
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: lsstdesc/stack-sims:w_2018_26-sims_2_9_0
# imSim Singularity image which includes write_image_amp_file.py 
# desc_sim_utils

%post
   set +e
   yum install -y time
   source scl_source enable devtoolset-6
   set -e
   source /opt/lsst/software/stack/loadLSST.bash
   setup lsst_sims
   mkdir /DC2
   cd /DC2
   git clone https://github.com/LSSTDESC/imSim.git
   cd imSim
   git checkout u/jchiang/fix_raw_file_packager
   setup -r . -j
   scons
   cd ..
   git clone https://github.com/LSSTDESC/desc_sim_utils
   cd desc_sim_utils
   git checkout u/jchiang/imsim_calib_scripts
   setup -r . -j
   scons
   cd ../..
 

%environment
   source /opt/lsst/software/stack/loadLSST.bash
   setup lsst_sims
   cd /DC2
   setup -r imSim -j
   setup -r desc_sim_utils -j
   cd
   export OMP_NUM_THREADS=1

#%runscript
#   exec python /DC2/ALCF_1.2i/scripts/run_imsim.py "$@"
```

## Collection

 - Name: [LSSTDESC/drp-stack](https://github.com/LSSTDESC/drp-stack)
 - License: [BSD 3-Clause "New" or "Revised" License](https://api.github.com/licenses/bsd-3-clause)

