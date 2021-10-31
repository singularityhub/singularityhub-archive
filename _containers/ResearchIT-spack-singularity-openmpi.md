---
id: 2225
name: "ResearchIT/spack-singularity"
branch: "master"
tag: "openmpi"
commit: "4b571c312165397eb3c6fe2896f4538aef99852c"
version: "12938774d3e1c6f7dec7a10f451edc80"
build_date: "2021-04-19T20:49:05.714Z"
size_mb: 694
size: 277757983
sif: "https://datasets.datalad.org/shub/ResearchIT/spack-singularity/openmpi/2021-04-19-4b571c31-12938774/12938774d3e1c6f7dec7a10f451edc80.simg"
url: https://datasets.datalad.org/shub/ResearchIT/spack-singularity/openmpi/2021-04-19-4b571c31-12938774/
recipe: https://datasets.datalad.org/shub/ResearchIT/spack-singularity/openmpi/2021-04-19-4b571c31-12938774/Singularity
collection: ResearchIT/spack-singularity
---

# ResearchIT/spack-singularity:openmpi

```bash
$ singularity pull shub://ResearchIT/spack-singularity:openmpi
```

## Singularity Recipe

```singularity
Bootstrap:shub
From:ResearchIT/spack-singularity:spack

%labels
MAINTAINER baber@iastate.edu

%environment
source /etc/profile.d/modules.sh
module load openmpi

%post
export SPACK_ROOT=/opt/spack
export SPACK_ROOT
export PATH=$SPACK_ROOT/bin:$PATH

source $SPACK_ROOT/share/spack/setup-env.sh

spack install openmpi schedulers=slurm

%runscript
exec mpirun "$@"
```

## Collection

 - Name: [ResearchIT/spack-singularity](https://github.com/ResearchIT/spack-singularity)
 - License: None

