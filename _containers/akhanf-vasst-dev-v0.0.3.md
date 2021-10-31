---
id: 1483
name: "akhanf/vasst-dev"
branch: "master"
tag: "v0.0.3"
commit: "ad1a6144728f42d7a520e89a6688164bdc849dc3"
version: "337c8e23e03e9dbbd6bb5d6298accec9"
build_date: "2018-01-28T20:20:09.452Z"
size_mb: 10985
size: 4666585119
sif: "https://datasets.datalad.org/shub/akhanf/vasst-dev/v0.0.3/2018-01-28-ad1a6144-337c8e23/337c8e23e03e9dbbd6bb5d6298accec9.simg"
url: https://datasets.datalad.org/shub/akhanf/vasst-dev/v0.0.3/2018-01-28-ad1a6144-337c8e23/
recipe: https://datasets.datalad.org/shub/akhanf/vasst-dev/v0.0.3/2018-01-28-ad1a6144-337c8e23/Singularity
collection: akhanf/vasst-dev
---

# akhanf/vasst-dev:v0.0.3

```bash
$ singularity pull shub://akhanf/vasst-dev:v0.0.3
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

SINGULARITY_TAG=${SINGULARITY_BUILDDEF#Singularity.}

cd /opt/vasst-dev
if [ ! "$SINGULARITY_TAG" = "Singularity" ]
then
  git checkout $SINGULARITY_TAG
fi

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

