---
id: 11086
name: "TomHarrop/funannotate-singularity"
branch: "master"
tag: "funannotate_1.6.0"
commit: "5d0496b71cc229fc31cf06953737f9c4038ee51a"
version: "99f8724bcc94f64280ac3e5f5ca54ddab65134a5b19cd4d6c4dde704b4f4f7d5"
build_date: "2020-02-25T04:05:44.930Z"
size_mb: 2626.8671875
size: 2754469888
sif: "https://datasets.datalad.org/shub/TomHarrop/funannotate-singularity/funannotate_1.6.0/2020-02-25-5d0496b7-99f8724b/99f8724bcc94f64280ac3e5f5ca54ddab65134a5b19cd4d6c4dde704b4f4f7d5.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/funannotate-singularity/funannotate_1.6.0/2020-02-25-5d0496b7-99f8724b/
recipe: https://datasets.datalad.org/shub/TomHarrop/funannotate-singularity/funannotate_1.6.0/2020-02-25-5d0496b7-99f8724b/Singularity
collection: TomHarrop/funannotate-singularity
---

# TomHarrop/funannotate-singularity:funannotate_1.6.0

```bash
$ singularity pull shub://TomHarrop/funannotate-singularity:funannotate_1.6.0
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: TomHarrop/funannotate-singularity:funannotate-deps_1.6.0

%help
    Funannotate
    https://funannotate.readthedocs.io

    Funannotate uses environment variables to define the path to the 
    funannotate database. Override with `-d`, or bind the FUNANNOTATE_DB
    directory into the container as follows:

    singularity exec \
        -B output/funannotate_db:/funannotate_db \
        funannotate.sif \
        funannotate

    The RepeatMasker installation does not include Repbase libraries.

%labels
    MAINTAINER "Tom Harrop (twharrop@gmail.com)"
    VERSION "funannotate 1.6.0"

%post
    export DEBIAN_FRONTEND=noninteractive

    # Genemark license? cp to ${HOME}/.gm_key at runtime

    # funannotate 
    wget -O funannotate.tar.gz \
        --no-check-certificate \
        https://github.com/nextgenusfs/funannotate/archive/1.6.0.tar.gz
    mkdir funannotate
    tar -zxf funannotate.tar.gz \
        -C funannotate \
        --strip-components 1
    # git clone https://github.com/nextgenusfs/funannotate.git
    # cd funannotate || exit 1
    # git checkout 16500bc
    # cd .. || exit 1

%environment
    export PATH="/blast/bin:${PATH}:/usr/lib/debian-med/bin:/fasta/bin:/pasa/bin:/genemark:/funannotate:/evm:/snap"
    export FUNANNOTATE_DB=/funannotate_db
    export PASAHOME=/pasa
    export TRINITYHOME=/usr/bin
    export EVM_HOME=/evm
    export AUGUSTUS_CONFIG_PATH="/usr/share/augustus/config"
    export GENEMARK_PATH=/genemark
    export BAMTOOLS_PATH=/usr/bin

%runscript
    exec /funannotate/funannotate "$@"
```

## Collection

 - Name: [TomHarrop/funannotate-singularity](https://github.com/TomHarrop/funannotate-singularity)
 - License: [MIT License](https://api.github.com/licenses/mit)

