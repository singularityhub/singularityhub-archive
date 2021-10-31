---
id: 6843
name: "baxpr/magm-normalize"
branch: "master"
tag: "v3.0.0"
commit: "98a4ed921960c8b0e8e64777c5944bd6c653c3ad"
version: "f894195959e9e59282eac57a8337cbf6"
build_date: "2019-02-04T09:08:23.726Z"
size_mb: 3526
size: 1558937631
sif: "https://datasets.datalad.org/shub/baxpr/magm-normalize/v3.0.0/2019-02-04-98a4ed92-f8941959/f894195959e9e59282eac57a8337cbf6.simg"
url: https://datasets.datalad.org/shub/baxpr/magm-normalize/v3.0.0/2019-02-04-98a4ed92-f8941959/
recipe: https://datasets.datalad.org/shub/baxpr/magm-normalize/v3.0.0/2019-02-04-98a4ed92-f8941959/Singularity
collection: baxpr/magm-normalize
---

# baxpr/magm-normalize:v3.0.0

```bash
$ singularity pull shub://baxpr/magm-normalize:v3.0.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%help
magm_normalize

Warp gray matter segmentation to atlas using SPM12 "Old Normalise"

%setup
  mkdir -p ${SINGULARITY_ROOTFS}/opt/magm_normalize

%files
  bin /opt/magm_normalize/bin
  src /opt/magm_normalize/bin
  compile_matlab.sh /opt/magm_normalize
  test_singularity.sh /opt/magm_normalize

%labels
  Maintainer baxter.rogers@vanderbilt.edu

%post
  apt-get update
  apt-get install -y wget unzip zip xvfb openjdk-8-jre

  # Download the Matlab Compiled Runtime installer, install, clean up
  mkdir /MCR
  wget -nv -P/MCR http://ssd.mathworks.com/supportfiles/downloads/R2017a/deployment_files/R2017a/installers/glnxa64/MCR_R2017a_glnxa64_installer.zip
  unzip /MCR/MCR_R2017a_glnxa64_installer.zip -d /MCR/MCR_R2017a_glnxa64_installer
  /MCR/MCR_R2017a_glnxa64_installer/install -mode silent -agreeToLicense yes
  rm -fr /MCR/MCR_R2017a_glnxa64_installer /MCR/MCR_R2017a_glnxa64_installer.zip
  rmdir /MCR

  # Create input/output directories for binding
  mkdir /INPUTS && mkdir /OUTPUTS

  # Singularity-hub doesn't work with github LFS (it gets the pointer info instead 
  # of the actual file) so we get the compiled matlab executable via direct download
  rm /opt/magm_normalize/bin/magm_normalize
  wget -nv -P /opt/magm_normalize/bin https://github.com/baxpr/magm-normalize/raw/master/bin/magm_normalize
  chmod ugo+rx /opt/magm_normalize/bin/magm_normalize

%runscript
  xvfb-run --server-num=$(($$ + 99)) \
  --server-args='-screen 0 1600x1200x24 -ac +extension GLX' \
  bash /opt/magm_normalize/bin/run_magm_normalize.sh \
  /usr/local/MATLAB/MATLAB_Runtime/v92 "$@"
```

## Collection

 - Name: [baxpr/magm-normalize](https://github.com/baxpr/magm-normalize)
 - License: None

