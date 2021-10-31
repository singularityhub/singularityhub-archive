---
id: 3630
name: "akhanf/vasst-dev"
branch: "master"
tag: "v0.0.4g"
commit: "0f44eaba003b62b739be37f07acc27f62185d8df"
version: "ffac13f5a6b23519b1d641af46cc3750"
build_date: "2019-11-05T22:36:15.531Z"
size_mb: 10985
size: 4666765343
sif: "https://datasets.datalad.org/shub/akhanf/vasst-dev/v0.0.4g/2019-11-05-0f44eaba-ffac13f5/ffac13f5a6b23519b1d641af46cc3750.simg"
url: https://datasets.datalad.org/shub/akhanf/vasst-dev/v0.0.4g/2019-11-05-0f44eaba-ffac13f5/
recipe: https://datasets.datalad.org/shub/akhanf/vasst-dev/v0.0.4g/2019-11-05-0f44eaba-ffac13f5/Singularity
collection: akhanf/vasst-dev
---

# akhanf/vasst-dev:v0.0.4g

```bash
$ singularity pull shub://akhanf/vasst-dev:v0.0.4g
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

