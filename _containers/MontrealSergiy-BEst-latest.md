---
id: 6207
name: "MontrealSergiy/BEst"
branch: "master"
tag: "latest"
commit: "7d22155a6cf0ec164d888b8de6dfb142e3fdf561"
version: "c88f60bbaa6ca1fc869262c3022fe761"
build_date: "2019-08-12T14:26:59.332Z"
size_mb: 5160
size: 2436993055
sif: "https://datasets.datalad.org/shub/MontrealSergiy/BEst/latest/2019-08-12-7d22155a-c88f60bb/c88f60bbaa6ca1fc869262c3022fe761.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/MontrealSergiy/BEst/latest/2019-08-12-7d22155a-c88f60bb/
recipe: https://datasets.datalad.org/shub/MontrealSergiy/BEst/latest/2019-08-12-7d22155a-c88f60bb/Singularity
collection: MontrealSergiy/BEst
---

# MontrealSergiy/BEst:latest

```bash
$ singularity pull shub://MontrealSergiy/BEst:latest
```

## Singularity Recipe

```singularity
# BY USING THIS RECIPE YOU ACCEPT THE MATLAB RUNTIME LICENcES
# you need install matlab runtime in graphic mode to read the current licence agreement

Bootstrap: docker
From: ubuntu:16.04

%labels
MAINTAINER S.Boroday

%environment
    MCR_ROOT=/usr/local/MATLAB/MATLAB_Runtime/v95
    BEST_DIR=/usr/local/Multi_FunkIm_lab/BEst/application
    LAUNCH_BEST="$BEST_DIR $MCR_ROOT"
    export BEST_DIR 
    export MCR_ROOT
    export LAUNCH_BEST

%help

 to update container you need to create a release and attached installer package BEst_install of the tool BEst
 Presently installer is built locally manually using Matlap Compiler pluging GUI or in console with
     cd ~
     git clone https://gitlab.com/multifunkimlab/best 
     mcc -o BEst -W main:BEst -T link:exe -d ~/best/LAUNCH_ME_SCRIPT_BEst/for_redistribution -R '-logfile,mcc.log' -v ~/best/BEst.m -a ~/best/BEst.m -a ~/best/CODE -a ~/best/LAUNCH_ME_SCRIPT.m 
 
 
 To run you need at least three matlab .mat files with recording, leading fields data, and adjacency matrix
 
 Example
 
   singularity run recording.mat leadfield.mat adjacency.mat result.mat cMEM "MEG" "1 1.9" "0 0.9"  normalization adaptive clusteringMethod static mspWindow 10 mspThresholdMethod arbitrary mspThreshold 0 neighborhoodOrder 4 spatialSmoothing 0.6 activeMeanInit 2 activeProbaInit 3 lambdaInit 1 activeProbaThreshold 0 activeVarCoef 0.05 inactiveVarCoef 0 noiseCovMethod 2 optimMethod fminunc useParallel 0 
 
 Example inside container
   $BEST_DIR/run_BEst.sh $MCR_ROOT MMEG.mat GMEG.mat vtcConn.mat result.mat cMEM "MEG" "1 1.9" "0 0.9"  normalization adaptive clusteringMethod static mspWindow 10 mspThresholdMethod arbitrary mspThreshold 0 neighborhoodOrder 4 spatialSmoothing 0.6 activeMeanInit 2 activeProbaInit 3 lambdaInit 1 activeProbaThreshold 0 activeVarCoef 0.05 inactiveVarCoef 0 noiseCovMethod 2 optimMethod fminunc useParallel 0

...

%runscript

$BEST_DIR/run_BEst.sh $MCR_ROOT 

%post

mkdir -p DERIVATIVES
apt-get update
apt-get install unzip -y
apt-get install xorg -y --fix-missing
apt-get install wget -y --fix-missing
# chmod 0444 /DATA
chmod 777 /DERIVATIVES

# figure the latest release tag
export TAG=$(wget -qO- --header="Accept: application/json" https://github.com/MontrealSergiy/BEst/releases/latest| cut -d '"' -f 6)

#download tool instalation package file from the release
wget https://github.com/MontrealSergiy/BEst/releases/download/$TAG/BEst_.install

# an alternative download from gitlab
# wget https://gitlab.com/sergiyb/best-sing/raw/master/BEst_.install

chmod a+x BEst_.install
./BEst_.install -mode silent -agreeToLicense yes
rm BEst_.install
apt-get install python -y

# todo move to zenodo from gitlab?
wget https://gitlab.com/sergiyb/best-sing/raw/master/data_best_toolbox/GMEG.mat
wget https://gitlab.com/sergiyb/best-sing/raw/master/data_best_toolbox/MMEG.mat
wget https://gitlab.com/sergiyb/best-sing/raw/master/data_best_toolbox/vtcConn.mat
```

## Collection

 - Name: [MontrealSergiy/BEst](https://github.com/MontrealSergiy/BEst)
 - License: None

