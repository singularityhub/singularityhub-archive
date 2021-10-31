---
id: 7377
name: "ISUGIFsingularity/masurca"
branch: "master"
tag: "3.2.9"
commit: "e6f1edd708f2a97616b5d42117db50527701f90a"
version: "9b14bbfafc78c1203a709a5e1faaee71"
build_date: "2021-03-05T14:10:09.446Z"
size_mb: 2128
size: 684232735
sif: "https://datasets.datalad.org/shub/ISUGIFsingularity/masurca/3.2.9/2021-03-05-e6f1edd7-9b14bbfa/9b14bbfafc78c1203a709a5e1faaee71.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ISUGIFsingularity/masurca/3.2.9/2021-03-05-e6f1edd7-9b14bbfa/
recipe: https://datasets.datalad.org/shub/ISUGIFsingularity/masurca/3.2.9/2021-03-05-e6f1edd7-9b14bbfa/Singularity
collection: ISUGIFsingularity/masurca
---

# ISUGIFsingularity/masurca:3.2.9

```bash
$ singularity pull shub://ISUGIFsingularity/masurca:3.2.9
```

## Singularity Recipe

```singularity
Bootstrap:shub
From:ResearchIT/spack-singularity:openmpi

%labels
MAINTAINER severin@iastate.edu
APPLICATION MaSurCArunScripts

%help
This container contains all the necessary programs to run MaSuRCA
See https://github.com/ISUGIFsingularity/masurca.git for more inforation

%environment
source /etc/profile.d/modules.sh
SPACK_ROOT=/opt/spack
export SPACK_ROOT
export PATH=$SPACK_ROOT/bin:$PATH
source /etc/profile.d/modules.sh
source $SPACK_ROOT/share/spack/setup-env.sh
#for d in /opt/spack/opt/spack/linux-centos7-x86_64/gcc-4.8.5/*/bin; do export PATH="$PATH:$d"; done

# make sure spack is up2date

module load perl
module load masurca




%post
export SPACK_ROOT=/opt/spack
export SPACK_ROOT
export PATH=$SPACK_ROOT/bin:$PATH

# make sure spack is up2date
cd $SPACK_ROOT
git pull

# modify package to include latest verson
awk '/ftp.genome.umd.edu/ { print; print "\n";printf "    version('\''3.2.9'\'', '\''f37e1a6f44a884b237b333c353161881'\'', url='\''https://github.com/alekseyzimin/masurca/raw/master/MaSuRCA-3.2.9.tar.gz'\'')"; next }1' $SPACK_ROOT/var/spack/repos/builtin/packages/masurca/package.py  > package.py

mv package.py $SPACK_ROOT/var/spack/repos/builtin/packages/masurca/
cd -


yum -y install bc paste wget
yum clean all

export FORCE_UNSAFE_CONFIGURE=1

source $SPACK_ROOT/share/spack/setup-env.sh


#bzip.org is down, dfetching repo from fossies.org into mirror
mkdir -p $SPACK_ROOT/mirror/bzip2
spack mirror add local $SPACK_ROOT/mirror
pushd $SPACK_ROOT/mirror/bzip2
wget https://fossies.org/linux/misc/bzip2-1.0.6.tar.gz
popd





spack install masurca@3.2.9



#for d in /opt/spack/opt/spack/linux-centos7-x86_64/gcc-4.8.5/*/bin; do export PATH="$PATH:$d"; done


cd $SPACK_ROOT

%runscript
```

## Collection

 - Name: [ISUGIFsingularity/masurca](https://github.com/ISUGIFsingularity/masurca)
 - License: None

