---
id: 9125
name: "baxpr/fmriqa"
branch: "master"
tag: "v4.2.0"
commit: "3ed4922a06b54ddef726a9e9a4f9a3969438affc"
version: "4988bc3ff97e7a79fc386cc3a2eb47c6"
build_date: "2019-05-17T08:23:25.035Z"
size_mb: 3896
size: 1715048479
sif: "https://datasets.datalad.org/shub/baxpr/fmriqa/v4.2.0/2019-05-17-3ed4922a-4988bc3f/4988bc3ff97e7a79fc386cc3a2eb47c6.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/baxpr/fmriqa/v4.2.0/2019-05-17-3ed4922a-4988bc3f/
recipe: https://datasets.datalad.org/shub/baxpr/fmriqa/v4.2.0/2019-05-17-3ed4922a-4988bc3f/Singularity
collection: baxpr/fmriqa
---

# baxpr/fmriqa:v4.2.0

```bash
$ singularity pull shub://baxpr/fmriqa:v4.2.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%help
Functional MRI QA pipeline. Usage:

  singularity run --cleanenv \
    --home `pwd`/INPUTS \
    --bind INPUTS:/INPUTS \
    --bind OUTPUTS:/OUTPUTS \
    container.simg \
    /OUTPUTS \
    INPUTS/t1.nii.gz \
    INPUTS/seg.nii.gz \
    INPUTS/fmri.nii.gz \
    PROJ_LABEL \
    SUBJ_LABEL \
    SESS_LABEL \
    SCAN_LABEL


%setup
  mkdir -p ${SINGULARITY_ROOTFS}/opt/fmriqa


%files
  bin                          /opt/fmriqa
  src                          /opt/fmriqa
  README.md                    /opt/fmriqa
  compile_matlab.sh            /opt/fmriqa
  spm_make_standalone_local.m  /opt/fmriqa
  test_sing_container.sh       /opt/fmriqa
  
 
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
  rm /opt/fmriqa/bin/spm12.ctf
  wget -nv -P /opt/fmriqa/bin https://github.com/baxpr/fmriqa/raw/master/bin/spm12.ctf
  /opt/fmriqa/bin/run_spm12.sh /usr/local/MATLAB/MATLAB_Runtime/v92 quit

%environment
  # We don't need to set the Matlab library path here, because Matlab's
  # auto-generated run_??.sh script does it for us.


%runscript
  xvfb-run --server-num=$(($$ + 99)) \
  --server-args='-screen 0 1600x1200x24 -ac +extension GLX' \
  bash /opt/fmriqa/bin/run_spm12.sh \
  /usr/local/MATLAB/MATLAB_Runtime/v92 function fmriqa "$@"
```

## Collection

 - Name: [baxpr/fmriqa](https://github.com/baxpr/fmriqa)
 - License: None

