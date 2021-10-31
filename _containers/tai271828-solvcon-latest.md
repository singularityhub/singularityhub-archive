---
id: 5363
name: "tai271828/solvcon"
branch: "master"
tag: "latest"
commit: "ef3f7d151201aa24dbe70d1649ea43752aa49877"
version: "978bcf4eb604adc6862a199af665e930"
build_date: "2018-10-28T13:17:12.816Z"
size_mb: 2754
size: 916733983
sif: "https://datasets.datalad.org/shub/tai271828/solvcon/latest/2018-10-28-ef3f7d15-978bcf4e/978bcf4eb604adc6862a199af665e930.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/tai271828/solvcon/latest/2018-10-28-ef3f7d15-978bcf4e/
recipe: https://datasets.datalad.org/shub/tai271828/solvcon/latest/2018-10-28-ef3f7d15-978bcf4e/Singularity
collection: tai271828/solvcon
---

# tai271828/solvcon:latest

```bash
$ singularity pull shub://tai271828/solvcon:latest
```

## Singularity Recipe

```singularity
BootStrap: debootstrap
OSVersion: xenial
MirrorURL: http://us.archive.ubuntu.com/ubuntu/


%environment
    export SOLVCON_WORKING_DIR=/opt/solvcon-working
    export PATH="$SOLVCON_WORKING_DIR/venv-conda/bin:$SOLVCON_WORKING_DIR/miniconda/bin:$PATH"

%runscript
    echo "Welcome to SOLVCON singularity instance."

%files
    prepare-solvcon-dev.sh /prepare-solvcon-dev.sh

%post
    echo "Prepare to build SOLVCON in singularity instance..."
    sed -i 's/$/ universe/' /etc/apt/sources.list
    apt-get update
    # general tools
    apt-get install vim git -y
    # used for miniconda extraction
    apt-get install bzip2
    # SOLVCON build tools
    apt-get install openssh-client openssh-server liblapack-pic liblapack-dev -y
    apt-get install build-essential unzip -y
    # it currently works in the root path
    echo "Working location: " `pwd`
    # it is /root
    echo $HOME
    apt-get clean

    # start to build
    export SOLVCON_BUILD_DIR=/opt
    /bin/bash -c "source /prepare-solvcon-dev.sh $SOLVCON_BUILD_DIR"
```

## Collection

 - Name: [tai271828/solvcon](https://github.com/tai271828/solvcon)
 - License: [BSD 3-Clause "New" or "Revised" License](https://api.github.com/licenses/bsd-3-clause)

