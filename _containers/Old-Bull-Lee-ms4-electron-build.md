---
id: 5649
name: "Old-Bull-Lee/ms4"
branch: "master"
tag: "electron-build"
commit: "0606228ee50c5e138f2cff9c6e6b0ad8e8f3a4f8"
version: "36be5cb6e959ec7e5618d3335be28f5c"
build_date: "2018-12-14T05:20:14.972Z"
size_mb: 5275
size: 2117181471
sif: "https://datasets.datalad.org/shub/Old-Bull-Lee/ms4/electron-build/2018-12-14-0606228e-36be5cb6/36be5cb6e959ec7e5618d3335be28f5c.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/Old-Bull-Lee/ms4/electron-build/2018-12-14-0606228e-36be5cb6/
recipe: https://datasets.datalad.org/shub/Old-Bull-Lee/ms4/electron-build/2018-12-14-0606228e-36be5cb6/Singularity
collection: Old-Bull-Lee/ms4
---

# Old-Bull-Lee/ms4:electron-build

```bash
$ singularity pull shub://Old-Bull-Lee/ms4:electron-build
```

## Singularity Recipe

```singularity
Bootstrap: docker
FROM: continuumio/miniconda3:latest

%labels
    Maintainer Jeremy Magland
    Version 0.1.0
    InstalledBy Michael Montgomery
    TestedOn hpc.arizona.edu (with errors)(unsolved, as yet)
    

%setup

%post
  echo "#################### update & install GTK+3.0"
  
  apt-get update -y && apt-get upgrade -y
  apt-get install build-essential clang libdbus-1-dev libgtk-3-dev \
                       libnotify-dev libgnome-keyring-dev libgconf2-dev \
                       libasound2-dev libcap-dev libcups2-dev libxtst-dev \
                       libxss1 libnss3-dev gcc-multilib g++-multilib curl \
                       gperf bison python-dbusmock -y


  echo "################################## Activating conda environment"
  . /opt/conda/etc/profile.d/conda.sh
  conda create -n mountainlab
  conda activate mountainlab

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

  echo "################################# modify fontconfig to fix bug"
  conda install -c conda-forge fontconfig==2.12.6

  echo "################################## Installing Python"
  conda install python=3.6
  
  echo "################################## Testing installation"
  ml-list-processors

%environment
  . /opt/conda/etc/profile.d/conda.sh
  conda activate mountainlab
```

## Collection

 - Name: [Old-Bull-Lee/ms4](https://github.com/Old-Bull-Lee/ms4)
 - License: None

