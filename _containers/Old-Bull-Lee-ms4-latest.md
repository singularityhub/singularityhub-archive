---
id: 5375
name: "Old-Bull-Lee/ms4"
branch: "master"
tag: "latest"
commit: "9e930c3310b740d8079a5bf840f4a7aad092cf6e"
version: "e258729d5a18ffcc0882f4c3ab9a2299"
build_date: "2019-02-19T02:46:13.379Z"
size_mb: 4757
size: 2006634527
sif: "https://datasets.datalad.org/shub/Old-Bull-Lee/ms4/latest/2019-02-19-9e930c33-e258729d/e258729d5a18ffcc0882f4c3ab9a2299.simg"
url: https://datasets.datalad.org/shub/Old-Bull-Lee/ms4/latest/2019-02-19-9e930c33-e258729d/
recipe: https://datasets.datalad.org/shub/Old-Bull-Lee/ms4/latest/2019-02-19-9e930c33-e258729d/Singularity
collection: Old-Bull-Lee/ms4
---

# Old-Bull-Lee/ms4:latest

```bash
$ singularity pull shub://Old-Bull-Lee/ms4:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
FROM: continuumio/miniconda3:latest

%labels
    Maintainer Jeremy Magland
    Version 0.1.0
    InstalledBy Michael Montgomery


%setup

%post
  echo "############## apt-get update & install (misc)"
  
  apt-get update -y && apt-get upgrade -y
  apt-get install apt-utils build-essential \
  	  	  libgtk-3-0 \
		  libxss1 \
		  libgconf-2-4 \
		  libnss3 \
		  libasound2 -y

#  	  	       clang libdbus-1-dev libgtk-3-dev \
#		       libnotify-dev libgnome-keyring-dev libgconf2-dev \
#                       libasound2-dev libcap-dev libcups2-dev libxtst-dev \
#                       libxss1 libnss3-dev gcc-multilib g++-multilib curl \
#                       gperf bison python-dbusmock -y

  echo "############## install nodejs #############"
  curl -sL https://deb.nodesource.com/setup_11.x | bash -
  apt-get install -y nodejs

  echo "############## install electronjs #########"
  npm i -D electron@latest

  echo "################################## Activating conda environment"
  . /opt/conda/etc/profile.d/conda.sh
  conda create -n mountainlab
  conda activate mountainlab

  echo "################################## Installing Python"
  conda install python=3.6

  echo "################################## Installing MountainLab"
  conda install -c flatiron -c conda-forge \
  		   	    mountainlab \
			    mountainlab_pytools \
			    ml_ephys \
			    ephys-viz \
			    ml_ms3 \
			    ml_ms4alg \
			    ml_pyms \
			    qt-mountainview

#  echo "################################# modify fontconfig to fix bug"
  conda install -c conda-forge fontconfig==2.12.6
  
  echo "################################## Testing installation"
  ml-list-processors

%environment
  . /opt/conda/etc/profile.d/conda.sh
  conda activate mountainlab
```

## Collection

 - Name: [Old-Bull-Lee/ms4](https://github.com/Old-Bull-Lee/ms4)
 - License: None

