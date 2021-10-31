---
id: 1609
name: "akhanf/vasst-dev"
branch: "master"
tag: "v0.0.4c"
commit: "aaf5c710f7e5b40134156d0abf06117e6dd20b07"
version: "55a2e43b6046c710aafb195ba9d3d15e"
build_date: "2018-02-05T10:17:17.255Z"
size_mb: 10985
size: 4666687519
sif: "https://datasets.datalad.org/shub/akhanf/vasst-dev/v0.0.4c/2018-02-05-aaf5c710-55a2e43b/55a2e43b6046c710aafb195ba9d3d15e.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/akhanf/vasst-dev/v0.0.4c/2018-02-05-aaf5c710-55a2e43b/
recipe: https://datasets.datalad.org/shub/akhanf/vasst-dev/v0.0.4c/2018-02-05-aaf5c710-55a2e43b/Singularity
collection: akhanf/vasst-dev
---

# akhanf/vasst-dev:v0.0.4c

```bash
$ singularity pull shub://akhanf/vasst-dev:v0.0.4c
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

