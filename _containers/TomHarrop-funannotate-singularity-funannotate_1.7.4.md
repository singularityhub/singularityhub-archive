---
id: 12925
name: "TomHarrop/funannotate-singularity"
branch: "master"
tag: "funannotate_1.7.4"
commit: "c5e7e94e1830f825ad4dabc1af29413c65c3fd13"
version: "16bb903a258de24e0a36cb2872cc700a69b488f985dabdd55bba30c2cf55a695"
build_date: "2020-05-07T05:31:26.546Z"
size_mb: 2892.09765625
size: 3032584192
sif: "https://datasets.datalad.org/shub/TomHarrop/funannotate-singularity/funannotate_1.7.4/2020-05-07-c5e7e94e-16bb903a/16bb903a258de24e0a36cb2872cc700a69b488f985dabdd55bba30c2cf55a695.sif"
url: https://datasets.datalad.org/shub/TomHarrop/funannotate-singularity/funannotate_1.7.4/2020-05-07-c5e7e94e-16bb903a/
recipe: https://datasets.datalad.org/shub/TomHarrop/funannotate-singularity/funannotate_1.7.4/2020-05-07-c5e7e94e-16bb903a/Singularity
collection: TomHarrop/funannotate-singularity
---

# TomHarrop/funannotate-singularity:funannotate_1.7.4

```bash
$ singularity pull shub://TomHarrop/funannotate-singularity:funannotate_1.7.4
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: TomHarrop/funannotate-singularity:funannotate-deps_1.7.4

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

    The following dependencies have issues in 1.7.4
    - proteinortho not installed, dont know what it is
    - salmon (installed at /usr/bin/salmon)
    - signalp (not installed, license)
    '

%labels
    MAINTAINER "Tom Harrop (twharrop@gmail.com)"
    VERSION "funannotate v1.7.4 for python2"

%post
    export DEBIAN_FRONTEND=noninteractive

    # provide wrapper for trimmomatic (move to deps)
    wget \
        -O trimmomatic.py \
        https://raw.githubusercontent.com/bioconda/bioconda-recipes/master/recipes/trimmomatic/trimmomatic.py
    sed -e \
        's/trimmomatic.jar/\/usr\/share\/java\/trimmomatic.jar/g' \
        trimmomatic.py \
        > /usr/local/bin/trimmomatic
    rm trimmomatic.py
    chmod 755 /usr/local/bin/trimmomatic

    # funannotate 
    /usr/local/bin/pip2 \
        install \
        git+git://github.com/nextgenusfs/funannotate.git@v1.7.4

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

