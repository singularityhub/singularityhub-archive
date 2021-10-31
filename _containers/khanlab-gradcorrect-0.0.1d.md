---
id: 2597
name: "khanlab/gradcorrect"
branch: "master"
tag: "0.0.1d"
commit: "079b694bfb5a13727159710f08bf175bb79487ed"
version: "877e14d44f08d78e63c146e12cda19ac"
build_date: "2018-04-20T05:38:16.782Z"
size_mb: 4237
size: 1577648159
sif: "https://datasets.datalad.org/shub/khanlab/gradcorrect/0.0.1d/2018-04-20-079b694b-877e14d4/877e14d44f08d78e63c146e12cda19ac.simg"
url: https://datasets.datalad.org/shub/khanlab/gradcorrect/0.0.1d/2018-04-20-079b694b-877e14d4/
recipe: https://datasets.datalad.org/shub/khanlab/gradcorrect/0.0.1d/2018-04-20-079b694b-877e14d4/Singularity
collection: khanlab/gradcorrect
---

# khanlab/gradcorrect:0.0.1d

```bash
$ singularity pull shub://khanlab/gradcorrect:0.0.1d
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:xenial

#note: install_afni_fsl_sudo.sh solves error message when run itksnap: LibGlu.so.1

#run freesurfer's freeview 
# if libQtOpenGL.so.4, run sudo apt-get libqt4-dev
# if missing:  libjpeg.so.62, run apt-get install libjpeg62

#create image
#rm ~/neuroglia/neuroglia.img && singularity create  --size 20000 ~/neuroglia/neuroglia.img && sudo singularity bootstrap ~/neuroglia/neuroglia.img Singularity

#########
%setup
#########
mkdir -p $SINGULARITY_ROOTFS/gradcorrect
cp -Rv . $SINGULARITY_ROOTFS/gradcorrect

#########
%post
#########

cd /gradcorrect/deps

export DEBIAN_FRONTEND=noninteractive
bash 00.install_basics_sudo.sh
bash 03.install_anaconda2_nipype_dcmstack_by_binary.sh /opt
bash 10.install_afni_fsl_sudo.sh
bash 25.install_niftyreg_by_source.sh /opt
bash 28.install_gradunwarp_by_source.sh /opt




#########
%environment

#anaconda2
export PATH=/opt/anaconda2/bin/:$PATH

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

#niftyreg
export LD_LIBRARY_PATH=/opt/niftyreg-1.3.9/lib:$LD_LIBRARY_PATH 
export PATH=/opt/niftyreg-1.3.9/bin:$PATH

#this app:
export PATH=/gradcorrect:$PATH

%runscript
exec /gradcorrect/run.sh $@
```

## Collection

 - Name: [khanlab/gradcorrect](https://github.com/khanlab/gradcorrect)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)
