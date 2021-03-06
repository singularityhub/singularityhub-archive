---
id: 7783
name: "switt4/surfAnalysis"
branch: "master"
tag: "0.0"
commit: "ab177e4ca94ec72731ab0e290f542afaab2086e3"
version: "e4d60d2a49405c56d47b05901eaef540"
build_date: "2019-03-15T23:31:17.259Z"
size_mb: 9602
size: 4183253023
sif: "https://datasets.datalad.org/shub/switt4/surfAnalysis/0.0/2019-03-15-ab177e4c-e4d60d2a/e4d60d2a49405c56d47b05901eaef540.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/switt4/surfAnalysis/0.0/2019-03-15-ab177e4c-e4d60d2a/
recipe: https://datasets.datalad.org/shub/switt4/surfAnalysis/0.0/2019-03-15-ab177e4c-e4d60d2a/Singularity
collection: switt4/surfAnalysis
---

# switt4/surfAnalysis:0.0

```bash
$ singularity pull shub://switt4/surfAnalysis:0.0
```

## Singularity Recipe

```singularity
# Generated by Neurodocker version 0.4.3-2-g01cdd22
# Timestamp: 2019-03-13 19:56:17 UTC
# 
# Thank you for using Neurodocker. If you discover any issues
# or ways to improve this software, please submit an issue or
# pull request on our GitHub repository:
# 
#     https://github.com/kaczmarj/neurodocker

Bootstrap: docker
From: debian:stretch

%setup
#mkdir $SINGULARITY_ROOTFS/src
#cp -Rv ./ src/

%post
export ND_ENTRYPOINT="/neurodocker/startup.sh"
apt-get update -qq
apt-get install -y -q --no-install-recommends \
    apt-utils \
    bzip2 \
    ca-certificates \
    curl \
    locales \
    unzip
apt-get clean
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen
dpkg-reconfigure --frontend=noninteractive locales
update-locale LANG="en_US.UTF-8"
chmod 777 /opt && chmod a+s /opt
mkdir -p /neurodocker
if [ ! -f "$ND_ENTRYPOINT" ]; then
  echo '#!/usr/bin/env bash' >> "$ND_ENTRYPOINT"
  echo 'set -e' >> "$ND_ENTRYPOINT"
  echo 'if [ -n "$1" ]; then "$@"; else /usr/bin/env bash; fi' >> "$ND_ENTRYPOINT";
fi
chmod -R 777 /neurodocker && chmod a+s /neurodocker

apt-get update -qq
apt-get install -y -q --no-install-recommends \
    bc \
    libgomp1 \
    libxmu6 \
    libxt6 \
    perl \
    tcsh
apt-get clean
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
echo "Downloading FreeSurfer ..."
mkdir -p /opt/freesurfer-6.0.0
curl -fsSL --retry 5 ftp://surfer.nmr.mgh.harvard.edu/pub/dist/freesurfer/6.0.0/freesurfer-Linux-centos6_x86_64-stable-pub-v6.0.0.tar.gz \
| tar -xz -C /opt/freesurfer-6.0.0 --strip-components 1 \
  --exclude='freesurfer/average/mult-comp-cor' \
  --exclude='freesurfer/lib/cuda' \
  --exclude='freesurfer/lib/qt' \
  --exclude='freesurfer/subjects/V1_average' \
  --exclude='freesurfer/subjects/bert' \
  --exclude='freesurfer/subjects/cvs_avg35' \
  --exclude='freesurfer/subjects/cvs_avg35_inMNI152' \
  --exclude='freesurfer/subjects/fsaverage3' \
  --exclude='freesurfer/subjects/fsaverage4' \
  --exclude='freesurfer/subjects/fsaverage5' \
  --exclude='freesurfer/subjects/fsaverage6' \
  --exclude='freesurfer/subjects/fsaverage_sym' \
  --exclude='freesurfer/trctrain'
sed -i '$isource "/opt/freesurfer-6.0.0/SetUpFreeSurfer.sh"' "$ND_ENTRYPOINT"

apt-get update -qq
apt-get install -y -q --no-install-recommends \
    bc \
    libncurses5 \
    libxext6 \
    libxmu6 \
    libxpm-dev \
    libxt6
apt-get clean
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
echo "Downloading MATLAB Compiler Runtime ..."
curl -fsSL --retry 5 -o /tmp/mcr.zip https://ssd.mathworks.com/supportfiles/downloads/R2018a/deployment_files/R2018a/installers/glnxa64/MCR_R2018a_glnxa64_installer.zip
unzip -q /tmp/mcr.zip -d /tmp/mcrtmp
/tmp/mcrtmp/install -destinationFolder /opt/matlabmcr-2018a -mode silent -agreeToLicense yes
rm -rf /tmp/*

apt-get update -qq
apt-get install -y -q --no-install-recommends \
    connectome-workbench
apt-get clean
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

echo '{
\n  "pkg_manager": "apt",
\n  "instructions": [
\n    [
\n      "base",
\n      "debian:stretch"
\n    ],
\n    [
\n      "_header",
\n      {
\n        "version": "generic",
\n        "method": "custom"
\n      }
\n    ],
\n    [
\n      "freesurfer",
\n      {
\n        "version": "6.0.0",
\n        "method": "binaries"
\n      }
\n    ],
\n    [
\n      "matlabmcr",
\n      {
\n        "version": "2018a",
\n        "method": "binaries"
\n      }
\n    ],
\n    [
\n      "install",
\n      [
\n        "connectome-workbench"
\n      ]
\n    ]
\n  ]
\n}' > /neurodocker/neurodocker_specs.json

#apt-get update -qq
#apt-get install -y -q --no-install-recommends \ 
#    libgiftiio-dev
#apt-get clean

apt-get update -qq
apt-get install -y -q --no-install-recommends \
    git
apt-get clean
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
git clone http://github.com/jdiedrichsen/dataframe
git clone https://github.com/gllmflndn/gifti
git clone https://github.com/switt4/surfAnalysis

%environment
export LANG="en_US.UTF-8"
export LC_ALL="en_US.UTF-8"
export ND_ENTRYPOINT="/neurodocker/startup.sh"
export FREESURFER_HOME="/opt/freesurfer-6.0.0"
export PATH="/opt/freesurfer-6.0.0/bin:$PATH"
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/lib/x86_64-linux-gnu:/opt/matlabmcr-2018a/v94/runtime/glnxa64:/opt/matlabmcr-2018a/v94/bin/glnxa64:/opt/matlabmcr-2018a/v94/sys/os/glnxa64:/opt/matlabmcr-2018a/v94/extern/bin/glnxa64"
export MATLABCMD="/opt/matlabmcr-2018a/v94/toolbox/matlab"

%runscript
/neurodocker/startup.sh "$@"
```

## Collection

 - Name: [switt4/surfAnalysis](https://github.com/switt4/surfAnalysis)
 - License: None

