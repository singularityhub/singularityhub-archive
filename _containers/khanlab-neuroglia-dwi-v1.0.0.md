---
id: 1332
name: "khanlab/neuroglia-dwi"
branch: "master"
tag: "v1.0.0"
commit: "3ddbab47edadee2e23f354ef6eccaffd76c8bd08"
version: "807eb232a31ec96724bf07163ec5073b"
build_date: "2018-01-17T03:51:06.623Z"
size_mb: 7115
size: 2597138463
sif: "https://datasets.datalad.org/shub/khanlab/neuroglia-dwi/v1.0.0/2018-01-17-3ddbab47-807eb232/807eb232a31ec96724bf07163ec5073b.simg"
url: https://datasets.datalad.org/shub/khanlab/neuroglia-dwi/v1.0.0/2018-01-17-3ddbab47-807eb232/
recipe: https://datasets.datalad.org/shub/khanlab/neuroglia-dwi/v1.0.0/2018-01-17-3ddbab47-807eb232/Singularity
collection: khanlab/neuroglia-dwi
---

# khanlab/neuroglia-dwi:v1.0.0

```bash
$ singularity pull shub://khanlab/neuroglia-dwi:v1.0.0
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: khanlab/neuroglia-core:v1.0.0

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


cd /src

# checkout specific git release 
SINGULARITY_TAG=${SINGULARITY_BUILDDEF#Singularity.}
if [ ! "$SINGULARITY_TAG" = "Singularity" ]
then
  git checkout $SINGULARITY_TAG
fi

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
```

## Collection

 - Name: [khanlab/neuroglia-dwi](https://github.com/khanlab/neuroglia-dwi)
 - License: None

