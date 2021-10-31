---
id: 5645
name: "Old-Bull-Lee/ms4"
branch: "master"
tag: "xss"
commit: "40dd0ab4a5fba16910ca40247365f5998c5d88b7"
version: "189fe7c568b720c04f5b8dd1ae0dabd1"
build_date: "2018-11-19T20:38:17.880Z"
size_mb: 4175
size: 1755361311
sif: "https://datasets.datalad.org/shub/Old-Bull-Lee/ms4/xss/2018-11-19-40dd0ab4-189fe7c5/189fe7c568b720c04f5b8dd1ae0dabd1.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/Old-Bull-Lee/ms4/xss/2018-11-19-40dd0ab4-189fe7c5/
recipe: https://datasets.datalad.org/shub/Old-Bull-Lee/ms4/xss/2018-11-19-40dd0ab4-189fe7c5/Singularity
collection: Old-Bull-Lee/ms4
---

# Old-Bull-Lee/ms4:xss

```bash
$ singularity pull shub://Old-Bull-Lee/ms4:xss
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
  apt-get install libxss1 -y


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

