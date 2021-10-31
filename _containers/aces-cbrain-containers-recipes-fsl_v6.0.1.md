---
id: 10203
name: "aces/cbrain-containers-recipes"
branch: "master"
tag: "fsl_v6.0.1"
commit: "88d2e5887934146d715ba36cb11456867f7247a4"
version: "9e51e712df0837cc5b4b61b09285f90e"
build_date: "2021-04-13T19:13:26.380Z"
size_mb: 13016
size: 5445525535
sif: "https://datasets.datalad.org/shub/aces/cbrain-containers-recipes/fsl_v6.0.1/2021-04-13-88d2e588-9e51e712/9e51e712df0837cc5b4b61b09285f90e.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/aces/cbrain-containers-recipes/fsl_v6.0.1/2021-04-13-88d2e588-9e51e712/
recipe: https://datasets.datalad.org/shub/aces/cbrain-containers-recipes/fsl_v6.0.1/2021-04-13-88d2e588-9e51e712/Singularity
collection: aces/cbrain-containers-recipes
---

# aces/cbrain-containers-recipes:fsl_v6.0.1

```bash
$ singularity pull shub://aces/cbrain-containers-recipes:fsl_v6.0.1
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:xenial-20190610  

############################################################
#                                                          #
# MCIN (McGill Centre for Integrative Neuroscience)        #
#                                                          #
# Singularity recipe for FSL 6.0.1 to build a container    #
# used in CBRAIN (https://github.com/aces/cbrain)          #
#                                                          #
############################################################
%labels
  Maintainer Shawn Brown 

%help
This container executes any fsl-core 6.0.1 command, and it contain all the fsl data too. 
For more information see FSL website: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki

%post
  apt-get update
  apt-get install -y python wget curl file build-essential tcl libpng12-dev libmng-dev bzip2 sudo perl
  curl -O https://fsl.fmrib.ox.ac.uk/fsldownloads/fslinstaller.py 
  chmod 755 fslinstaller.py 
  su -c "python ./fslinstaller.py -D -E -d /usr/local/fsl --fslversion 6.0.1"
  mkdir /validation-data
  cd /validation-data
  wget https://fsl.fmrib.ox.ac.uk/fslcourse/downloads/preCourse.tar.gz
  tar -xvzf preCourse.tar.gz
 
%environment
  export FSLDIR=/usr/local/fsl
  export FSLOUTPUTTYPE=NIFTI_GZ
  export PATH=/usr/local/fsl/bin:$PATH
  export FSLMULTIFILEQUIT=TRUE
  export POSSUMDIR=/usr/local/fsl
  export LD_LIBRARY_PATH=/usr/local/fsl/lib:$LD_LIBRARY_PATH
```

## Collection

 - Name: [aces/cbrain-containers-recipes](https://github.com/aces/cbrain-containers-recipes)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

