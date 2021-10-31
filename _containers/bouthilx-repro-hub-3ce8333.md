---
id: 6140
name: "bouthilx/repro-hub"
branch: "master"
tag: "3ce8333"
commit: "dc467f42e0165cc73c9a20588c65a181563a8212"
version: "6f57331a304811bccd45c32378be56cb"
build_date: "2019-01-07T08:46:00.821Z"
size_mb: 2486
size: 1508581407
sif: "https://datasets.datalad.org/shub/bouthilx/repro-hub/3ce8333/2019-01-07-dc467f42-6f57331a/6f57331a304811bccd45c32378be56cb.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bouthilx/repro-hub/3ce8333/2019-01-07-dc467f42-6f57331a/
recipe: https://datasets.datalad.org/shub/bouthilx/repro-hub/3ce8333/2019-01-07-dc467f42-6f57331a/Singularity
collection: bouthilx/repro-hub
---

# bouthilx/repro-hub:3ce8333

```bash
$ singularity pull shub://bouthilx/repro-hub:3ce8333
```

## Singularity Recipe

```singularity
BootStrap: shub
From: bouthilx/flow:pytorch.1.0.0

%labels
    AUTHOR xavier.bouthillier@umontreal.ca

% environment
    REPRO_DATA_PATH=/data

%post
    echo "------------------------------------------------------"
    echo "Installing Mahler"
    echo "------------------------------------------------------"
    pip3 install 'setuptools>=v40.1.0'
    pip3 install git+https://github.com/bouthilx/mahler.git

    echo "------------------------------------------------------"
    echo "Installing Mahler MongoDB Registry"
    echo "------------------------------------------------------"
    pip3 install git+https://github.com/bouthilx/mahler.registry.mongodb.git

    echo "------------------------------------------------------"
    echo "Installing Mahler Flow Scheduler"
    echo "------------------------------------------------------"
    pip3 install git+https://github.com/bouthilx/mahler.scheduler.flow.git

    echo "------------------------------------------------------"
    echo "Fetching repro"
    echo "------------------------------------------------------"
    cd /repos
    git clone https://gitlab.com/bouthilx/repro.git
    cd repro
        git fetch
        git checkout --track origin/dev
        git reset --hard 3ce8333

    cd ..

    echo "------------------------------------------------------"
    echo "Installing repro"
    echo "------------------------------------------------------"
    pip3 install 'setuptools>=v40.1.0'
    pip3 install --process-dependency-links -e repro[execute,configure,deploy]

    echo "------------------------------------------------------"
    echo "Cleaning up"
    echo "------------------------------------------------------"
    apt-get clean
    apt-get autoclean
    rm -rf /var/lib/apt/lists/*
```

## Collection

 - Name: [bouthilx/repro-hub](https://github.com/bouthilx/repro-hub)
 - License: [BSD 3-Clause "New" or "Revised" License](https://api.github.com/licenses/bsd-3-clause)

