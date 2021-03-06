---
id: 2882
name: "khanlab/neuroglia-core-minc"
branch: "master"
tag: "v1.0.1b"
commit: "5b05467f873af40f6d0465235ba6db980a043bfd"
version: "8973cf9959e65caa5e97be4ff22f27c9"
build_date: "2018-05-22T20:04:29.627Z"
size_mb: 3484
size: 1252114463
sif: "https://datasets.datalad.org/shub/khanlab/neuroglia-core-minc/v1.0.1b/2018-05-22-5b05467f-8973cf99/8973cf9959e65caa5e97be4ff22f27c9.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/khanlab/neuroglia-core-minc/v1.0.1b/2018-05-22-5b05467f-8973cf99/
recipe: https://datasets.datalad.org/shub/khanlab/neuroglia-core-minc/v1.0.1b/2018-05-22-5b05467f-8973cf99/Singularity
collection: khanlab/neuroglia-core-minc
---

# khanlab/neuroglia-core-minc:v1.0.1b

```bash
$ singularity pull shub://khanlab/neuroglia-core-minc:v1.0.1b
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:xenial

#########
%setup
#########
mkdir -p $SINGULARITY_ROOTFS/src
cp -Rv . $SINGULARITY_ROOTFS/src

#########
%post
#########

cd /src/install_scripts

export DEBIAN_FRONTEND=noninteractive
bash 00.install_basics_sudo.sh
bash 10.install_afni_fsl_sudo.sh
bash 16.install_ants_by_binary.sh /opt
bash 25.install_niftyreg_by_source.sh /opt
bash 22.install_minc_by_deb.sh /opt


#remove all install scripts
rm -rf /src


#########
%environment


#fsl
export FSLDIR=/usr/share/fsl/5.0
export POSSUMDIR=$FSLDIR
export PATH=/usr/lib/fsl/5.0:$PATH
export FSLOUTPUTTYPE=NIFTI_GZ
export FSLMULTIFILEQUIT=TRUE
export FSLTCLSH=/usr/bin/tclsh
export FSLWISH=/usr/bin/wish
export FSLBROWSER=/etc/alternatives/x-www-browser
export LD_LIBRARY_PATH=/usr/lib/fsl/5.0:${LD_LIBRARY_PATH}


#ants
export PATH=/opt/ants:$PATH
export ANTSPATH=/opt/ants

#niftyreg
export LD_LIBRARY_PATH=/opt/niftyreg-1.3.9/lib:$LD_LIBRARY_PATH 
export PATH=/opt/niftyreg-1.3.9/bin:$PATH

#minc
export MINC_TOOLKIT=/opt/minc/1.9.15
export MINC_TOOLKIT_VERSION="1.9.15-20170529"
export PATH=/opt/minc/1.9.15/bin:/opt/minc/1.9.15/pipeline:${PATH}
export PERL5LIB=/opt/minc/1.9.15/perl:/opt/minc/1.9.15/pipeline:${PERL5LIB}
export LD_LIBRARY_PATH=/opt/minc/1.9.15/lib:/opt/minc/1.9.15/lib/InsightToolkit:${LD_LIBRARY_PATH}
export MNI_DATAPATH=/opt/minc/1.9.15/share
export MINC_FORCE_V2=1
export MINC_COMPRESS=4
export VOLUME_CACHE_THRESHOLD=-1
export MANPATH=/opt/minc/1.9.15/man:${MANPATH}
```

## Collection

 - Name: [khanlab/neuroglia-core-minc](https://github.com/khanlab/neuroglia-core-minc)
 - License: None

