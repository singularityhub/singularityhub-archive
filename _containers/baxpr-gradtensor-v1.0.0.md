---
id: 6305
name: "baxpr/gradtensor"
branch: "master"
tag: "v1.0.0"
commit: "bb9608c86768bbe60827748be110e53aa06daa37"
version: "c96475a9ec20b6c00cd836d2c7666dd1"
build_date: "2019-08-31T01:11:46.744Z"
size_mb: 3401
size: 1434488863
sif: "https://datasets.datalad.org/shub/baxpr/gradtensor/v1.0.0/2019-08-31-bb9608c8-c96475a9/c96475a9ec20b6c00cd836d2c7666dd1.simg"
url: https://datasets.datalad.org/shub/baxpr/gradtensor/v1.0.0/2019-08-31-bb9608c8-c96475a9/
recipe: https://datasets.datalad.org/shub/baxpr/gradtensor/v1.0.0/2019-08-31-bb9608c8-c96475a9/Singularity
collection: baxpr/gradtensor
---

# baxpr/gradtensor:v1.0.0

```bash
$ singularity pull shub://baxpr/gradtensor:v1.0.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%help
gradtensor

https://github.com/baxpr/gradtensor/
Gradient coil tensor: estimation from field maps, and correction of b-values

See information in the container's files 
  /opt/gradtensor/README.md
  /opt/gradtensor/usage-singularity.txt

%setup
  mkdir -p ${SINGULARITY_ROOTFS}/opt/gradtensor
  
%files
  bin /opt/gradtensor
  src /opt/gradtensor
  external /opt/gradtensor
  LICENSE.txt /opt/gradtensor
  README.md /opt/gradtensor
  usage-singularity.txt /opt/gradtensor
 
%labels
  Maintainer baxter.rogers@vanderbilt.edu

%post
  apt-get update
  apt-get install -y wget unzip openjdk-8-jre libxt6
  
  # Download the Matlab Compiled Runtime installer, install, clean up
  mkdir /MCR
  wget -nv -P /MCR http://ssd.mathworks.com/supportfiles/downloads/R2017a/deployment_files/R2017a/installers/glnxa64/MCR_R2017a_glnxa64_installer.zip
  unzip -q /MCR/MCR_R2017a_glnxa64_installer.zip -d /MCR/MCR_R2017a_glnxa64_installer
  /MCR/MCR_R2017a_glnxa64_installer/install -mode silent -agreeToLicense yes
  rm -r /MCR/MCR_R2017a_glnxa64_installer /MCR/MCR_R2017a_glnxa64_installer.zip
  rmdir /MCR

  # Create input/output directories for binding
  mkdir /INPUTS && mkdir /OUTPUTS

%runscript
    /bin/bash -c "cat /opt/gradtensor/usage-singularity.txt"
```

## Collection

 - Name: [baxpr/gradtensor](https://github.com/baxpr/gradtensor)
 - License: [Other](None)

