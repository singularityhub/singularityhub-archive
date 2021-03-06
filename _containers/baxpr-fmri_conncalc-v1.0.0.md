---
id: 5342
name: "baxpr/fmri_conncalc"
branch: "master"
tag: "v1.0.0"
commit: "cd316395c1c2e281839639010b55e599ba955a28"
version: "9385959c90d6b29e9074323edbcffbff"
build_date: "2018-10-24T18:39:33.700Z"
size_mb: 3589
size: 1581383711
sif: "https://datasets.datalad.org/shub/baxpr/fmri_conncalc/v1.0.0/2018-10-24-cd316395-9385959c/9385959c90d6b29e9074323edbcffbff.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/baxpr/fmri_conncalc/v1.0.0/2018-10-24-cd316395-9385959c/
recipe: https://datasets.datalad.org/shub/baxpr/fmri_conncalc/v1.0.0/2018-10-24-cd316395-9385959c/Singularity
collection: baxpr/fmri_conncalc
---

# baxpr/fmri_conncalc:v1.0.0

```bash
$ singularity pull shub://baxpr/fmri_conncalc:v1.0.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%help
fmri_conncalc

FMRI functional connectivity processing

TO BUILD
We expect to build from fmri_conncalc directory:
  sudo singularity build fmri_conncalc_v1.0.0.simg Singularity.v1.0.0 

TO RUN
See the associated YAML files for info about inputs and running the container

%files
  # Build from fmri_conncalc for this to work 
  bin /matlab_bin
 
%labels
  Maintainer baxter.rogers@vanderbilt.edu

%post
  apt-get update
  apt-get install -y wget unzip zip xvfb ghostscript openjdk-8-jre imagemagick
  
  # Fix imagemagick policy to allow PDF output. See https://usn.ubuntu.com/3785-1/
  sed -i 's/rights="none" pattern="PDF"/rights="read | write" pattern="PDF"/' \
    /etc/ImageMagick-6/policy.xml
  
  # Download the Matlab Compiled Runtime installer, install, clean up
  mkdir /MCR
  wget -nv -P /MCR http://ssd.mathworks.com/supportfiles/downloads/R2017a/deployment_files/R2017a/installers/glnxa64/MCR_R2017a_glnxa64_installer.zip
  unzip /MCR/MCR_R2017a_glnxa64_installer.zip -d /MCR/MCR_R2017a_glnxa64_installer
  /MCR/MCR_R2017a_glnxa64_installer/install -mode silent -agreeToLicense yes
  rm -r /MCR/MCR_R2017a_glnxa64_installer /MCR/MCR_R2017a_glnxa64_installer.zip
  rmdir /MCR

  # Create input/output directories for binding
  mkdir /INPUTS && mkdir /OUTPUTS

  # Singularity-hub doesn't work with github LFS (it gets the pointer info instead 
  # of the actual file) so we get the compiled matlab executable via direct download
  rm /matlab_bin/fmri_conncalc
  wget -nv -P /matlab_bin https://github.com/baxpr/fmri_conncalc/raw/master/bin/fmri_conncalc
  chmod ugo+rx /matlab_bin/fmri_conncalc

%environment
  # Set Matlab library path
  LD_LIBRARY_PATH=/usr/local/MATLAB/MATLAB_Runtime/v92/runtime/glnxa64:/usr/local/MATLAB/MATLAB_Runtime/v92/bin/glnxa64:/usr/local/MATLAB/MATLAB_Runtime/v92/sys/os/glnxa64:${LD_LIBRARY_PATH}
  export LD_LIBRARY_PATH

%runscript
    xvfb-run --server-num=$(($$ + 99)) \
    --server-args='-screen 0 1600x1200x24 -ac +extension GLX' \
    sh /matlab_bin/run_fmri_conncalc.sh \
    /usr/local/MATLAB/MATLAB_Runtime/v92 "$@"
```

## Collection

 - Name: [baxpr/fmri_conncalc](https://github.com/baxpr/fmri_conncalc)
 - License: None

