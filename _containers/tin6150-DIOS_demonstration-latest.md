---
id: 14087
name: "tin6150/DIOS_demonstration"
branch: "tin"
tag: "latest"
commit: "047e4cb713c3d2fc23241e4911730cdbe08c1381"
version: "16126427ebd23145fc792f6e139823290b73eed470e3021ca712e02ec50f37be"
build_date: "2020-09-29T17:53:42.408Z"
size_mb: 1873.2109375
size: 1964204032
sif: "https://datasets.datalad.org/shub/tin6150/DIOS_demonstration/latest/2020-09-29-047e4cb7-16126427/16126427ebd23145fc792f6e139823290b73eed470e3021ca712e02ec50f37be.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/tin6150/DIOS_demonstration/latest/2020-09-29-047e4cb7-16126427/
recipe: https://datasets.datalad.org/shub/tin6150/DIOS_demonstration/latest/2020-09-29-047e4cb7-16126427/Singularity
collection: tin6150/DIOS_demonstration
---

# tin6150/DIOS_demonstration:latest

```bash
$ singularity pull shub://tin6150/DIOS_demonstration:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tin6150/r4envids

# This is a Singularity def for DIOS demonstration 

# Example run for the DIOS demonstration using Singularity Container 
# singularity pull shub://tin6150/DIOS_demonstration
# singularity exec DIOS_demonstration_latest.sif /usr/bin/Rscript  /DIOS_demonstration/code/DIOS_demonstration.R  2>&1 | tee output.log


#	Advance usage or future tweak of this container:
#	Alternate example run:
# 	Pull and run via singularity-hub:
#	singularity pull --name R shub://tin6150/DIOS_demonstration
#	./R
#	singularity exec R /usr/bin/Rscript -e 'library()'
#	singularity exec --bind  .:/mnt  R  /usr/bin/Rscript  /mnt/helloWorld.R > output.txt
#   Where helloWorld.R is in your current dir (on the host system)

#	LINKS
#	git repo:        https://github.com/tin6150/DIOS_demonstration # tin branch for now
#	docker hub:      https://hub.docker.com/repository/docker/tin6150/r4envids
#	singularity hub: https://singularity-hub.org/collections/4713

 
# manual build cmd (singularity 3.6.1): 
# sudo SINGULARITY_TMPDIR=/tmp  singularity build --sandbox ./r4envids.sif Singularity 2>&1  | tee singularity_build.log


%post
	touch "_ROOT_DIR_OF_CONTAINER_" ## also is "_CURRENT_DIR_CONTAINER_BUILD" 
	date     >> _ROOT_DIR_OF_CONTAINER_
	hostname >> _ROOT_DIR_OF_CONTAINER_
	echo "Singularity def 2020.0910.1437 procps" >> _ROOT_DIR_OF_CONTAINER_
	echo "Singularity def 2020.0918.1501 R::snow" >> _ROOT_DIR_OF_CONTAINER_
	echo "Singularity def 2020.0927.2147 _par   " >> _ROOT_DIR_OF_CONTAINER_

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

    
%environment
	TZ=PST8PDT
	export TZ 

%labels
	BUILD = 2020_0927_2147_par
	MAINTAINER = tin_at_berkeley_edu
	REFERENCES = "https://github.com/tin6150/r4"

%runscript
    #/bin/bash -i 
	R

	
# `singularity run-help $CONTAINER_NAME` will show info below
%help
	Example run for the DIOS demonstration using Singularity Container 
	singularity pull shub://tin6150/DIOS_demonstration
	singularity exec --bind .:/mnt DIOS_demonstration_latest.sif bash -c "cd /mnt/code && /usr/bin/Rscript  ./DIOS_demonstration.R"  2>&1 | tee output.log

# vim: noexpandtab nosmarttab noautoindent nosmartindent tabstop=4 shiftwidth=4 paste formatoptions-=cro
```

## Collection

 - Name: [tin6150/DIOS_demonstration](https://github.com/tin6150/DIOS_demonstration)
 - License: None

