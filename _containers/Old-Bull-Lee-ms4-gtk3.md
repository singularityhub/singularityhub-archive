---
id: 5632
name: "Old-Bull-Lee/ms4"
branch: "master"
tag: "gtk3"
commit: "ccf0023c58155d31d9212f53e61a64b5a31e755d"
version: "e22c34cf71389b589ea6d04f6ce827a2"
build_date: "2018-11-17T04:47:35.232Z"
size_mb: 4175
size: 1755336735
sif: "https://datasets.datalad.org/shub/Old-Bull-Lee/ms4/gtk3/2018-11-17-ccf0023c-e22c34cf/e22c34cf71389b589ea6d04f6ce827a2.simg"
url: https://datasets.datalad.org/shub/Old-Bull-Lee/ms4/gtk3/2018-11-17-ccf0023c-e22c34cf/
recipe: https://datasets.datalad.org/shub/Old-Bull-Lee/ms4/gtk3/2018-11-17-ccf0023c-e22c34cf/Singularity
collection: Old-Bull-Lee/ms4
---

# Old-Bull-Lee/ms4:gtk3

```bash
$ singularity pull shub://Old-Bull-Lee/ms4:gtk3
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
  apt-get install libgtk-3-0 -y


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

