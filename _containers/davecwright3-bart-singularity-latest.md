---
id: 14860
name: "davecwright3/bart-singularity"
branch: "master"
tag: "latest"
commit: "0f7595c6f664cf94abd8a65afd827e230d41771b"
version: "26d7531d71e9fcdcbc10367aaffc8271"
build_date: "2020-11-13T16:00:28.462Z"
size_mb: 3068.0
size: 1350062111
sif: "https://datasets.datalad.org/shub/davecwright3/bart-singularity/latest/2020-11-13-0f7595c6-26d7531d/26d7531d71e9fcdcbc10367aaffc8271.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/davecwright3/bart-singularity/latest/2020-11-13-0f7595c6-26d7531d/
recipe: https://datasets.datalad.org/shub/davecwright3/bart-singularity/latest/2020-11-13-0f7595c6-26d7531d/Singularity
collection: davecwright3/bart-singularity
---

# davecwright3/bart-singularity:latest

```bash
$ singularity pull shub://davecwright3/bart-singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:20.04

%post
    apt-get update -y && apt-get install -y build-essential bc wget git unzip

    rm -rf /var/lib/apt/lists/*


    CONDA_INSTALL_PATH="/opt/miniconda"
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
    bash miniconda.sh -b -p $CONDA_INSTALL_PATH

    rm -r miniconda.sh

    . $CONDA_INSTALL_PATH/etc/profile.d/conda.sh

    mkdir /bart_dir
    cd /bart_dir
    mkdir run
    git clone --recursive https://github.com/exosports/BART BART/
    conda env create -f /bart_dir/BART/environment.yml
    conda activate bart
    echo ". $CONDA_INSTALL_PATH/etc/profile.d/conda.sh" >> /.singularity_bashrc
    echo "conda activate bart" >> /.singularity_bashrc



    cd /bart_dir/BART/modules/transit/
    make

    cd /bart_dir/BART/modules/MCcubed/
    make


%environment
    CONDA_INSTALL_PATH="/opt/miniconda"
    CONDA_BIN_PATH="/opt/minconda/bin"
    SINGULARITY_SHELL=/bin/bash
    topdir="/bart_dir"
    action="${0##*/}"
    if [ "$action" == "shell" ]; then
        if [ "${SINGULARITY_SHELL:-}" == "/bin/bash" ]; then
            set -- --noprofile --init-file /.singularity_bashrc
        elif test -z "${SINGULARITY_SHELL:-}"; then
            export SINGULARITY_SHELL=/bin/bash
            set -- --noprofile --init-file /.singularity_bashrc
        fi
    fi
    export PATH="$CONDA_BIN_PATH:$PATH"
    export topdir

%runscript
    exec /bin/bash --noprofile --init-file /.singularity_bashrc "$@"
%labels
    Maintainer David Wright <davecwright@knights.ucf.edu>
    License See README or /bart_dir/BART/license in container
    Version v1.0
```

## Collection

 - Name: [davecwright3/bart-singularity](https://github.com/davecwright3/bart-singularity)
 - License: [Other](None)

