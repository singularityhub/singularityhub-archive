---
id: 11066
name: "tin6150/CMAQ"
branch: "tin_521_docker"
tag: "latest"
commit: "421be3c3a46c84e673dd615745e8606f54cd2764"
version: "None"
build_date: "2021-03-19T16:06:56.980Z"
size_mb: None
size: 562749471
sif: "https://datasets.datalad.org/shub/tin6150/CMAQ/latest/2021-03-19-421be3c3-cd8c0d53/cd8c0d5381d39aa324518fba00dbf5ee.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/tin6150/CMAQ/latest/2021-03-19-421be3c3-cd8c0d53/
recipe: https://datasets.datalad.org/shub/tin6150/CMAQ/latest/2021-03-19-421be3c3-cd8c0d53/Singularity
collection: tin6150/CMAQ
---

# tin6150/CMAQ:latest

```bash
$ singularity pull shub://tin6150/CMAQ:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tin6150/cmaq

# Singularity def, wrap around docker tin6150/cmaq 

%post
	touch "_ROOT_DIR_OF_CONTAINER_" ## also is "_CURRENT_DIR_CONTAINER_BUILD" 
	date >> _ROOT_DIR_OF_CONTAINER_
	echo "Singularity def 2019.0902.2315" >> _ROOT_DIR_OF_CONTAINER_
	echo "Singularity def 2019.0929 (timestamp change only)" >> _ROOT_DIR_OF_CONTAINER_

	# docker run as root, but singularity may run as user, so adding these hacks here
	mkdir -p /global/scratch/tin
	mkdir -p /global/home/users/tin
	mkdir -p /home/tin
	chown    43143 /global/scratch/tin
	chown    43143 /global/home/users/tin
	chown -R 43143 /home/tin
	chown -R 43143 /home/username  # some oddities resulting from the cmaq make process ran in docker
	chown -R 43143 /opt
	chown -R 43143 /Downloads

%runscript
    #pgcc $@
    #pgf95 $@
    #/bin/tcsh
    #/bin/bash -i 
    source /etc/bashrc && /Downloads/CMAQ/CMAQ-4.5-ADJ-LAJB_tutorial/code/CMAQ-4.5-ADJ-LAJB/./built_gcc_gfortran_serial_SAPRC99ROS/bin/CCTM/cctm
	

%help
    EPA CMAQ, Lucas Bastein Adjon modesl, tryin to get them to work in a container, may not work yet.
    
# Pull and run via singularity-hub:
# singularity pull shub://tin6150/CMAQ
# singularity pull --name CMAQ_b0929.sif shub://tin6150/CMAQ
# singularity shell CMAQ_b0929.sif

# manual build cmd:
# sudo /opt/singularity-2.6/bin/singularity build --writable cmaq_b0902a.img Singularity 2>&1  | tee singularity_build.log
#
# eg run cmd on bofh w/ singularity 2.6.2:
#      /opt/singularity-2.6/bin/singularity run     cmaq_b0820a.img
# sudo /opt/singularity-2.6/bin/singularity exec -w cmaq_b0820a.img /bin/tcsh

# eg run cmd on lrc, singularity 2.6-dist (maybe locally compiled)
#      singularity shell -w -B /global/scratch/tin ./cmaq_b0902a.img
#

# vim: nosmartindent tabstop=4 noexpandtab shiftwidth=4
```

## Collection

 - Name: [tin6150/CMAQ](https://github.com/tin6150/CMAQ)
 - License: None

