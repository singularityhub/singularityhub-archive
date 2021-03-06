---
id: 4600
name: "aces/cbrain-containers-recipes"
branch: "master"
tag: "freesurfer_v5.3"
commit: "83b9287b742619b7dc864fbe24b160fecb8a262e"
version: "1b2368e33161f7ec4fdde5dc83b877e0"
build_date: "2018-08-31T19:20:29.115Z"
size_mb: 7867
size: 4016381983
sif: "https://datasets.datalad.org/shub/aces/cbrain-containers-recipes/freesurfer_v5.3/2018-08-31-83b9287b-1b2368e3/1b2368e33161f7ec4fdde5dc83b877e0.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/aces/cbrain-containers-recipes/freesurfer_v5.3/2018-08-31-83b9287b-1b2368e3/
recipe: https://datasets.datalad.org/shub/aces/cbrain-containers-recipes/freesurfer_v5.3/2018-08-31-83b9287b-1b2368e3/Singularity
collection: aces/cbrain-containers-recipes
---

# aces/cbrain-containers-recipes:freesurfer_v5.3

```bash
$ singularity pull shub://aces/cbrain-containers-recipes:freesurfer_v5.3
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:trusty

#######################################################
#                                                     #
# MCIN (McGill Centre for Integrative Neuroscience)   #
#                                                     #
# Singularity recipe for FreeSurfer 5.3               #
# to build a container                                #
# used in CBRAIN (https://github.com/aces/cbrain)     #
#                                                     #
#######################################################

%labels
  Maintainer Natacha Beck

%help
This container provides FreeSurfer 5.3.
To run FreeSurfer you should have a personal license installed under $FREESURFER_HOME.

%post
  apt-get update
  apt-get -y install tcsh tar wget libgomp1 perl-modules bc
  wget -N -qO- ftp://surfer.nmr.mgh.harvard.edu/pub/dist/freesurfer/5.3.0/freesurfer-Linux-centos4_x86_64-stable-pub-v5.3.0.tar.gz | tar -xzv -C /opt
  chmod a+w /opt/freesurfer

%environment
OS=Linux
FS_OVERRIDE=0
FIX_VERTEX_AREA= 
FSF_OUTPUT_FORMAT=nii.gz
MNI_DIR=/opt/freesurfer/mni
LOCAL_DIR=/opt/freesurfer/local
FREESURFER_HOME=/opt/freesurfer
FSFAST_HOME=/opt/freesurfer/fsfast
MINC_BIN_DIR=/opt/freesurfer/mni/bin
MINC_LIB_DIR=/opt/freesurfer/mni/lib
MNI_DATAPATH=/opt/freesurfer/mni/data
FMRI_ANALYSIS_DIR=/opt/freesurfer/fsfast
PERL5LIB=/opt/freesurfer/mni/lib/perl5/5.8.5
MNI_PERL5LIB=/opt/freesurfer/mni/lib/perl5/5.8.5
PATH=/opt/freesurfer/bin:/opt/freesurfer/fsfast/bin:/opt/freesurfer/tktools:/opt/freesurfer/mni/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

export OS FS_OVERRIDE FIX_VERTEX_AREA FSF_OUTPUT_FORMAT MNI_DIR LOCAL_DIR FREESURFER_HOME FSFAST_HOME MINC_BIN_DIR MINC_LIB_DIR MNI_DATAPATH FMRI_ANALYSIS_DIR PERL5LIB MNI_PERL5LIB PATH
```

## Collection

 - Name: [aces/cbrain-containers-recipes](https://github.com/aces/cbrain-containers-recipes)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

