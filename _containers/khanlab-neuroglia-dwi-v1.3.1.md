---
id: 2939
name: "khanlab/neuroglia-dwi"
branch: "master"
tag: "v1.3.1"
commit: "2e22aad74e2a1ac1039e0b26a29247eaa167dec9"
version: "c5ad887e5a3483ac3eba2cb2a2fdf076"
build_date: "2018-05-27T16:15:46.757Z"
size_mb: 15194
size: 6057144351
sif: "https://datasets.datalad.org/shub/khanlab/neuroglia-dwi/v1.3.1/2018-05-27-2e22aad7-c5ad887e/c5ad887e5a3483ac3eba2cb2a2fdf076.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/khanlab/neuroglia-dwi/v1.3.1/2018-05-27-2e22aad7-c5ad887e/
recipe: https://datasets.datalad.org/shub/khanlab/neuroglia-dwi/v1.3.1/2018-05-27-2e22aad7-c5ad887e/Singularity
collection: khanlab/neuroglia-dwi
---

# khanlab/neuroglia-dwi:v1.3.1

```bash
$ singularity pull shub://khanlab/neuroglia-dwi:v1.3.1
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: khanlab/neuroglia-core:v1.3.1


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

