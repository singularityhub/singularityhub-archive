---
id: 5866
name: "baxpr/nirsqa"
branch: "master"
tag: "v3.0.0"
commit: "5a425b111793b90042589b4bf1132c41034ed6c1"
version: "785ac9a0202ac499624cd1f8e58eefe6"
build_date: "2021-02-17T17:37:10.806Z"
size_mb: 3485
size: 1473167391
sif: "https://datasets.datalad.org/shub/baxpr/nirsqa/v3.0.0/2021-02-17-5a425b11-785ac9a0/785ac9a0202ac499624cd1f8e58eefe6.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/baxpr/nirsqa/v3.0.0/2021-02-17-5a425b11-785ac9a0/
recipe: https://datasets.datalad.org/shub/baxpr/nirsqa/v3.0.0/2021-02-17-5a425b11-785ac9a0/Singularity
collection: baxpr/nirsqa
---

# baxpr/nirsqa:v3.0.0

```bash
$ singularity pull shub://baxpr/nirsqa:v3.0.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%help
nirsqa

Quality evaluation and preprocessing for Hitachi ETG-4000 NIRS data. See 
/opt/nirsqa/README.md for references.

Run with the command line below. Arguments mes_file and onward are optional, 
and will take the defaults shown.

singularity run \
--cleanenv \
--home <input_dir> \
--bind <input_dir>:/INPUTS \
--bind <output_dir>:/OUTPUTS \
<singularity_image> \
mes_file /INPUTS/data_MES_Probe1.csv \
downsample 10 \
hpf_cutoff_sec 200 \
project UNK_PROJ \
subject UNK_SUBJ \
session UNK_SESS \
project UNK_SCAN \
out_dir /OUTPUTS

%setup
  mkdir -p ${SINGULARITY_ROOTFS}/opt/nirsqa

%files
  bin /opt/nirsqa
  src /opt/nirsqa
  external /opt/nirsqa
  README.md /opt/nirsqa
 
%labels
  Maintainer baxter.rogers@vanderbilt.edu

%post
  apt-get update
  apt-get install -y wget unzip openjdk-8-jre libxt6 \
    xvfb ghostscript imagemagick
  
  # Fix imagemagick policy to allow PDF output. See https://usn.ubuntu.com/3785-1/
  sed -i 's/rights="none" pattern="PDF"/rights="read | write" pattern="PDF"/' \
    /etc/ImageMagick-6/policy.xml

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
  xvfb-run --server-num=$(($$ + 99)) \
  --server-args='-screen 0 1600x1200x24 -ac +extension GLX' \
  sh /opt/nirsqa/bin/run_nirsqa.sh \
  /usr/local/MATLAB/MATLAB_Runtime/v92 "$@"
```

## Collection

 - Name: [baxpr/nirsqa](https://github.com/baxpr/nirsqa)
 - License: None

