---
id: 5356
name: "ISUGIFsingularity/masurca"
branch: "master"
tag: "1.0.0"
commit: "05c0966a276ef62037665d3cfbac05ff3d55a9cf"
version: "c4056ad7d372885d3f9f62c71adeeae1"
build_date: "2021-04-16T05:49:03.477Z"
size_mb: 2110
size: 673984543
sif: "https://datasets.datalad.org/shub/ISUGIFsingularity/masurca/1.0.0/2021-04-16-05c0966a-c4056ad7/c4056ad7d372885d3f9f62c71adeeae1.simg"
url: https://datasets.datalad.org/shub/ISUGIFsingularity/masurca/1.0.0/2021-04-16-05c0966a-c4056ad7/
recipe: https://datasets.datalad.org/shub/ISUGIFsingularity/masurca/1.0.0/2021-04-16-05c0966a-c4056ad7/Singularity
collection: ISUGIFsingularity/masurca
---

# ISUGIFsingularity/masurca:1.0.0

```bash
$ singularity pull shub://ISUGIFsingularity/masurca:1.0.0
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
awk '/ftp.genome.umd.edu/ { print; print "\n";printf "    version('\''3.2.8'\'', '\''7e01fd95f7aefa270b67373ef8f1f8ce'\'', url='\''https://github.com/alekseyzimin/masurca/releases/download/3.2.8/MaSuRCA-3.2.8.tar.gz'\'')"; next }1' $SPACK_ROOT/var/spack/repos/builtin/packages/masurca/package.py  > package.py

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





spack install masurca@3.2.8



#for d in /opt/spack/opt/spack/linux-centos7-x86_64/gcc-4.8.5/*/bin; do export PATH="$PATH:$d"; done


cd $SPACK_ROOT

%runscript
```

## Collection

 - Name: [ISUGIFsingularity/masurca](https://github.com/ISUGIFsingularity/masurca)
 - License: None

