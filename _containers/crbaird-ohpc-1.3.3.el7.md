---
id: 803
name: "crbaird/ohpc"
branch: "obs/OpenHPC_1.3.3_Factory"
tag: "1.3.3.el7"
commit: "c6f5ab92c120cefaaf6f8e0f6bc3776458dafe9b"
version: "730c5d18dfeaed2046d5a3f616519df4"
build_date: "2017-11-16T10:30:37.232Z"
size_mb: 3682
size: 959365151
sif: "https://datasets.datalad.org/shub/crbaird/ohpc/1.3.3.el7/2017-11-16-c6f5ab92-730c5d18/730c5d18dfeaed2046d5a3f616519df4.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/crbaird/ohpc/1.3.3.el7/2017-11-16-c6f5ab92-730c5d18/
recipe: https://datasets.datalad.org/shub/crbaird/ohpc/1.3.3.el7/2017-11-16-c6f5ab92-730c5d18/Singularity
collection: crbaird/ohpc
---

# crbaird/ohpc:1.3.3.el7

```bash
$ singularity pull shub://crbaird/ohpc:1.3.3.el7
```

## Singularity Recipe

```singularity
bootstrap:docker
From:centos:7

%post

yum -y upgrade

# OpenHPC repo
yum -y install https://github.com/openhpc/ohpc/releases/download/v1.3.GA/ohpc-release-1.3-1.el7.x86_64.rpm

yum -y install perl

yum -y install \
    ohpc-base \
    ohpc-base-compute \
    ohpc-autotools \
    ohpc-gnu7-io-libs \
    ohpc-gnu7-mpich-parallel-libs \
    ohpc-gnu7-mvapich2-parallel-libs \
    ohpc-gnu7-openmpi3-parallel-libs \
    ohpc-gnu7-perf-tools \
    ohpc-gnu7-python-libs \
    ohpc-gnu7-serial-libs \
    openssh-clients

yum -y install lmod-defaults-gnu7-openmpi3-ohpc

cat << EOF > /etc/profile.d/lmod.sh
#!/bin/sh
# -*- shell-script -*-
########################################################################
#  This is the system wide source file for setting up
#  modules:
#
########################################################################

# NOOP if running under known resource manager
if [[ ! -z "$SLURM_NODELIST" && -z "$SINGULARITY_CONTAINER" ]];then
     return
fi

if [[ ! -z "$PBS_NODEFILE" && -z "$SINGULARITY_CONTAINER" ]];then
    return
fi

export LMOD_SETTARG_CMD=":"
export LMOD_FULL_SETTARG_SUPPORT=no
export LMOD_COLORIZE=no
export LMOD_PREPEND_BLOCK=normal

if [ $EUID -eq 0 ]; then
    export MODULEPATH=/opt/ohpc/admin/modulefiles:/opt/ohpc/pub/modulefiles
else
    export MODULEPATH=/opt/ohpc/pub/modulefiles
fi

export BASH_ENV=/opt/ohpc/admin/lmod/lmod/init/bash

# Initialize modules system
. /opt/ohpc/admin/lmod/lmod/init/bash >/dev/null

if [[ -n "$SINGULARITY_CONTAINER" ]];then
    module purge
    clearMT
fi

# Load baseline OpenHPC environment
module try-add ohpc

EOF

cat << EOF > /etc/profile.d/lmod.csh
#!/bin/csh
# -*- shell-script -*-
########################################################################
#  This is the system wide source file for setting up
#  modules:
#
########################################################################

if ( $?SLURM_NODELIST && ! $?SINGULARITY_CONTAINER ) then
    exit 0
endif

if ( $?PBS_NODEFILE && ! $?SINGULARITY_CONTAINER ) then
    exit 0
endif

setenv LMOD_SETTARG_CMD ":"
setenv LMOD_FULL_SETTARG_SUPPORT "no"
setenv LMOD_COLORIZE "no"
setenv LMOD_PREPEND_BLOCK "normal"


if ( `id -u` == "0" ) then
   setenv MODULEPATH  "/opt/ohpc/admin/modulefiles:/opt/ohpc/pub/modulefiles"
else   
   setenv MODULEPATH "/opt/ohpc/pub/modulefiles"
endif

# Initialize modules system
source /opt/ohpc/admin/lmod/lmod/init/csh >/dev/null

if ( $?SINGULARITY_CONTAINER ) then
    module purge
    clearMT
endif

# Load baseline OpenHPC environment
module try-add ohpc 

EOF

# verification
ls -l /opt/ohpc/pub

# build info
echo "Timestamp:" `date --utc` | tee /image-build-info.txt
```

## Collection

 - Name: [crbaird/ohpc](https://github.com/crbaird/ohpc)
 - License: None

