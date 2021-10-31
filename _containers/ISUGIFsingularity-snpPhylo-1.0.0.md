---
id: 3221
name: "ISUGIFsingularity/snpPhylo"
branch: "master"
tag: "1.0.0"
commit: "f8c6e508bae07e46977f17a9c3c323f2d0f5460b"
version: "bce964b26feea689a38a65a08550936b"
build_date: "2018-06-20T16:42:28.197Z"
size_mb: 696
size: 278237215
sif: "https://datasets.datalad.org/shub/ISUGIFsingularity/snpPhylo/1.0.0/2018-06-20-f8c6e508-bce964b2/bce964b26feea689a38a65a08550936b.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ISUGIFsingularity/snpPhylo/1.0.0/2018-06-20-f8c6e508-bce964b2/
recipe: https://datasets.datalad.org/shub/ISUGIFsingularity/snpPhylo/1.0.0/2018-06-20-f8c6e508-bce964b2/Singularity
collection: ISUGIFsingularity/snpPhylo
---

# ISUGIFsingularity/snpPhylo:1.0.0

```bash
$ singularity pull shub://ISUGIFsingularity/snpPhylo:1.0.0
```

## Singularity Recipe

```singularity
Bootstrap:shub
From:ResearchIT/spack-singularity:openmpi

%labels
MAINTAINER severin@iastate.edu

$help
echo "This container contains a runscript for snpPhylo"

%environment
SPACK_ROOT=/opt/spack
export SPACK_ROOT
export PATH=$SPACK_ROOT/bin:$PATH
source /etc/profile.d/modules.sh
source $SPACK_ROOT/share/spack/setup-env.sh
export PATH=$SPACK_ROOT/isugif/snpPhylo/bin:$SPACK_ROOT/isugif/snpPhylo/wrappers:$PATH
for d in /opt/spack/opt/spack/linux-centos7-x86_64/gcc-4.8.5/*/bin; do export PATH="$PATH:$d"; done

%post
export SPACK_ROOT=/opt/spack
export SPACK_ROOT
export PATH=$SPACK_ROOT/bin:$PATH

yum -y install git python \
gcc gcc-c++ gcc-gfortran curl \
gnupg2 sed patch \
unzip gzip bzip2 \
findutils make vim \
environment-modules

yum clean all


if [ ! -d "$SPACK_ROOT" ]; then
  git clone https://github.com/spack/spack.git $SPACK_ROOT
  spack compiler find $(which gcc)
  spack compiler find $(which g++)
  spack compiler find $(which gfortran)

  #because i'm buildiing as root
  export FORCE_UNSAFE_CONFIGURE=1

  source $SPACK_ROOT/share/spack/setup-env.sh
  spack install vcftools
  spack install snphylo
fi


# export BUSCODIR=$SPACK_ROOT/opt/spack/linux-centos7-x86_64/gcc-4.8.5/busco-3.0.1-cafwtkz5ryvlwnup3xzntotjwlrqsiui
# cp $BUSCODIR/config/config.ini.default $BUSCODIR/config/config.ini

cd $SPACK_ROOT
mkdir isugif
cd isugif
git clone https://github.com/ISUGIFsingularity/snpPhylo.git
cd snpPhylo
chmod 755 bin/*

%runscript
echo "This container contains a runscript for snpPhylo"
exec runSNPphylo.sh "$@"
```

## Collection

 - Name: [ISUGIFsingularity/snpPhylo](https://github.com/ISUGIFsingularity/snpPhylo)
 - License: None

