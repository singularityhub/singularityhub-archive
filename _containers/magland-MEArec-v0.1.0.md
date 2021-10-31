---
id: 4994
name: "magland/MEArec"
branch: "master"
tag: "v0.1.0"
commit: "bb43b0695f5fc4729c77c42876dc6631646eb52d"
version: "5af59ecb55cdb87d0a9d81ee57dcbada"
build_date: "2018-09-26T15:44:58.301Z"
size_mb: 2591
size: 1115738143
sif: "https://datasets.datalad.org/shub/magland/MEArec/v0.1.0/2018-09-26-bb43b069-5af59ecb/5af59ecb55cdb87d0a9d81ee57dcbada.simg"
url: https://datasets.datalad.org/shub/magland/MEArec/v0.1.0/2018-09-26-bb43b069-5af59ecb/
recipe: https://datasets.datalad.org/shub/magland/MEArec/v0.1.0/2018-09-26-bb43b069-5af59ecb/Singularity
collection: magland/MEArec
---

# magland/MEArec:v0.1.0

```bash
$ singularity pull shub://magland/MEArec:v0.1.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
FROM: continuumio/miniconda3

%labels
    Maintainer Jeremy Magland

%setup
  mkdir ${SINGULARITY_ROOTFS}/working
  cp -r . ${SINGULARITY_ROOTFS}/working/src

%post
  echo "################################## Activating conda environment"
  . /opt/conda/etc/profile.d/conda.sh
  conda create -n mountainlab
  conda activate mountainlab

  echo "################################## Installing MountainLab"
  conda install -c flatiron -c conda-forge mountainlab mountainlab_pytools mlprocessors

  echo "################################## Testing installation"
  ml-list-processors

  # Install MEAutility
  git clone https://github.com/alejoe91/MEAutility /working/MEAutility
  cd /working/MEAutility && python setup.py install

  echo "################################## Installing ML package"
  pip install -r /working/src/ml_requirements.txt
  ln -s /working/src `ml-config package_directory`/ml_mearec

  echo "################################## Testing package"
  ml-spec --lock
  ml-spec -p mearec.gen_spiketrains
  ml-spec -p mearec.gen_recording

%environment
  . /opt/conda/etc/profile.d/conda.sh
  conda activate mountainlab
```

## Collection

 - Name: [magland/MEArec](https://github.com/magland/MEArec)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

