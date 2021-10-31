---
id: 5353
name: "baxpr/fmri_modularity"
branch: "master"
tag: "v1.0.0"
commit: "cf5b733276949992622cdc95022b52e0668dffe9"
version: "e3041514ab02ee78339f74b0e09c92f8"
build_date: "2018-10-26T11:06:03.712Z"
size_mb: 3589
size: 1581309983
sif: "https://datasets.datalad.org/shub/baxpr/fmri_modularity/v1.0.0/2018-10-26-cf5b7332-e3041514/e3041514ab02ee78339f74b0e09c92f8.simg"
url: https://datasets.datalad.org/shub/baxpr/fmri_modularity/v1.0.0/2018-10-26-cf5b7332-e3041514/
recipe: https://datasets.datalad.org/shub/baxpr/fmri_modularity/v1.0.0/2018-10-26-cf5b7332-e3041514/Singularity
collection: baxpr/fmri_modularity
---

# baxpr/fmri_modularity:v1.0.0

```bash
$ singularity pull shub://baxpr/fmri_modularity:v1.0.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%help
fmri_modularity

FMRI functional connectivity processing - compute modularity from a connectivity
matrix.

See the associated YAML for inputs, outputs, and run command.

%files
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
  wget -nv -P/MCR http://ssd.mathworks.com/supportfiles/downloads/R2017a/deployment_files/R2017a/installers/glnxa64/MCR_R2017a_glnxa64_installer.zip
  unzip /MCR/MCR_R2017a_glnxa64_installer.zip -d /MCR/MCR_R2017a_glnxa64_installer
  /MCR/MCR_R2017a_glnxa64_installer/install -mode silent -agreeToLicense yes
  rm -fr /MCR/MCR_R2017a_glnxa64_installer /MCR/MCR_R2017a_glnxa64_installer.zip
  rmdir /MCR

  # Create input/output directories for binding
  mkdir /INPUTS && mkdir /OUTPUTS

  # Singularity-hub doesn't work with github LFS (it gets the pointer info instead 
  # of the actual file) so we get the compiled matlab executable via direct download
  rm /matlab_bin/fmri_modularity
  wget -nv -P /matlab_bin https://github.com/baxpr/fmri_modularity/raw/master/bin/fmri_modularity
  chmod ugo+rx /matlab_bin/fmri_modularity
  
%environment
  # Set Matlab library path
  LD_LIBRARY_PATH=/usr/local/MATLAB/MATLAB_Runtime/v92/runtime/glnxa64:/usr/local/MATLAB/MATLAB_Runtime/v92/bin/glnxa64:/usr/local/MATLAB/MATLAB_Runtime/v92/sys/os/glnxa64:${LD_LIBRARY_PATH}
  export LD_LIBRARY_PATH

%runscript
    xvfb-run --server-num=$(($$ + 99)) \
    --server-args='-screen 0 1600x1200x24 -ac +extension GLX' \
    sh /matlab_bin/run_fmri_modularity.sh \
    /usr/local/MATLAB/MATLAB_Runtime/v92 "$@"
```

## Collection

 - Name: [baxpr/fmri_modularity](https://github.com/baxpr/fmri_modularity)
 - License: None

