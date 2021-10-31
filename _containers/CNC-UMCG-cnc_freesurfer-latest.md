---
id: 2283
name: "CNC-UMCG/cnc_freesurfer"
branch: "master"
tag: "latest"
commit: "cc126bf21e2212ffdfe94644e4c089240395e524"
version: "e0484e3389a382f68b23bd161c2d749e"
build_date: "2018-03-26T10:14:22.646Z"
size_mb: 7236
size: 2987237407
sif: "https://datasets.datalad.org/shub/CNC-UMCG/cnc_freesurfer/latest/2018-03-26-cc126bf2-e0484e33/e0484e3389a382f68b23bd161c2d749e.simg"
url: https://datasets.datalad.org/shub/CNC-UMCG/cnc_freesurfer/latest/2018-03-26-cc126bf2-e0484e33/
recipe: https://datasets.datalad.org/shub/CNC-UMCG/cnc_freesurfer/latest/2018-03-26-cc126bf2-e0484e33/Singularity
collection: CNC-UMCG/cnc_freesurfer
---

# CNC-UMCG/cnc_freesurfer:latest

```bash
$ singularity pull shub://CNC-UMCG/cnc_freesurfer:latest
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: CNC-UMCG/cnc_base


%post

	apt-get update \
	    && apt-get install -y wget
	wget -qO- https://surfer.nmr.mgh.harvard.edu/pub/dist/freesurfer/6.0.1/freesurfer-Linux-centos6_x86_64-stable-pub-v6.0.1.tar.gz | tar zxv --no-same-owner -C /opt \
	    --exclude='freesurfer/trctrain' \
	    --exclude='freesurfer/subjects/fsaverage_sym' \
	    --exclude='freesurfer/subjects/fsaverage3' \
	    --exclude='freesurfer/subjects/fsaverage4' \
	    --exclude='freesurfer/subjects/fsaverage5' \
	    --exclude='freesurfer/subjects/fsaverage6' \
	    --exclude='freesurfer/subjects/cvs_avg35' \
	    --exclude='freesurfer/subjects/cvs_avg35_inMNI152' \
	    --exclude='freesurfer/subjects/bert' \
	    --exclude='freesurfer/subjects/V1_average' \
	    --exclude='freesurfer/average/mult-comp-cor' \
	    --exclude='freesurfer/lib/cuda' \
	    --exclude='freesurfer/lib/qt'

	apt-get install -y python3
	apt-get install -y python3-pip
	pip3 install nibabel pandas
	apt-get install -y python2.7
	apt-get install -y python-pip

	apt-get install -y tcsh
	apt-get install -y bc
	apt-get install -y tar libgomp1 perl-modules

	apt-get install -y curl
	curl -sL https://deb.nodesource.com/setup_6.x | bash -
	apt-get install -y nodejs
	npm install -g bids-validator@0.19.8

	# Configure environment
	FSLDIR=/usr/share/fsl/5.0
	FSLOUTPUTTYPE=NIFTI_GZ
	PATH=/usr/lib/fsl/5.0:$PATH
	FSLMULTIFILEQUIT=TRUE
	POSSUMDIR=/usr/share/fsl/5.0
	LD_LIBRARY_PATH=/usr/lib/fsl/5.0:$LD_LIBRARY_PATH
	FSLTCLSH=/usr/bin/tclsh
	FSLWISH=/usr/bin/wish
	FSLOUTPUTTYPE=NIFTI_GZ

#ENV SUBJECTS_DIR /opt/freesurfer/subjects
#ENV FSF_OUTPUT_FORMAT nii.gz
#ENV MNI_DIR /opt/freesurfer/mni
#ENV LOCAL_DIR /opt/freesurfer/local
#ENV FREESURFER_HOME /opt/freesurfer
#ENV FSFAST_HOME /opt/freesurfer/fsfast
#ENV MINC_BIN_DIR /opt/freesurfer/mni/bin
#ENV MINC_LIB_DIR /opt/freesurfer/mni/lib
#ENV MNI_DATAPATH /opt/freesurfer/mni/data
#ENV FMRI_ANALYSIS_DIR /opt/freesurfer/fsfast
#ENV PERL5LIB /opt/freesurfer/mni/lib/perl5/5.8.5
#ENV MNI_PERL5LIB /opt/freesurfer/mni/lib/perl5/5.8.5
#ENV PATH /opt/freesurfer/bin:/opt/freesurfer/fsfast/bin:/opt/freesurfer/tktools:/opt/freesurfer/mni/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
#ENV PYTHONPATH=""

	mkdir /scratch
	mkdir /local-scratch

#	run.py /run.py
#	chmod +x /run.py

#	version /version

#ENTRYPOINT ["/run.py"]
```

## Collection

 - Name: [CNC-UMCG/cnc_freesurfer](https://github.com/CNC-UMCG/cnc_freesurfer)
 - License: None

