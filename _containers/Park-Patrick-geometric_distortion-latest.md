---
id: 1058
name: "Park-Patrick/geometric_distortion"
branch: "master"
tag: "latest"
commit: "392126e96e4b1a39808f2f6f61a94c5776bcab00"
version: "b158ded89a9e7623ad52b6eff9e9d3b8"
build_date: "2017-12-07T15:25:40.582Z"
size_mb: 8372
size: 3120255007
sif: "https://datasets.datalad.org/shub/Park-Patrick/geometric_distortion/latest/2017-12-07-392126e9-b158ded8/b158ded89a9e7623ad52b6eff9e9d3b8.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/Park-Patrick/geometric_distortion/latest/2017-12-07-392126e9-b158ded8/
recipe: https://datasets.datalad.org/shub/Park-Patrick/geometric_distortion/latest/2017-12-07-392126e9-b158ded8/Singularity
collection: Park-Patrick/geometric_distortion
---

# Park-Patrick/geometric_distortion:latest

```bash
$ singularity pull shub://Park-Patrick/geometric_distortion:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:xenial

#########
%setup
#########
cp ./install_scripts/*.sh $SINGULARITY_ROOTFS

#########
%post
#########


export DEBIAN_FRONTEND=noninteractive
bash 00.install_basics_sudo.sh
bash 03.install_anaconda2_nipype_dcmstack_by_binary.sh /opt
bash 05.install_MCR.sh /opt v93 R2017b
bash 10.install_afni_fsl_sudo.sh
bash 15.install_freesurfer_minimal_by_binary.sh /opt
bash 16.install_ants_by_binary.sh /opt
bash 25.install_niftyreg_by_source.sh /opt
bash 25.install_niftyreg_by_git_source.sh /opt


#remove all install scripts
rm *.sh


#########
%environment

#export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

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

#niftyreg  - latest git (binaries with _git)
export LD_LIBRARY_PATH=/opt/niftyreg-git/lib:$LD_LIBRARY_PATH 
export PATH=/opt/niftyreg-git/bin:$PATH

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

 - Name: [Park-Patrick/geometric_distortion](https://github.com/Park-Patrick/geometric_distortion)
 - License: None

