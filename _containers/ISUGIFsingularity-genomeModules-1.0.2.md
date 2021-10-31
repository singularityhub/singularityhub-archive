---
id: 2404
name: "ISUGIFsingularity/genomeModules"
branch: "master"
tag: "1.0.2"
commit: "07c90f44c5865262ee63d679c91ab194f95b08c6"
version: "b2889c4e80c28812d0778005ec54d9ba"
build_date: "2020-07-15T16:44:45.941Z"
size_mb: 1624
size: 835846175
sif: "https://datasets.datalad.org/shub/ISUGIFsingularity/genomeModules/1.0.2/2020-07-15-07c90f44-b2889c4e/b2889c4e80c28812d0778005ec54d9ba.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ISUGIFsingularity/genomeModules/1.0.2/2020-07-15-07c90f44-b2889c4e/
recipe: https://datasets.datalad.org/shub/ISUGIFsingularity/genomeModules/1.0.2/2020-07-15-07c90f44-b2889c4e/Singularity
collection: ISUGIFsingularity/genomeModules
---

# ISUGIFsingularity/genomeModules:1.0.2

```bash
$ singularity pull shub://ISUGIFsingularity/genomeModules:1.0.2
```

## Singularity Recipe

```singularity
Bootstrap:shub
From:ResearchIT/spack-singularity:openmpi

%labels
MAINTAINER severin@iastate.edu
APPLICATION genomeModules 

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
export PATH=$SPACK_ROOT/isugif/utilities/bin:$SPACK_ROOT/utilities/wrappers:$PATH
#for d in /opt/spack/opt/spack/linux-centos7-x86_64/gcc-4.8.5/*/bin; do export PATH="$PATH:$d"; done

module load gmap-gsnap
module load bowtie2
module load bwa
module load gatk
module load bedtools2
module load samtools
module load picard
module load jdk
export _JAVA_OPTIONS="-Xmx100G"
module load parallel

%post
export SPACK_ROOT=/opt/spack
export SPACK_ROOT
export PATH=$SPACK_ROOT/bin:$PATH

yum -y install bc paste
yum clean all

export FORCE_UNSAFE_CONFIGURE=1 

source $SPACK_ROOT/share/spack/setup-env.sh
spack install picard
spack install gmap-gsnap
spack install bowtie2
spack install bwa
spack install gatk
spack install bedtools2
spack install samtools
spack install parallel

#for d in /opt/spack/opt/spack/linux-centos7-x86_64/gcc-4.8.5/*/bin; do export PATH="$PATH:$d"; done


cd $SPACK_ROOT

%runscript
```

## Collection

 - Name: [ISUGIFsingularity/genomeModules](https://github.com/ISUGIFsingularity/genomeModules)
 - License: None

