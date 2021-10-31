---
id: 2639
name: "khanlab/gradcorrect"
branch: "master"
tag: "0.0.1e"
commit: "9e43784f1eb190351cd3191a6bbaa4bfeb89502b"
version: "4aa2efcf372e73376479d7cfb7c981c3"
build_date: "2018-04-25T06:48:58.548Z"
size_mb: 4237
size: 1577865247
sif: "https://datasets.datalad.org/shub/khanlab/gradcorrect/0.0.1e/2018-04-25-9e43784f-4aa2efcf/4aa2efcf372e73376479d7cfb7c981c3.simg"
url: https://datasets.datalad.org/shub/khanlab/gradcorrect/0.0.1e/2018-04-25-9e43784f-4aa2efcf/
recipe: https://datasets.datalad.org/shub/khanlab/gradcorrect/0.0.1e/2018-04-25-9e43784f-4aa2efcf/Singularity
collection: khanlab/gradcorrect
---

# khanlab/gradcorrect:0.0.1e

```bash
$ singularity pull shub://khanlab/gradcorrect:0.0.1e
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

