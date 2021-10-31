---
id: 5399
name: "baxpr/ndw_wm_edat"
branch: "master"
tag: "v3.0.0"
commit: "4d1bae0afca41c34bfd28a873a42e88db6ce3619"
version: "f804ee2a7bb037ba4de670509581e77a"
build_date: "2018-11-01T03:16:09.017Z"
size_mb: 3436
size: 1441493023
sif: "https://datasets.datalad.org/shub/baxpr/ndw_wm_edat/v3.0.0/2018-11-01-4d1bae0a-f804ee2a/f804ee2a7bb037ba4de670509581e77a.simg"
url: https://datasets.datalad.org/shub/baxpr/ndw_wm_edat/v3.0.0/2018-11-01-4d1bae0a-f804ee2a/
recipe: https://datasets.datalad.org/shub/baxpr/ndw_wm_edat/v3.0.0/2018-11-01-4d1bae0a-f804ee2a/Singularity
collection: baxpr/ndw_wm_edat
---

# baxpr/ndw_wm_edat:v3.0.0

```bash
$ singularity pull shub://baxpr/ndw_wm_edat:v3.0.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%help

Computes d prime, accuracy, reaction time for NDW working memory study. See associated YAML for inputs and outputs.


%files
  bin /matlab_bin

%labels
  Maintainer baxter.rogers@vanderbilt.edu

%post
  apt-get update
  apt-get install -y wget unzip zip xvfb ghostscript openjdk-8-jre
  
  # Download the Matlab Compiled Runtime installer
  mkdir /MCR
  wget -P/MCR http://ssd.mathworks.com/supportfiles/downloads/R2017a/deployment_files/R2017a/installers/glnxa64/MCR_R2017a_glnxa64_installer.zip

  # Install the MCR, then clean up. unzip needs a fully qualified output path
  unzip /MCR/MCR_R2017a_glnxa64_installer.zip -d /MCR/MCR_R2017a_glnxa64_installer
  /MCR/MCR_R2017a_glnxa64_installer/install -mode silent -agreeToLicense yes
  rm -fr /MCR/MCR_R2017a_glnxa64_installer /MCR/MCR_R2017a_glnxa64_installer.zip

  # Create input/output directories for binding
  mkdir /INPUTS && mkdir /OUTPUTS

  # Singularity-hub doesn't work with github LFS (it gets the pointer info instead 
  # of the actual file) so we get the compiled matlab executable via direct download
  rm /matlab_bin/ndw_wm_edat
  wget -nv -P /matlab_bin https://github.com/baxpr/ndw_wm_edat/raw/master/bin/ndw_wm_edat
  chmod ugo+rx /matlab_bin/ndw_wm_edat

%environment
  # Set Matlab library path
  LD_LIBRARY_PATH=/usr/local/MATLAB/MATLAB_Runtime/v92/runtime/glnxa64:/usr/local/MATLAB/MATLAB_Runtime/v92/bin/glnxa64:/usr/local/MATLAB/MATLAB_Runtime/v92/sys/os/glnxa64:${LD_LIBRARY_PATH}
  XAPPLRESDIR=/usr/local/MATLAB/MATLAB_Runtime/v92/X11/app-defaults
  export LD_LIBRARY_PATH XAPPLRESDIR

%runscript
    xvfb-run --server-num=$(($$ + 99)) \
    --server-args='-screen 0 1600x1200x24 -ac +extension GLX' \
    /matlab_bin/run_ndw_wm_edat.sh \
    /usr/local/MATLAB/MATLAB_Runtime/v92 \
    "$@"
```

## Collection

 - Name: [baxpr/ndw_wm_edat](https://github.com/baxpr/ndw_wm_edat)
 - License: None

