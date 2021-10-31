---
id: 11894
name: "tin6150/ansys"
branch: "master"
tag: "latest"
commit: "6b9c89b12d5743fac1a605c44ec021535b5ba4eb"
version: "32cbf190941e082de7f322fa3020a353a52d0d1af7a9b016123c99f668cb3b2f"
build_date: "2020-01-03T00:10:57.102Z"
size_mb: 228.16015625
size: 239243264
sif: "https://datasets.datalad.org/shub/tin6150/ansys/latest/2020-01-03-6b9c89b1-32cbf190/32cbf190941e082de7f322fa3020a353a52d0d1af7a9b016123c99f668cb3b2f.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/tin6150/ansys/latest/2020-01-03-6b9c89b1-32cbf190/
recipe: https://datasets.datalad.org/shub/tin6150/ansys/latest/2020-01-03-6b9c89b1-32cbf190/Singularity
collection: tin6150/ansys
---

# tin6150/ansys:latest

```bash
$ singularity pull shub://tin6150/ansys:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nugent68/ansys-nersc:latest
#From: nvidia/cuda:10.2-runtime-centos7 #tmp test only
 

%post
	yum -y install xterm tmux screen zsh tcsh less vim

	[[ -d /opt ]] || mkdir /opt
	#cd /opt
	#wget --quiet https://www.ansys.com/download/software/ansys.tgz
	# OR, if just want to use the tgz that was already created, assuming no private content
	#wget --quiet https://download.dropbox/USERNAME/.../ansys.tgz

	#tar xfz ansys.tgz

	# hacks that maybe useful during development/troubleshooting 
	# outside the cluster where scratch is not available and still want to write files to it temporarily
	# 41274 is uid for hjohansen
	mkdir -p       /global/scratch/penugent
	chown -R 12645 /global/scratch/penugent
	mkdir -p       /global/scratch/hjohansen
	chown    41273 /global/scratch/hjohansen
	chown -R 12645:504 /opt

	
%runscript
	#TZ=PST8PDT /opt/ansys/bin/ansys $@
	TZ=PST8PDT /bin/bash

%help
	Please see https://github.com/tin6150/ansys 
    
# Pull container from singularity-hub: 
# singularity pull --name ansys.sif shub://tin6150/ansys
# run binary specified by container in %runscript
# ./ansys.sif


# manual build cmd if not using singularity-hub:
# sudo singularity build  ansys.sif Singularity 2>&1  | tee singularity_build.log
#
# older singularity 2.6 cmd:
# sudo singularity build --writable ansys.sif Singularity 2>&1  | tee singularity_build.log
# troubleshooting container by shelling into it:
# sudo singularity exec -w ansys.sif /bin/bash

# Dirac has Singularity 3.2
```

## Collection

 - Name: [tin6150/ansys](https://github.com/tin6150/ansys)
 - License: None

