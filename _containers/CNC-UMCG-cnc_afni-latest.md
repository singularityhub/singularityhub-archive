---
id: 3020
name: "CNC-UMCG/cnc_afni"
branch: "master"
tag: "latest"
commit: "1e2c267d68212d6db3784181b263ae7d6bfa9fde"
version: "763932047560de9ecea98ccd8e91264b"
build_date: "2021-04-09T19:11:18.324Z"
size_mb: 5509
size: 2933506079
sif: "https://datasets.datalad.org/shub/CNC-UMCG/cnc_afni/latest/2021-04-09-1e2c267d-76393204/763932047560de9ecea98ccd8e91264b.simg"
url: https://datasets.datalad.org/shub/CNC-UMCG/cnc_afni/latest/2021-04-09-1e2c267d-76393204/
recipe: https://datasets.datalad.org/shub/CNC-UMCG/cnc_afni/latest/2021-04-09-1e2c267d-76393204/Singularity
collection: CNC-UMCG/cnc_afni
---

# CNC-UMCG/cnc_afni:latest

```bash
$ singularity pull shub://CNC-UMCG/cnc_afni:latest
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: CNC-UMCG/cnc_r

%environment
    export R_LIBS=$HOME/R
    mkdir $R_LIBS
    export PATH=$PATH:/usr/share/afni
    export R_LIBS=$HOME/R
    
%post

  # afni dependencies
  ## apt-get install -y libmotif4 libmotif-dev motif-clients gsl-bin netpbm xvfb gnome-tweak-tool libjpeg62 xterm gedit evince
  
  echo "deb http://security.ubuntu.com/ubuntu precise-security main" >> /etc/apt/sources.list
  apt-get update
  
  apt-get install -y libxp6 tcsh
  apt-get install -y python-qt4 r-base
  
  # install afni
  wget https://afni.nimh.nih.gov/pub/dist/tgz/linux_ubuntu_16_64.tgz
  tar xvzf linux_ubuntu_16_64.tgz -C /usr/share/
    
  mv /usr/share/linux_ubuntu_16_64 /usr/share/afni   
  
  curl -O https://afni.nimh.nih.gov/pub/dist/src/scripts_src/@add_rcran_ubuntu.tcsh
  tcsh @add_rcran_ubuntu.tcsh

  #rPkgsInstall -pkgs ALL

  #afni_system_check.py -check_all > out.afni_system_check.txt
```

## Collection

 - Name: [CNC-UMCG/cnc_afni](https://github.com/CNC-UMCG/cnc_afni)
 - License: None

