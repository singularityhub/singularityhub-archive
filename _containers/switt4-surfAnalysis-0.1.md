---
id: 7830
name: "switt4/surfAnalysis"
branch: "master"
tag: "0.1"
commit: "12991631de647352a624c15467a675aeceb0615c"
version: "2da73f96102317037cdc6b15b0849886"
build_date: "2019-03-20T08:24:17.205Z"
size_mb: 9575
size: 4171350047
sif: "https://datasets.datalad.org/shub/switt4/surfAnalysis/0.1/2019-03-20-12991631-2da73f96/2da73f96102317037cdc6b15b0849886.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/switt4/surfAnalysis/0.1/2019-03-20-12991631-2da73f96/
recipe: https://datasets.datalad.org/shub/switt4/surfAnalysis/0.1/2019-03-20-12991631-2da73f96/Singularity
collection: switt4/surfAnalysis
---

# switt4/surfAnalysis:0.1

```bash
$ singularity pull shub://switt4/surfAnalysis:0.1
```

## Singularity Recipe

```singularity
# Generated by Neurodocker version 0.4.3-2-g01cdd22
# Timestamp: 2019-03-18 19:17:11 UTC
# 
# Thank you for using Neurodocker. If you discover any issues
# or ways to improve this software, please submit an issue or
# pull request on our GitHub repository:
# 
#     https://github.com/kaczmarj/neurodocker

Bootstrap: docker
From: debian:stretch

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
mkdir -p /opt/freesurfer-6.0.1
curl -fsSL --retry 5 ftp://surfer.nmr.mgh.harvard.edu/pub/dist/freesurfer/6.0.1/freesurfer-Linux-centos6_x86_64-stable-pub-v6.0.1.tar.gz \
| tar -xz -C /opt/freesurfer-6.0.1 --strip-components 1 \
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
sed -i '$isource "/opt/freesurfer-6.0.1/SetUpFreeSurfer.sh"' "$ND_ENTRYPOINT"

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
\n        "version": "6.0.1",
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
\n  ]
\n}' > /neurodocker/neurodocker_specs.json

apt-get update -qq
apt-get install -y -q --no-install-recommends \
    git
apt-get clean
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
git clone http://github.com/jdiedrichsen/dataframe
git clone https://github.com/gllmflndn/gifti
git clone https://github.com/switt4/surfAnalysis

apt-get update -qq
apt-get install -y -q --no-install-recommends \
    wget
apt-get clean
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

apt-get update -qq
apt-get install -y -q --no-install-recommends \
    libfreetype6 \
    libglu1-mesa \
    libssl.dev \
    libglib2.0-0 \
    zlib1g
apt-get clean
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

wget https://www.dropbox.com/s/38gghuq2w7hl7pe/freesurfer_license
mv freesurfer_license /opt/freesurfer-6.0.1/license.txt

#wget https://ftp.humanconnectome.org/workbench/workbench-linux64-v1.3.2.zip
#unzip workbench-linux64-v1.3.2.zip
#mv workbench opt/
#rm -f workbench-linux64-v1.3.2.zip

#wget https://debian.pkgs.org/9/neurodebian-main-amd64/connectome-workbench_1.3.2-2~nd90+1_amd64.deb
#dpkg -i connectome-workbench_1.3.2-2~nd90+1_amd64.deb
#rm -f connectome-workbench_1.3.2-2~nd90+1_amd64.deb

wget http://security.debian.org/debian-security/pool/updates/main/o/openssl/libssl1.0.0_1.0.1t-1+deb8u11_amd64.deb
dpkg -i libssl1.0.0_1.0.1t-1+deb8u11_amd64.deb
rm -f libssl1.0.0_1.0.1t-1+deb8u11_amd64.deb

%environment
export LANG="en_US.UTF-8"
export LC_ALL="en_US.UTF-8"
export ND_ENTRYPOINT="/neurodocker/startup.sh"
export FREESURFER_HOME="/opt/freesurfer-6.0.1"
export PATH="/opt/freesurfer-6.0.1/bin:$PATH"
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/lib/x86_64-linux-gnu:/opt/matlabmcr-2018a/v94/runtime/glnxa64:/opt/matlabmcr-2018a/v94/bin/glnxa64:/opt/matlabmcr-2018a/v94/sys/os/glnxa64:/opt/matlabmcr-2018a/v94/extern/bin/glnxa64"
export MATLABCMD="/opt/matlabmcr-2018a/v94/toolbox/matlab"
export PERL5LIB="/opt/freesurfer-6.0.1/mni/lib/perl5/5.8.5"
#export PATH="/opt/workbench/bin_linux64:$PATH"
#export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/opt/workbench/libs_linux64"
export PATH="/usr/bin:$PATH"
alias wb_command='/usr/bin/wb_command'

%files

%runscript
/neurodocker/startup.sh "$@"
```

## Collection

 - Name: [switt4/surfAnalysis](https://github.com/switt4/surfAnalysis)
 - License: None

