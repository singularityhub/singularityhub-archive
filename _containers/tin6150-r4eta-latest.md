---
id: 12537
name: "tin6150/r4eta"
branch: "master"
tag: "latest"
commit: "83a8811781e2b6e6587303bf8a8e9650383046c1"
version: "6af14063468714767c0813750a4f1f7478ca71648df1afedafe79e8e08e716cc"
build_date: "2020-09-09T02:37:37.922Z"
size_mb: 2393.62890625
size: 2509901824
sif: "https://datasets.datalad.org/shub/tin6150/r4eta/latest/2020-09-09-83a88117-6af14063/6af14063468714767c0813750a4f1f7478ca71648df1afedafe79e8e08e716cc.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/tin6150/r4eta/latest/2020-09-09-83a88117-6af14063/
recipe: https://datasets.datalad.org/shub/tin6150/r4eta/latest/2020-09-09-83a88117-6af14063/Singularity
collection: tin6150/r4eta
---

# tin6150/r4eta:latest

```bash
$ singularity pull shub://tin6150/r4eta:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tin6150/r4eta

# vim: nosmartindent tabstop=4 noexpandtab shiftwidth=4

# Singularity def, wrap around docker tin6150/r4eta

# manual build cmd (singularity 3.2): 
# sudo SINGULARITY_TMPDIR=/global/scratch/tin/tmp singularity build --sandbox ./r4eta.sif Singularity 2>&1  | tee singularity_build.log
# sudo SINGULARITY_TMPDIR=/dev/shm singularity build --sandbox ./r4eta.sif Singularity 2>&1  | tee singularity_build.log
#
# manual build cmd (singularity 2.6): 
# sudo /opt/singularity-2.6/bin/singularity build --writable r4eta_b1219a.img Singularity 2>&1  | tee singularity_build.log
#
# eg run cmd on bofh w/ singularity 2.6.2:
#      /opt/singularity-2.6/bin/singularity run     r4eta_b1219a.img
# sudo /opt/singularity-2.6/bin/singularity exec -w r4eta_b1219a.img /bin/tcsh

# eg run cmd on lrc, singularity 2.6-dist (maybe locally compiled)
#      singularity shell -w -B /global/scratch/tin ./r4eta_b1219a.img
#
# dirac1 has singularity singularity-3.2.1-1.el7.x86_64 


%post
	touch "_ROOT_DIR_OF_CONTAINER_" ## also is "_CURRENT_DIR_CONTAINER_BUILD" 
	date     >> _ROOT_DIR_OF_CONTAINER_
	hostname >> _ROOT_DIR_OF_CONTAINER_
	echo "Singularity def 2020.0908.1717 HelloWorld" >> _ROOT_DIR_OF_CONTAINER_

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
	BUILD = 2020_0908_1717_helloWorld
	MAINTAINER = tin_at_lbl_dot_gov
	REFERENCES = "https://github.com/tin6150/r4eta"

%runscript
    #/bin/bash -i 
	R

	
## help is displayed by `singularity run-help ./myR`

%help
	R programming language env in a container, with many packages from CRAN
	Example run:
	Pull and run via singularity-hub:
	singularity pull --name myR shub://tin6150/r4eta
	./myR
	singularity exec myR /usr/bin/Rscript -e 'library()'
	singularity exec --bind  .:/mnt  myR  /usr/bin/Rscript  /mnt/helloWorld.R > output.txt
    Where helloWorld.R is in your current dir (on the host system)
	See README.rst for additional details.
	source:          https://github.com/tin6150/r4eta
	docker hub:      https://hub.docker.com/repository/docker/tin6150/r4eta
	singularity hub: https://singularity-hub.org/collections/4160
```

## Collection

 - Name: [tin6150/r4eta](https://github.com/tin6150/r4eta)
 - License: None

