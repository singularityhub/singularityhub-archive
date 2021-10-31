---
id: 2655
name: "khanlab/gradcorrect"
branch: "master"
tag: "0.0.1f"
commit: "60e99d15774c2c8dff148fa6bbd3c824fa3323f2"
version: "187457d3b3d0247657ca4185f244b39b"
build_date: "2018-04-26T16:28:56.903Z"
size_mb: 4238
size: 1577885727
sif: "https://datasets.datalad.org/shub/khanlab/gradcorrect/0.0.1f/2018-04-26-60e99d15-187457d3/187457d3b3d0247657ca4185f244b39b.simg"
url: https://datasets.datalad.org/shub/khanlab/gradcorrect/0.0.1f/2018-04-26-60e99d15-187457d3/
recipe: https://datasets.datalad.org/shub/khanlab/gradcorrect/0.0.1f/2018-04-26-60e99d15-187457d3/Singularity
collection: khanlab/gradcorrect
---

# khanlab/gradcorrect:0.0.1f

```bash
$ singularity pull shub://khanlab/gradcorrect:0.0.1f
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
bash 16.install_ants_by_binary.sh /opt
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

#ants
export PATH=/opt/ants:$PATH
export ANTSPATH=/opt/ants


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

