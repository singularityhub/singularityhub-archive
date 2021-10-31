---
id: 5804
name: "baxpr/freesurfer-singularity"
branch: "master"
tag: "dev"
commit: "ccd366c606e3800897ebdd9ee0b41cbed41740ae"
version: "09b4cb5db001eb3d4df851232232a35e"
build_date: "2020-11-16T23:48:10.573Z"
size_mb: 11080
size: 5068095519
sif: "https://datasets.datalad.org/shub/baxpr/freesurfer-singularity/dev/2020-11-16-ccd366c6-09b4cb5d/09b4cb5db001eb3d4df851232232a35e.simg"
url: https://datasets.datalad.org/shub/baxpr/freesurfer-singularity/dev/2020-11-16-ccd366c6-09b4cb5d/
recipe: https://datasets.datalad.org/shub/baxpr/freesurfer-singularity/dev/2020-11-16-ccd366c6-09b4cb5d/Singularity
collection: baxpr/freesurfer-singularity
---

# baxpr/freesurfer-singularity:dev

```bash
$ singularity pull shub://baxpr/freesurfer-singularity:dev
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:7.5.1804

%help

Freesurfer development version. Runs recon-all plus hippocampus, thalamus, 
brainstem modules. Requires a valid license file at runtime.

Useful information within the container:
  /opt/README.md                          Summary and references
  /opt/USAGE.md                           Detailed instructions
  /usr/local/freesurfer/build-stamp.txt   Specific Freesurfer version


%files

  # Freesurfer development version, if we are going to download manually and 
  # reference a local copy during the build
  # https://surfer.nmr.mgh.harvard.edu/pub/dist/freesurfer/dev/freesurfer-linux-centos7_x86_64-dev.tar.gz
  #freesurfer-linux-centos7_x86_64-dev.tar.gz /usr/local

  # Matlab runtime, if we are going to download manually and ref the local copy
  # http://ssd.mathworks.com/supportfiles/downloads/R2014b/deployment_files/R2014b/installers/glnxa64/MCR_R2014b_glnxa64_installer.zip
  #MCR_R2014b_glnxa64_installer.zip /opt

  # FSL archive, if we are going to download manually and ref the local copy
  # https://fsl.fmrib.ox.ac.uk/fsldownloads/fsl-6.0.0-centos7_64.tar.gz
  #fsl-6.0.0-centos7_64.tar.gz /opt

  # Default run scripts
  runscripts /opt

  # Usage and Readme
  USAGE.md /opt
  README.md /opt
  

%post
  
  # For installs
  yum -y install unzip wget
  
  # For Freesurfer
  yum -y install tcsh bc mesa-libGLU libgomp perl mesa-dri-drivers
  
  # For FSL
  yum -y install epel-release
  yum -y install openblas-devel
  
  # For matlab runtime
  yum -y install java-1.8.0-openjdk
  
  # For X
  yum -y install xorg-x11-server-Xvfb xorg-x11-xauth which

  # For PDF outputs
  yum -y install ImageMagick
  
  
  # We need a piece of FSL (fslstats)
  wget -nv -P /opt https://fsl.fmrib.ox.ac.uk/fsldownloads/fsl-6.0.0-centos7_64.tar.gz
  cd /opt
  tar -zxf fsl-6.0.0-centos7_64.tar.gz
  mkdir -p /usr/local/fsl/bin
  cp fsl/bin/fslstats /usr/local/fsl/bin
  rm -r fsl fsl-6.0.0-centos7_64.tar.gz
  
  
  # Matlab runtime for brainstem, hippocampus, thalamus modules
  wget -nv -P /opt http://ssd.mathworks.com/supportfiles/downloads/R2014b/deployment_files/R2014b/installers/glnxa64/MCR_R2014b_glnxa64_installer.zip
  unzip -q /opt/MCR_R2014b_glnxa64_installer.zip -d /opt/MCR_R2014b_glnxa64_installer
  /opt/MCR_R2014b_glnxa64_installer/install -mode silent -agreeToLicense yes
  rm -r /opt/MCR_R2014b_glnxa64_installer
  rm /opt/MCR_R2014b_glnxa64_installer.zip


  # Install Freesurfer
  wget -nv -P /usr/local https://surfer.nmr.mgh.harvard.edu/pub/dist/freesurfer/dev/freesurfer-linux-centos7_x86_64-dev.tar.gz
  cd /usr/local
  tar -zxf freesurfer-linux-centos7_x86_64-dev.tar.gz
  rm freesurfer-linux-centos7_x86_64-dev.tar.gz

  # Freeview needs a machine id here
  dbus-uuidgen > /etc/machine-id
  
  # Tell freesurfer where to find the MCR
  ln -s /usr/local/MATLAB/MATLAB_Compiler_Runtime/v84 /usr/local/freesurfer/MCRv84


  # Create input/output directories for binding
  mkdir /INPUTS && mkdir /OUTPUTS


%environment

  # FSL (we only use fslstats so no need for the full setup)
  export FSLOUTPUTTYPE=NIFTI_GZ
  
  # Freesurfer
  export FREESURFER_HOME=/usr/local/freesurfer


%runscript
  xvfb-run --server-num=$(($$ + 99)) \
  --server-args='-screen 0 1600x1200x24 -ac +extension GLX' \
  bash /opt/runscripts/run_everything.sh "$@"
```

## Collection

 - Name: [baxpr/freesurfer-singularity](https://github.com/baxpr/freesurfer-singularity)
 - License: None

