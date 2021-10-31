---
id: 6308
name: "bouthilx/repro-hub"
branch: "master"
tag: "6e61273"
commit: "5cbed0f511d5f52285794831ca4cb836e29e7ba6"
version: "a174dc282489d981eedfbbb70bdd5286"
build_date: "2019-01-18T10:30:23.387Z"
size_mb: 2502
size: 1527504927
sif: "https://datasets.datalad.org/shub/bouthilx/repro-hub/6e61273/2019-01-18-5cbed0f5-a174dc28/a174dc282489d981eedfbbb70bdd5286.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bouthilx/repro-hub/6e61273/2019-01-18-5cbed0f5-a174dc28/
recipe: https://datasets.datalad.org/shub/bouthilx/repro-hub/6e61273/2019-01-18-5cbed0f5-a174dc28/Singularity
collection: bouthilx/repro-hub
---

# bouthilx/repro-hub:6e61273

```bash
$ singularity pull shub://bouthilx/repro-hub:6e61273
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
    echo "Installing forked visdom"
    echo "------------------------------------------------------"
    pip3 install git+https://github.com/bouthilx/visdom.git

    echo "------------------------------------------------------"
    echo "Fetching repro"
    echo "------------------------------------------------------"
    cd /repos
    git clone https://gitlab.com/bouthilx/repro.git
    cd repro
        git fetch
        git checkout --track origin/dev
        git reset --hard 6e61273

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

