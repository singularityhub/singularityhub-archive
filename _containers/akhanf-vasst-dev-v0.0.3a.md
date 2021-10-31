---
id: 1487
name: "akhanf/vasst-dev"
branch: "master"
tag: "v0.0.3a"
commit: "102659670395b442a59545aeee7f3fde5e052d42"
version: "aa6c965c43ffd3c3e3996327a6468330"
build_date: "2018-01-29T09:31:50.973Z"
size_mb: 10985
size: 4666589215
sif: "https://datasets.datalad.org/shub/akhanf/vasst-dev/v0.0.3a/2018-01-29-10265967-aa6c965c/aa6c965c43ffd3c3e3996327a6468330.simg"
url: https://datasets.datalad.org/shub/akhanf/vasst-dev/v0.0.3a/2018-01-29-10265967-aa6c965c/
recipe: https://datasets.datalad.org/shub/akhanf/vasst-dev/v0.0.3a/2018-01-29-10265967-aa6c965c/Singularity
collection: akhanf/vasst-dev
---

# akhanf/vasst-dev:v0.0.3a

```bash
$ singularity pull shub://akhanf/vasst-dev:v0.0.3a
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

