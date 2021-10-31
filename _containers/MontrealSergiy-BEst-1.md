---
id: 6208
name: "MontrealSergiy/BEst"
branch: "master"
tag: "1"
commit: "86d4f0a2de6669dd470da3d7e5fa9cf23e0748bd"
version: "8c3823aea923531de3e8252c18f969aa"
build_date: "2019-05-24T15:49:12.080Z"
size_mb: 5160
size: 2436993055
sif: "https://datasets.datalad.org/shub/MontrealSergiy/BEst/1/2019-05-24-86d4f0a2-8c3823ae/8c3823aea923531de3e8252c18f969aa.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/MontrealSergiy/BEst/1/2019-05-24-86d4f0a2-8c3823ae/
recipe: https://datasets.datalad.org/shub/MontrealSergiy/BEst/1/2019-05-24-86d4f0a2-8c3823ae/Singularity
collection: MontrealSergiy/BEst
---

# MontrealSergiy/BEst:1

```bash
$ singularity pull shub://MontrealSergiy/BEst:1
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
 The recipe does not involve the compilation and uses the executable(standalone) attached to github release
 
 To run the tool you need at least three matlab .mat files with recording, leading fields data, and adjacency matrix
 
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

wget https://gitlab.com/sergiyb/best-sing/raw/master/data_best_toolbox/GMEG.mat
wget https://gitlab.com/sergiyb/best-sing/raw/master/data_best_toolbox/MMEG.mat
wget https://gitlab.com/sergiyb/best-sing/raw/master/data_best_toolbox/vtcConn.mat
```

## Collection

 - Name: [MontrealSergiy/BEst](https://github.com/MontrealSergiy/BEst)
 - License: None

