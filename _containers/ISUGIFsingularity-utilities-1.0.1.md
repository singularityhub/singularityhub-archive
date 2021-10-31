---
id: 2412
name: "ISUGIFsingularity/utilities"
branch: "master"
tag: "1.0.1"
commit: "734bcab9b17e9d070a8ad0b20c3da2cd85fa6455"
version: "cc2f35a81cda344f76c8c9e1998fe440"
build_date: "2021-04-05T08:56:48.625Z"
size_mb: 1032
size: 411217951
sif: "https://datasets.datalad.org/shub/ISUGIFsingularity/utilities/1.0.1/2021-04-05-734bcab9-cc2f35a8/cc2f35a81cda344f76c8c9e1998fe440.simg"
url: https://datasets.datalad.org/shub/ISUGIFsingularity/utilities/1.0.1/2021-04-05-734bcab9-cc2f35a8/
recipe: https://datasets.datalad.org/shub/ISUGIFsingularity/utilities/1.0.1/2021-04-05-734bcab9-cc2f35a8/Singularity
collection: ISUGIFsingularity/utilities
---

# ISUGIFsingularity/utilities:1.0.1

```bash
$ singularity pull shub://ISUGIFsingularity/utilities:1.0.1
```

## Singularity Recipe

```singularity
Bootstrap:shub
From:ResearchIT/spack-singularity:openmpi

%labels
MAINTAINER severin@iastate.edu
APPLICATION utililities

%help
This container contains all the necessary programs to create genome modules.
See https://github.com/ISUGIFsingularity/genomeModules.git for more inforation 

%environment
source /etc/profile.d/modules.sh
SPACK_ROOT=/opt/spack
export SPACK_ROOT
export PATH=$SPACK_ROOT/bin:$PATH
source /etc/profile.d/modules.sh
source $SPACK_ROOT/share/spack/setup-env.sh
export PATH=$SPACK_ROOT/isugif/utilities/utilities/:$PATH
module load python
module load perl
module load perl-bio-perl
module load py-biopython

%post
export SPACK_ROOT=/opt/spack
export SPACK_ROOT
export PATH=$SPACK_ROOT/bin:$PATH

yum -y install bc paste
yum clean all

export FORCE_UNSAFE_CONFIGURE=1 

source $SPACK_ROOT/share/spack/setup-env.sh
spack install python
spack install perl
spack install perl-bio-perl
spack install py-biopython

export PATH=$SPACK_ROOT/isugif/utilities/utilities:$SPACK_ROOT/isugif/utilities/wrappers:$PATH
#for d in /opt/spack/opt/spack/linux-centos7-x86_64/gcc-4.8.5/*/bin; do export PATH="$PATH:$d"; done

cd $SPACK_ROOT
rm -rf isugif
mkdir isugif
cd isugif
git clone https://github.com/ISUGIFsingularity/utilities.git
ls utilities/utilities/

%runscript
ls $SPACK_ROOT/isugif/utilities/utilities/
```

## Collection

 - Name: [ISUGIFsingularity/utilities](https://github.com/ISUGIFsingularity/utilities)
 - License: None

