---
id: 9697
name: "baxpr/connprep"
branch: "master"
tag: "v2.1.0"
commit: "38b1b04bd360b9631d65eab0d6430c53b87500d3"
version: "9a58674057e931eb2574be4775399312"
build_date: "2021-02-10T18:21:01.378Z"
size_mb: 3926
size: 1741303839
sif: "https://datasets.datalad.org/shub/baxpr/connprep/v2.1.0/2021-02-10-38b1b04b-9a586740/9a58674057e931eb2574be4775399312.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/baxpr/connprep/v2.1.0/2021-02-10-38b1b04b-9a586740/
recipe: https://datasets.datalad.org/shub/baxpr/connprep/v2.1.0/2021-02-10-38b1b04b-9a586740/Singularity
collection: baxpr/connprep
---

# baxpr/connprep:v2.1.0

```bash
$ singularity pull shub://baxpr/connprep:v2.1.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%help
Functional MRI connectivity preprocessing pipeline. Info and usage:
/opt/connprep/README.md
/opt/connprep/build/test_sing_container.sh


%setup
  mkdir -p ${SINGULARITY_ROOTFS}/opt/connprep


%files
  bin                          /opt/connprep
  src                          /opt/connprep
  build                        /opt/connprep
  README.md                    /opt/connprep

 
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
  # of the actual file) so we get the compiled matlab executable via direct download.
  # Also need a "dry run" of SPM executable to avoid directory creation errors later.
  rm /opt/connprep/bin/spm12.ctf
  wget -nv -P /opt/connprep/bin https://github.com/baxpr/connprep/raw/master/bin/spm12.ctf
  /opt/connprep/bin/run_spm12.sh /usr/local/MATLAB/MATLAB_Runtime/v92 quit


%environment
  # We don't need to set the Matlab library path here, because Matlab's
  # auto-generated run_??.sh script does it for us.


%runscript
  xvfb-run --server-num=$(($$ + 99)) \
  --server-args='-screen 0 1600x1200x24 -ac +extension GLX' \
  bash /opt/connprep/bin/run_spm12.sh \
  /usr/local/MATLAB/MATLAB_Runtime/v92 function connprep "$@"
```

## Collection

 - Name: [baxpr/connprep](https://github.com/baxpr/connprep)
 - License: None

