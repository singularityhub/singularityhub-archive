---
id: 9830
name: "rainsworth/idia-container-jupytercasa"
branch: "master"
tag: "latest"
commit: "2587145cd86d165bc50988d0e41deb6c2b866c5b"
version: "6606159de61a9f72e3550cf6ebaf0da1"
build_date: "2019-06-17T19:35:32.441Z"
size_mb: 3262
size: 1351475231
sif: "https://datasets.datalad.org/shub/rainsworth/idia-container-jupytercasa/latest/2019-06-17-2587145c-6606159d/6606159de61a9f72e3550cf6ebaf0da1.simg"
url: https://datasets.datalad.org/shub/rainsworth/idia-container-jupytercasa/latest/2019-06-17-2587145c-6606159d/
recipe: https://datasets.datalad.org/shub/rainsworth/idia-container-jupytercasa/latest/2019-06-17-2587145c-6606159d/Singularity
collection: rainsworth/idia-container-jupytercasa
---

# rainsworth/idia-container-jupytercasa:latest

```bash
$ singularity pull shub://rainsworth/idia-container-jupytercasa:latest
```

## Singularity Recipe

```singularity
# URL: https://github.com/aardk/jupyter-casa
# Definition file for IDIA Jupyter Casa 
BootStrap: docker
From: penngwyn/jupytercasa

%runscript
	#!/bin/sh
	/usr/bin/python "$@"
%post 
	# Install some software 
	apt-get -y install wget vim python-pip 
	
	# Bind through IDIA volumes to the container
	mkdir /users /scratch /data

%environment 
	PYTHONPATH="/home/jupyter/.local/lib/python2.7/site-packages/:/usr/local/lib/python2.7/site-packages:/usr/local/casa/linux64/python/2.7"
	LD_LIBRARY_PATH="/usr/local/casa/linux64/lib" 
	CASAPATH="/usr/local/casa/ linux64" 
	PATH="/usr/local/casa/linux64/bin:$PATH"
```

## Collection

 - Name: [rainsworth/idia-container-jupytercasa](https://github.com/rainsworth/idia-container-jupytercasa)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

