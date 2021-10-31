---
id: 1508
name: "akhanf/vasst-dev"
branch: "master"
tag: "v0.0.4a"
commit: "3cb139985932f0f6a0b1fb4f6c947fa60bbdd037"
version: "f184e003236feb495e490e3d49a5fd20"
build_date: "2018-01-30T16:28:23.274Z"
size_mb: 10985
size: 4666593311
sif: "https://datasets.datalad.org/shub/akhanf/vasst-dev/v0.0.4a/2018-01-30-3cb13998-f184e003/f184e003236feb495e490e3d49a5fd20.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/akhanf/vasst-dev/v0.0.4a/2018-01-30-3cb13998-f184e003/
recipe: https://datasets.datalad.org/shub/akhanf/vasst-dev/v0.0.4a/2018-01-30-3cb13998-f184e003/Singularity
collection: akhanf/vasst-dev
---

# akhanf/vasst-dev:v0.0.4a

```bash
$ singularity pull shub://akhanf/vasst-dev:v0.0.4a
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: khanlab/neuroglia-dwi:v1.0.0


%labels
Maintainer "Ali Khan"

#########
%setup
#########
mkdir -p $SINGULARITY_ROOTFS/opt/vasst-dev
cp -Rv . $SINGULARITY_ROOTFS/opt/vasst-dev

#########
%post
#########

echo addpath\(genpath\(\'/opt/vasst-dev/tools/matlab\'\)\)\; >> /etc/octave.conf 

cd /opt/vasst-dev/install_scripts
export DEBIAN_FRONTEND=noninteractive

bash 05.install_MCR.sh /opt v92 R2017a
bash 27.install_vasst_dev_atlases_by_source.sh /opt


#########
%environment



#vasst-dev
export VASST_DEV_HOME=/opt/vasst-dev
export PIPELINE_ATLAS_DIR=/opt/atlases
export PIPELINE_DIR=$VASST_DEV_HOME/pipeline
export PIPELINE_TOOL_DIR=$VASST_DEV_HOME/tools
MIAL_DEPENDS_DIR=$VASST_DEV_HOME/mial-depends
#MIAL_DEPENDS_LIBS=$VASST_DEV_HOME/mial-depends/lib
#export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$MIAL_DEPENDS_LIBS
export PIPELINE_CFG_DIR=$PIPELINE_DIR/cfg
export PATH=$PIPELINE_TOOL_DIR:$MIAL_DEPENDS_DIR:$PATH
export MCRBINS=$VASST_DEV_HOME/mcr/v92
for name in `ls -d $PIPELINE_DIR/*`; do  export PATH=$name:$PATH; done
#mcr - vasst-dev dependency
export MCRROOT=/opt/mcr/v92
```

## Collection

 - Name: [akhanf/vasst-dev](https://github.com/akhanf/vasst-dev)
 - License: [GNU General Public License v2.0](https://api.github.com/licenses/gpl-2.0)

