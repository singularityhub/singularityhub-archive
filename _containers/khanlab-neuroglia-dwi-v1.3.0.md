---
id: 2875
name: "khanlab/neuroglia-dwi"
branch: "master"
tag: "v1.3.0"
commit: "ce8fca3beb071e530d2a62b6d9f2b7394f004a18"
version: "cc860626c15818d754f903841327e777"
build_date: "2018-05-22T18:24:28.102Z"
size_mb: 12104
size: 4750815263
sif: "https://datasets.datalad.org/shub/khanlab/neuroglia-dwi/v1.3.0/2018-05-22-ce8fca3b-cc860626/cc860626c15818d754f903841327e777.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/khanlab/neuroglia-dwi/v1.3.0/2018-05-22-ce8fca3b-cc860626/
recipe: https://datasets.datalad.org/shub/khanlab/neuroglia-dwi/v1.3.0/2018-05-22-ce8fca3b-cc860626/Singularity
collection: khanlab/neuroglia-dwi
---

# khanlab/neuroglia-dwi:v1.3.0

```bash
$ singularity pull shub://khanlab/neuroglia-dwi:v1.3.0
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: khanlab/neuroglia-core:v1.3.0


%labels
Maintainer "Ali Khan"

#########
%setup
#########
mkdir -p $SINGULARITY_ROOTFS/src
cp -Rv . $SINGULARITY_ROOTFS/src

#########
%post
#########


export DEBIAN_FRONTEND=noninteractive
cd /src/install_scripts
bash 21.install_MRtrix3_by_source_sudo.sh /opt
bash 28.install_camino_by_source.sh /opt
bash 29.install_unring_by_binary.sh /opt
bash 30.install_dke_by_binary.sh /opt

rm -rf /src

#########
%environment


#MRtrix3
export PATH=/opt/mrtrix3/bin:$PATH


#camino
export PATH=/opt/camino/bin:$PATH
export LD_LIBRARY_PATH=/opt/camino/lib:$LD_LIBRARY_PATH
export MANPATH=/opt/camino/lib:$MANPATH
export CAMINO_HEAP_SIZE=32000

#unring
export PATH=/opt/unring/bin:$PATH


#dke
export PATH=/opt/dke:$PATH
export LC_ALL=C
```

## Collection

 - Name: [khanlab/neuroglia-dwi](https://github.com/khanlab/neuroglia-dwi)
 - License: None

