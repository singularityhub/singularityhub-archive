---
id: 2817
name: "khanlab/neuroglia-core-minc"
branch: "master"
tag: "v1.0.0"
commit: "65d4be03381b78ded8f79259a663860279a1a51f"
version: "adff0dc311bfdd3b48b5a37f272b56a5"
build_date: "2018-05-18T02:49:52.830Z"
size_mb: 3432
size: 1236365343
sif: "https://datasets.datalad.org/shub/khanlab/neuroglia-core-minc/v1.0.0/2018-05-18-65d4be03-adff0dc3/adff0dc311bfdd3b48b5a37f272b56a5.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/khanlab/neuroglia-core-minc/v1.0.0/2018-05-18-65d4be03-adff0dc3/
recipe: https://datasets.datalad.org/shub/khanlab/neuroglia-core-minc/v1.0.0/2018-05-18-65d4be03-adff0dc3/Singularity
collection: khanlab/neuroglia-core-minc
---

# khanlab/neuroglia-core-minc:v1.0.0

```bash
$ singularity pull shub://khanlab/neuroglia-core-minc:v1.0.0
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

