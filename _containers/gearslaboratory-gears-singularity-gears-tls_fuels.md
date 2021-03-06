---
id: 9929
name: "gearslaboratory/gears-singularity"
branch: "master"
tag: "gears-tls_fuels"
commit: "ef5f2fbfda9ecb23784354d40d58004a6b6c2314"
version: "e153b1b8a5912f9d4ffba1f8021197a0"
build_date: "2019-06-25T20:20:54.187Z"
size_mb: 6136
size: 2307194911
sif: "https://datasets.datalad.org/shub/gearslaboratory/gears-singularity/gears-tls_fuels/2019-06-25-ef5f2fbf-e153b1b8/e153b1b8a5912f9d4ffba1f8021197a0.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/gearslaboratory/gears-singularity/gears-tls_fuels/2019-06-25-ef5f2fbf-e153b1b8/
recipe: https://datasets.datalad.org/shub/gearslaboratory/gears-singularity/gears-tls_fuels/2019-06-25-ef5f2fbf-e153b1b8/Singularity
collection: gearslaboratory/gears-singularity
---

# gearslaboratory/gears-singularity:gears-tls_fuels

```bash
$ singularity pull shub://gearslaboratory/gears-singularity:gears-tls_fuels
```

## Singularity Recipe

```singularity
BootStrap: debootstrap
OSVersion: bionic
MirrorURL: http://archive.ubuntu.com/ubuntu/
Include: bash

####### GEARS Lab General-use Singularity image.  Contains R, GDAL, GRASS, and other code...

%environment
    PATH=$PATH:/APPS/LAStools/bin/
    export PATH

%post
  apt-get -y update && apt-get install -y --no-install-recommends apt-utils
  apt-get -y clean && apt-get -y update && apt-get install -y locales && locale-gen en_US.UTF-8
	
  # Add to sources list:
  sed -i 's/main/main restricted universe/g' /etc/apt/sources.list
  apt-get -y update

  # Latest R
  apt-get install -y software-properties-common
  apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
  add-apt-repository -y 'deb https://cloud.r-project.org/bin/linux/ubuntu bionic-cran35/'
  # apt-key -y adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9
  # apt-get -y update
  # apt-get install -y r-base r-base-core r-recommended
  
  # Install R, openmpi, misc. utilities:
  apt-get install -y libopenblas-dev r-base-core r-base-dev libcurl4-openssl-dev \
  	libopenmpi-dev openmpi-bin openmpi-common openmpi-doc openssh-client openssh-server \
  	libssh-dev wget vim git nano git cmake gfortran g++ curl wget python autoconf \
  	bzip2 libtool libtool-bin libxml2-dev unzip

  # GRASS GIS and QGIS:
  apt-get install -y software-properties-common
  wget -O - https://qgis.org/downloads/qgis-2017.gpg.key | gpg --import
  gpg --export --armor CAEB3DC3BDF7FB45 | apt-key add -
  apt-add-repository 'deb https://qgis.org/debian bionic main'  
#  add-apt-repository ppa:ubuntugis/ppa
  apt-get update
  apt-get install -y python3-qgis
  apt-get install -y grass libgdal-dev libproj-dev python-gdal python3-gdal
  apt-get install -y qgis python-qgis qgis-plugin-grass

  # Miscellaneous other installs.
  # libudunits2-dev is needed for the package "sf"
  apt-get install -y libudunits2-dev
  
  # SVN:
  apt-get install -y subversion

  # Clean up the installations...
  apt-get clean

  # wine:
  mkdir -p /APPS /PROFILES
  chmod 0777 /APPS /PROFILES
  dpkg --add-architecture i386
  wget -nc https://dl.winehq.org/wine-builds/winehq.key
  apt-key add winehq.key
  apt-add-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ bionic main'
  apt-get update
  apt-get install -y --install-recommends winehq-stable
  apt-get clean
  
  # computree
  git clone https://github.com/gearslaboratory/gears-singularity.git
  cd gears-singularity/additional_data/computree
  unzip computree_v5.0.184e.zip
  mv computree_v5.0.184e /APPS/
  # TODO: shortcut

  # lastools
  cd ~
  wget https://lastools.github.io/download/LAStools.zip
  unzip LAStools.zip
  mv LAStools /APPS/
  
# Lastools shortcuts:  
for filename in /APPS/LAStools/bin/*.exe; do
basename=`basename $filename .exe`
  echo '#!/bin/bash
WINEDEBUG=-all wine '$filename '"$@"' >> /usr/local/bin/$basename
chmod 755 /usr/local/bin/$basename
done
  
# PDAL via conda
cd /tmp
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -bfp /usr/local
ln -s /usr/local/etc/profile.d/conda.sh /etc/profile.d/conda.sh
# source /etc/profile.d/conda.sh
# conda update -n base -c defaults conda
conda create --yes --name pdal --channel conda-forge pdal
  
### SLURM FROM WITHIN THE CONTAINER VIA SSH, PRONGHORN ONLY

  echo '#!/bin/bash
ssh $USER@$HOSTNAME sacct "$@"' >> /usr/local/bin/sacct
  
  echo '#!/bin/bash
ssh $USER@$HOSTNAME sacctmgr "$@"' >> /usr/local/bin/sacctmgr
  
  echo '#!/bin/bash
ssh $USER@$HOSTNAME salloc "$@"' >> /usr/local/bin/salloc
    
  echo '#!/bin/bash
ssh $USER@$HOSTNAME sattach "$@"' >> /usr/local/bin/sattach
    
  echo '#!/bin/bash
ssh $USER@$HOSTNAME sbatch "$@"' >> /usr/local/bin/sbatch
    
  echo '#!/bin/bash
ssh $USER@$HOSTNAME sbcast "$@"' >> /usr/local/bin/sbcast
  
  echo '#!/bin/bash
ssh $USER@$HOSTNAME scancel "$@"' >> /usr/local/bin/scancel
  
  echo '#!/bin/bash
ssh $USER@$HOSTNAME scontrol "$@"' >> /usr/local/bin/scontrol
  
  echo '#!/bin/bash
ssh $USER@$HOSTNAME sdiag "$@"' >> /usr/local/bin/sdiag
  
  echo '#!/bin/bash
ssh $USER@$HOSTNAME sgather "$@"' >> /usr/local/bin/sgather
  
  echo '#!/bin/bash
ssh $USER@$HOSTNAME sinfo "$@"' >> /usr/local/bin/sinfo
  
  echo '#!/bin/bash
ssh $USER@$HOSTNAME smap "$@"' >> /usr/local/bin/smap
  
  echo '#!/bin/bash
ssh $USER@$HOSTNAME sprio "$@"' >> /usr/local/bin/sprio
  
  echo '#!/bin/bash
ssh $USER@$HOSTNAME squeue "$@"' >> /usr/local/bin/squeue
  
  echo '#!/bin/bash
ssh $USER@$HOSTNAME sreport "$@"' >> /usr/local/bin/sreport
  
  echo '#!/bin/bash
ssh $USER@$HOSTNAME srun "$@"' >> /usr/local/bin/srun
  
  echo '#!/bin/bash
ssh $USER@$HOSTNAME sshare "$@"' >> /usr/local/bin/sshare
  
  echo '#!/bin/bash
ssh $USER@$HOSTNAME sstat "$@"' >> /usr/local/bin/sstat
      
  echo '#!/bin/bash
ssh $USER@$HOSTNAME strigger "$@"' >> /usr/local/bin/strigger
  
  echo '#!/bin/bash
ssh $USER@$HOSTNAME sview "$@"' >> /usr/local/bin/sview
  
  cd /usr/local/bin
  chmod 755 sacct salloc sbatch scancel sdiag sinfo sprio sreport sshare strigger sacctmgr sattach sbcast scontrol sgather smap squeue srun sstat sview    
  

%runscript
   conda activate pdal
```

## Collection

 - Name: [gearslaboratory/gears-singularity](https://github.com/gearslaboratory/gears-singularity)
 - License: None

