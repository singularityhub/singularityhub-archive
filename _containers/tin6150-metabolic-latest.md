---
id: 11890
name: "tin6150/metabolic"
branch: "master"
tag: "latest"
commit: "617c1fa7b6239fddec1a636373b3093267ec07fe"
version: "763ed7d56a3eeaff8d0a88baf9f4d1af8bd2507fd89daf9d5d60676f2df75d23"
build_date: "2021-02-19T21:48:39.536Z"
size_mb: 6129.34765625
size: 6427086848
sif: "https://datasets.datalad.org/shub/tin6150/metabolic/latest/2021-02-19-617c1fa7-763ed7d5/763ed7d56a3eeaff8d0a88baf9f4d1af8bd2507fd89daf9d5d60676f2df75d23.sif"
url: https://datasets.datalad.org/shub/tin6150/metabolic/latest/2021-02-19-617c1fa7-763ed7d5/
recipe: https://datasets.datalad.org/shub/tin6150/metabolic/latest/2021-02-19-617c1fa7-763ed7d5/Singularity
collection: tin6150/metabolic
---

# tin6150/metabolic:latest

```bash
$ singularity pull shub://tin6150/metabolic:latest
```

## Singularity Recipe

```singularity
# Singularity definition file for METABOLIC, wrap around docker tin6150/metabolic
# vim: nosmartindent tabstop=4 noexpandtab shiftwidth=4

Bootstrap: docker
From: tin6150/metabolic

# manual build cmd (singularity 3.2): 
# sudo SINGULARITY_TMPDIR=/global/scratch/tin/tmp singularity build --sandbox ./metabolic.sif Singularity 2>&1  | tee singularity_build.log
# sudo SINGULARITY_TMPDIR=/dev/shm singularity build --sandbox ./metabolic.sif Singularity 2>&1  | tee singularity_build.log
#
# manual build cmd (singularity 2.6): 
# sudo /opt/singularity-2.6/bin/singularity build --writable metabolic_b1219a.img Singularity 2>&1  | tee singularity_build.log
#
# eg run cmd on bofh w/ singularity 2.6.2:
#      /opt/singularity-2.6/bin/singularity run     metabolic_b1219a.img
# sudo /opt/singularity-2.6/bin/singularity exec -w metabolic_b1219a.img /bin/tcsh

# eg run cmd on lrc, singularity 2.6-dist (maybe locally compiled)
#      singularity shell -w -B /global/scratch/tin ./metabolic_b1219a.img
#
# dirac1 has singularity singularity-3.2.1-1.el7.x86_64 

%post
	touch "_ROOT_DIR_OF_CONTAINER_" ## also is "_CURRENT_DIR_CONTAINER_BUILD" 
	date     >> _ROOT_DIR_OF_CONTAINER_
	hostname >> _ROOT_DIR_OF_CONTAINER_
	echo "Singularity def 2020.0109.2242" >> _ROOT_DIR_OF_CONTAINER_

	# docker run as root, but singularity may run as user, so adding these hacks here
	mkdir -p /global/scratch/tin
	mkdir -p /global/home/users/tin
	mkdir -p /home/tin
	mkdir -p /home/tmp
	mkdir -p /Downloads
	chown    43143 /global/scratch/tin
	chown    43143 /global/home/users/tin
	chown -R 43143 /home
	#chown -R 43143 /home/tin
	chown -R 43143 /opt
	chown -R 43143 /Downloads
	chmod 1777 /home/tmp

	# tmp add here till upstream container build is completed
    #apt-get -y --force-yes --quiet install libcurl4-openssl-dev  libxml2-dev libssl-dev httrack libhttrack-dev libhttrack2 harvest-tools git 
    #apt-get -y --quiet install bowtie2
	#/opt/conda/bin/conda install -y --quiet -v -c bioconda  gtdbtk   
	#/opt/conda/bin/pip install  gtdbtk   
	#Rscript --quiet -e 'install.packages("tidyverse", repos = "http://cran.us.r-project.org")' 
	Rscript --quiet -e 'library()' > R_library_list.out.txt.singularity 
    
%environment
	TZ=PST8PDT
	GTDBTK_DATA_PATH=/tmp/GTDBTK_DATA
	export TZ GTDBTK_DATA_PATH

%labels
	BUILD = 2019_0109_2242
	MAINTAINER = tin_at_lbl_dot_gov
	REFERENCES = "https://github.com/tin6150/metabolic https://github.com/AnantharamanLab/METABOLIC"

%runscript
    #TZ=PST8PDT /bin/tcsh
    #/bin/bash -i 
    #xx source /etc/bashrc && /Downloads/CMAQ/CMAQ-4.5-ADJ-LAJB_tutorial/code/CMAQ-4.5-ADJ-LAJB/./built_gcc_gfortran_serial_SAPRC99ROS/bin/CCTM/cctm
	LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/opt/conda/lib PATH=${PATH}:/opt/conda/bin /bin/bash -i

	

%help
    Metabolic from https://github.com/AnantharamanLab/METABOLIC
    
	Pull and run via singularity-hub:
	singularity pull --name metabolic.sif shub://tin6150/metabolic
	singularity shell metabolic.sif
```

## Collection

 - Name: [tin6150/metabolic](https://github.com/tin6150/metabolic)
 - License: None

