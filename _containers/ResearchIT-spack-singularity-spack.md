---
id: 2222
name: "ResearchIT/spack-singularity"
branch: "master"
tag: "spack"
commit: "1ec19eecb63e90753778fbeaf9f850d1d827d420"
version: "0a6cb0d7ff00f05dc956f6e289a3c7d8"
build_date: "2021-03-03T11:41:10.994Z"
size_mb: 489
size: 201273375
sif: "https://datasets.datalad.org/shub/ResearchIT/spack-singularity/spack/2021-03-03-1ec19eec-0a6cb0d7/0a6cb0d7ff00f05dc956f6e289a3c7d8.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ResearchIT/spack-singularity/spack/2021-03-03-1ec19eec-0a6cb0d7/
recipe: https://datasets.datalad.org/shub/ResearchIT/spack-singularity/spack/2021-03-03-1ec19eec-0a6cb0d7/Singularity
collection: ResearchIT/spack-singularity
---

# ResearchIT/spack-singularity:spack

```bash
$ singularity pull shub://ResearchIT/spack-singularity:spack
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:centos:7

%labels
MAINTAINER baber@iastate.edu
spack

%environment
SPACK_ROOT=/opt/spack
export SPACK_ROOT
export PATH=$SPACK_ROOT/bin:$PATH
source /etc/profile.d/modules.sh
source $SPACK_ROOT/share/spack/setup-env.sh

%post
export SPACK_ROOT=/opt/spack
export SPACK_ROOT
export PATH=$SPACK_ROOT/bin:$PATH

#spack dependencies
yum -y install git python \
gcc gcc-c++ gcc-gfortran curl \
gnupg2 sed patch \
unzip gzip bzip2 \
findutils make vim \
environment-modules

yum clean all

#get spack
git clone https://github.com/spack/spack.git $SPACK_ROOT

#setup compilers.yaml
spack compiler find --scope system $(which gcc)
spack compiler find --scope system $(which g++)
spack compiler find --scope system $(which gfortran)

#setup modules config file
echo "modules:" >> /opt/spack/etc/spack/modules.yaml
echo "  tcl:" >> /opt/spack/etc/spack/modules.yaml
echo "    naming_scheme: '\${PACKAGE}/\${VERSION}'" >> /opt/spack/etc/spack/modules.yaml

source $SPACK_ROOT/share/spack/setup-env.sh

%runscript
spack help
```

## Collection

 - Name: [ResearchIT/spack-singularity](https://github.com/ResearchIT/spack-singularity)
 - License: None

