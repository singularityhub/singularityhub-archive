---
id: 12384
name: "TomHarrop/funannotate-singularity"
branch: "master"
tag: "funannotate_8e2e0a1"
commit: "38358c6cb6bc998dc4c4c43f548c79d227db0d49"
version: "980fddd07ddecfb9d453c39c4cb3b91c6ed8fc815f471645802f99a1f514f96c"
build_date: "2020-02-26T23:35:31.249Z"
size_mb: 2654.0078125
size: 2782928896
sif: "https://datasets.datalad.org/shub/TomHarrop/funannotate-singularity/funannotate_8e2e0a1/2020-02-26-38358c6c-980fddd0/980fddd07ddecfb9d453c39c4cb3b91c6ed8fc815f471645802f99a1f514f96c.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/funannotate-singularity/funannotate_8e2e0a1/2020-02-26-38358c6c-980fddd0/
recipe: https://datasets.datalad.org/shub/TomHarrop/funannotate-singularity/funannotate_8e2e0a1/2020-02-26-38358c6c-980fddd0/Singularity
collection: TomHarrop/funannotate-singularity
---

# TomHarrop/funannotate-singularity:funannotate_8e2e0a1

```bash
$ singularity pull shub://TomHarrop/funannotate-singularity:funannotate_8e2e0a1
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: TomHarrop/funannotate-singularity:funannotate-deps_8e2e0a1

# Bootstrap: localimage
# From: funannotate-deps_8e2e0a1.sif

%help
    '
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

    cp the Genemake license to ${HOME}/.gm_key at runtime

    The following dependencies have issues in 8e2e0a1
    - augustus (installed, not sure what the error is)
    - proteinortho not installed, dont know what it is
    - salmon (installed at /usr/bin/salmon)
    - signalp (not installed, license)
    - trimmomatic (installed, java -jar /usr/share/java/trimmomatic.jar,
                   /usr/bin/TrimmomaticPE, /usr/bin/TrimmomaticSE)
    '

%labels
    MAINTAINER "Tom Harrop (twharrop@gmail.com)"
    VERSION "funannotate 8e2e0a1 for python3"

%post
    export DEBIAN_FRONTEND=noninteractive

    # Genemark license? cp to ${HOME}/.gm_key at runtime

    # funannotate 
    /usr/local/bin/pip3 \
        install \
        git+git://github.com/nextgenusfs/funannotate.git@8e2e0a1
    
    export PATH="/blast/bin:${PATH}:/usr/lib/debian-med/bin:/fasta/bin:/pasa/bin:/genemark:/evm:/snap"
    export FUNANNOTATE_DB=/funannotate_db
    export PASAHOME=/pasa
    export TRINITYHOME=/usr/bin
    export EVM_HOME=/evm
    export AUGUSTUS_CONFIG_PATH="/opt/augustus-3.3.3/config"
    export GENEMARK_PATH=/genemark
    export BAMTOOLS_PATH=/usr/bin
    funannotate check --show-versions

%environment
    export PATH="/blast/bin:${PATH}:/usr/lib/debian-med/bin:/fasta/bin:/pasa/bin:/genemark:/evm:/snap"
    export FUNANNOTATE_DB=/funannotate_db
    export PASAHOME=/pasa
    export TRINITYHOME=/usr/bin
    export EVM_HOME=/evm
    export AUGUSTUS_CONFIG_PATH="/opt/augustus-3.3.3/config"
    export GENEMARK_PATH=/genemark
    export BAMTOOLS_PATH=/usr/bin

%runscript
    exec /usr/local/bin/funannotate "$@"
```

## Collection

 - Name: [TomHarrop/funannotate-singularity](https://github.com/TomHarrop/funannotate-singularity)
 - License: [MIT License](https://api.github.com/licenses/mit)

