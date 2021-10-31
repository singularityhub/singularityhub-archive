---
id: 8926
name: "bouthilx/hpop-hub"
branch: "master"
tag: "d254e07"
commit: "a99d9bc9fb05afbb6c69e3e4a2207eed804aa346"
version: "a3e851529edd2c983cfccb4c318be595"
build_date: "2019-05-08T15:10:10.719Z"
size_mb: 2723
size: 1743126559
sif: "https://datasets.datalad.org/shub/bouthilx/hpop-hub/d254e07/2019-05-08-a99d9bc9-a3e85152/a3e851529edd2c983cfccb4c318be595.simg"
url: https://datasets.datalad.org/shub/bouthilx/hpop-hub/d254e07/2019-05-08-a99d9bc9-a3e85152/
recipe: https://datasets.datalad.org/shub/bouthilx/hpop-hub/d254e07/2019-05-08-a99d9bc9-a3e85152/Singularity
collection: bouthilx/hpop-hub
---

# bouthilx/hpop-hub:d254e07

```bash
$ singularity pull shub://bouthilx/hpop-hub:d254e07
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
    echo "Updating setuptools"
    echo "------------------------------------------------------"
    pip3 install 'setuptools>=v40.1.0'

    echo "------------------------------------------------------"
    echo "Installing coco"
    echo "------------------------------------------------------"
    pip3 install numpy scipy
    cd /repos
      git clone https://github.com/numbbo/coco.git
      cd coco
          python3.6 do.py run-python
      cd ..

    echo "------------------------------------------------------"
    echo "Installing mahler"
    echo "------------------------------------------------------"

    pip3 install --upgrade git+https://github.com/bouthilx/mahler.git
    pip3 install --upgrade git+https://github.com/bouthilx/mahler.registry.mongodb.git

    echo "------------------------------------------------------"
    echo "Fetching repro"
    echo "------------------------------------------------------"
    cd /repos
        git clone https://gitlab.com/bouthilx/repro.git
        cd repro
            git fetch
            git checkout --track origin/dev
            git reset --hard d254e07

        cd ..

    echo "------------------------------------------------------"
    echo "Installing repro"
    echo "------------------------------------------------------"
    pip3 install --process-dependency-links -e repro[coco]

    echo "------------------------------------------------------"
    echo "Cleaning up"
    echo "------------------------------------------------------"
    apt-get clean
    apt-get autoclean
    rm -rf /var/lib/apt/lists/*
```

## Collection

 - Name: [bouthilx/hpop-hub](https://github.com/bouthilx/hpop-hub)
 - License: None

