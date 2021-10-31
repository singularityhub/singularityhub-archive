---
id: 6354
name: "baxpr/example-spm-singularity-spider"
branch: "master"
tag: "v1.0.0"
commit: "6d6448057086bbee575462ca78c55611f177d134"
version: "61c734b65f9046753a1bbbcb802ab22b"
build_date: "2019-01-20T13:44:22.526Z"
size_mb: 3525
size: 1557848095
sif: "https://datasets.datalad.org/shub/baxpr/example-spm-singularity-spider/v1.0.0/2019-01-20-6d644805-61c734b6/61c734b65f9046753a1bbbcb802ab22b.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/baxpr/example-spm-singularity-spider/v1.0.0/2019-01-20-6d644805-61c734b6/
recipe: https://datasets.datalad.org/shub/baxpr/example-spm-singularity-spider/v1.0.0/2019-01-20-6d644805-61c734b6/Singularity
collection: baxpr/example-spm-singularity-spider
---

# baxpr/example-spm-singularity-spider:v1.0.0

```bash
$ singularity pull shub://baxpr/example-spm-singularity-spider:v1.0.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%help
example_spm

An example SPM-based container that implements realignment, coregistration, and 
smoothing for an fMRI data set. See /example_spm/README.md

%setup

  # Make a directory to store various files. We need bin to run, the others are
  # just to be informative for anyone who only has the container at hand.
  mkdir -p ${SINGULARITY_ROOTFS}/opt/example_spm

%files

  # Copy Matlab executable from bin (on host) to /example_spm in the container. 
  # No processing happens without it!
  bin /opt/example_spm
  
  # Let's also copy the source code. It's not needed to run the container, but
  # it could helpful for someone if we include it in anyway.
  src /opt/example_spm
  
  # And the README file and compilation script
  README.md /opt/example_spm
  compile_matlab.sh /opt/example_spm
  
 
%labels
  Maintainer baxter.rogers@vanderbilt.edu

%post

  # Update the package manager and install needed packages
  #   wget            Lets us download software during the build
  #   unzip,zip       Lets us unzip same
  #   openjdk-8-jre   Required for Matlab Runtime to work
  #   xvfb            May be used if figures must be shown on a virtual display, 
  #                      as no actual display is available at runtime. Matlab 
  #                      Runtime requires this, anyway.
  #   ghostscript     These two provide tools to generate/combine images/PDFs.
  #   imagemagick        We are not using them for this simple example.
  apt-get -qq update
  apt-get -qq install -y wget unzip zip openjdk-8-jre xvfb
  
  # If we are using ImageMagick to create PDFs, we need to relax its security 
  # policy to permit this. See https://usn.ubuntu.com/3785-1/
  #sed -i 's/rights="none" pattern="PDF"/rights="read | write" pattern="PDF"/' \
  #  /etc/ImageMagick-6/policy.xml
  
  # Download the Matlab Compiled Runtime installer, install, clean up.
  mkdir /MCR
  wget -nv -P /MCR http://ssd.mathworks.com/supportfiles/downloads/R2017a/deployment_files/R2017a/installers/glnxa64/MCR_R2017a_glnxa64_installer.zip
  unzip -q /MCR/MCR_R2017a_glnxa64_installer.zip -d /MCR/MCR_R2017a_glnxa64_installer
  /MCR/MCR_R2017a_glnxa64_installer/install -mode silent -agreeToLicense yes
  rm -r /MCR/MCR_R2017a_glnxa64_installer /MCR/MCR_R2017a_glnxa64_installer.zip
  rmdir /MCR

  # Create input/output directories that we can bind to at runtime
  mkdir /INPUTS && mkdir /OUTPUTS

  # Singularity-hub doesn't work with github LFS (it gets the pointer info 
  # instead of the actual file) so we get the compiled matlab executable via 
  # direct download. The "raw" in the URL is critical here.
  rm /opt/example_spm/bin/example_main
  wget -nv -P /opt/example_spm/bin https://github.com/baxpr/example-spm-singularity-spider/raw/master/bin/example_main
  chmod ugo+rx /opt/example_spm/bin/example_main


%environment
  # We don't need to set the Matlab library path here, because Matlab's 
  # auto-generated run_??.sh script does it for us.
 

%runscript
  # We use the "$@" argument to pass along any arguments that are given at the
  # singularity command line - this is how we pass in file paths, parameters, 
  # etc. The first argument given here is the location of the Matlab Runtime -
  # see the explanation in Matlab's auto-generated file bin/readme.txt
  bash /opt/example_spm/bin/run_example_main.sh \
  /usr/local/MATLAB/MATLAB_Runtime/v92 "$@"
```

## Collection

 - Name: [baxpr/example-spm-singularity-spider](https://github.com/baxpr/example-spm-singularity-spider)
 - License: None

