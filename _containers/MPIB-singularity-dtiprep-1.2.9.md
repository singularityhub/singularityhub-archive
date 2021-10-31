---
id: 1984
name: "MPIB/singularity-dtiprep"
branch: "master"
tag: "1.2.9"
commit: "ee4462e1074a2f68d54f337dbc6a2c9622a70b68"
version: "3eb451be71bcf4583a0d3518a40cfb80"
build_date: "2019-09-13T17:03:45.911Z"
size_mb: 4702
size: 2053201951
sif: "https://datasets.datalad.org/shub/MPIB/singularity-dtiprep/1.2.9/2019-09-13-ee4462e1-3eb451be/3eb451be71bcf4583a0d3518a40cfb80.simg"
url: https://datasets.datalad.org/shub/MPIB/singularity-dtiprep/1.2.9/2019-09-13-ee4462e1-3eb451be/
recipe: https://datasets.datalad.org/shub/MPIB/singularity-dtiprep/1.2.9/2019-09-13-ee4462e1-3eb451be/Singularity
collection: MPIB/singularity-dtiprep
---

# MPIB/singularity-dtiprep:1.2.9

```bash
$ singularity pull shub://MPIB/singularity-dtiprep:1.2.9
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
MirrorURL: http://archive.ubuntu.com/ubuntu/
OSVersion: xenial

%help

Contains BRAINSTools and DTIProcess from DTIPrep version 1.2.9

%post

export BUILD_SOFTWARE="git subversion cmake"
export CONTAINER_SOFTWARE="g++ libglu1-mesa lib32z1-dev libxt-dev qt4-dev-tools"

export DTIPREP_VERSION="DTIPrep1.2.9"
#export DTIPREP_VERSION="497b9782b9c27be172e9df7fb1a800c35cdeff47"

export WORKING_DIRECTORY=/opt
export DTIPREP_BUILD_DIRECTORY=$WORKING_DIRECTORY/dtiprep
export DTIPREP_REPO_NAME="DTIPrep"
export DTIPREP_CLONE_DIRECTORY=$WORKING_DIRECTORY/$DTIPREP_REPO_NAME
export GITHUB_REPO="https://github.com/NIRALUser/DTIPrep.git"

apt-get update
apt-get install $BUILD_SOFTWARE $CONTAINER_SOFTWARE -y


# Clone repository.
cd $WORKING_DIRECTORY
git clone $GITHUB_REPO
cd $DTIPREP_CLONE_DIRECTORY
#get desired version
git checkout $DTIPREP_VERSION

# Set up build directory
mkdir $DTIPREP_BUILD_DIRECTORY
cd $DTIPREP_BUILD_DIRECTORY
mkdir bin

# Build DTIProcess and BRAINSTools
cmake  $DTIPREP_CLONE_DIRECTORY
make BRAINSTools
make DTIProcess

echo "export PATH=${DTIPREP_BUILD_DIRECTORY}/bin:$PATH" >> $SINGULARITY_ENVIRONMENT


# Removing installation overhead.
 
cd
rm -rf $DTIPREP_CLONE_DIRECTORY
rm -rf /tmp/*
apt-get purge $BUILD_SOFTWARE -y
apt-get autoclean -y
apt-get autoremove -y
rm -rf /var/lib/apt/lists/*
```

## Collection

 - Name: [MPIB/singularity-dtiprep](https://github.com/MPIB/singularity-dtiprep)
 - License: None

