---
id: 3199
name: "khanlab/neuroglia-core"
branch: "master"
tag: "v1.3.2"
commit: "99caa839adc54a5ea97ce584881522d4b441e4ef"
version: "b110565de9a02f2f64de79f19636ec3a"
build_date: "2018-06-18T15:24:57.618Z"
size_mb: 14389
size: 5796155423
sif: "https://datasets.datalad.org/shub/khanlab/neuroglia-core/v1.3.2/2018-06-18-99caa839-b110565d/b110565de9a02f2f64de79f19636ec3a.simg"
url: https://datasets.datalad.org/shub/khanlab/neuroglia-core/v1.3.2/2018-06-18-99caa839-b110565d/
recipe: https://datasets.datalad.org/shub/khanlab/neuroglia-core/v1.3.2/2018-06-18-99caa839-b110565d/Singularity
collection: khanlab/neuroglia-core
---

# khanlab/neuroglia-core:v1.3.2

```bash
$ singularity pull shub://khanlab/neuroglia-core:v1.3.2
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: neurodebian:stretch-non-free
#From: debian:stretch-20180426
#From: continuumio/miniconda:4.4.10
#From: ubuntu:xenial-20171201



#note: install_afni_fsl_sudo.sh solves error message when run itksnap: LibGlu.so.1

#run freesurfer's freeview 
# if libQtOpenGL.so.4, run sudo apt-get libqt4-dev
# if missing:  libjpeg.so.62, run apt-get install libjpeg62

#create image
#rm ~/neuroglia/neuroglia.img && singularity create  --size 20000 ~/neuroglia/neuroglia.img && sudo singularity bootstrap ~/neuroglia/neuroglia.img Singularity

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
bash 03.install_anaconda2_nipype_dcmstack_by_binary.sh /opt
bash 04.install_octave_sudo.sh 
bash 10.install_afni_fsl_sudo.sh
python fslinstaller.py -d /opt/fsl
bash 12.install_c3d_by_binary.sh /opt
bash 15.install_freesurfer_minimal_by_binary.sh /opt
bash 16.install_ants_by_binary.sh /opt
bash 17.install_dcm2niix_by_binary.sh /opt
bash 23.install_heudiconv_by_source.sh /opt
bash 24.install_bids-validator_sudo.sh
bash 25.install_niftyreg_by_source.sh /opt
bash 28.install_gradunwarp_by_source.sh /opt


#remove all install scripts
rm -rf /src


#########
%environment

#export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

#anaconda2
export PATH=/opt/anaconda2/bin/:$PATH

#c3d
export PATH=/opt/c3d/bin:$PATH
#leave out deps for c3d gui to avoid conflicts
#export LD_LIBRARY_PATH=/opt/c3d/lib/c3d_gui-1.1.0:$LD_LIBRARY_PATH 

#itksnap
#export PATH=/opt/itksnap/bin:$PATH
#export LD_LIBRARY_PATH=/opt/itksnap/lib/snap-3.6.0:$LD_LIBRARY_PATH

#dicom_retrieve.py use dcm4che's getscu. So, put dcm4che's PATH before dcmtk's PATH
#dcm4che
#export PATH=/opt/dcm4che-3.3.8/bin:$PATH


#fsl
export FSLDIR=/opt/fsl
export POSSUMDIR=$FSLDIR
export PATH=$FSLDIR/bin:$PATH
export FSLOUTPUTTYPE=NIFTI_GZ
export FSLMULTIFILEQUIT=TRUE
export FSLTCLSH=/usr/bin/tclsh
export FSLWISH=/usr/bin/wish
export FSLBROWSER=/etc/alternatives/x-www-browser
export LD_LIBRARY_PATH=$FSLDIR/lib:${LD_LIBRARY_PATH}


#ants
export PATH=/opt/ants:$PATH
export ANTSPATH=/opt/ants

#dcm2niix
export PATH=/opt/mricrogl_lx:$PATH

#heudiconv
export PYTHONPATH=/opt/heudiconv:$PYTHONPATH

#niftyreg
export LD_LIBRARY_PATH=/opt/niftyreg-1.3.9/lib:$LD_LIBRARY_PATH 
export PATH=/opt/niftyreg-1.3.9/bin:$PATH

#matlab on graham (requires user to be on sharcnet matlab users list)
export JAVA_HOME=/cvmfs/soft.computecanada.ca/easybuild/software/2017/Core/java/1.8.0_121
export MLM_LICENSE_FILE=/cvmfs/restricted.computecanada.ca/config/licenses/matlab/inst_uwo/graham.lic
export PATH=/cvmfs/restricted.computecanada.ca/easybuild/software/2017/Core/matlab/2017a:/cvmfs/restricted.computecanada.ca/easybuild/software/2017/Core/matlab/2017a/bin:/cvmfs/soft.computecanada.ca/easybuild/software/2017/Core/java/1.8.0_121:/cvmfs/soft.computecanada.ca/easybuild/software/2017/Core/java/1.8.0_121/bin:$PATH
export _JAVA_OPTIONS=-Xmx256m
export LIBRARY_PATH=/cvmfs/soft.computecanada.ca/easybuild/software/2017/Core/java/1.8.0_121/lib

#freesurfer - minimal
export FREESURFER_HOME=/opt/freesurfer_minimal
export PATH=$FREESURFER_HOME/bin:$PATH
```

## Collection

 - Name: [khanlab/neuroglia-core](https://github.com/khanlab/neuroglia-core)
 - License: None

