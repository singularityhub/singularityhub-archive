---
id: 6043
name: "bouthilx/repro-hub"
branch: "master"
tag: "a9eba05"
commit: "439481e125f1ed5fddca573203ec9fb7704b648c"
version: "971928bfcc81ced013ad4bdd25bb3685"
build_date: "2018-12-23T09:58:23.450Z"
size_mb: 2485
size: 1508438047
sif: "https://datasets.datalad.org/shub/bouthilx/repro-hub/a9eba05/2018-12-23-439481e1-971928bf/971928bfcc81ced013ad4bdd25bb3685.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bouthilx/repro-hub/a9eba05/2018-12-23-439481e1-971928bf/
recipe: https://datasets.datalad.org/shub/bouthilx/repro-hub/a9eba05/2018-12-23-439481e1-971928bf/Singularity
collection: bouthilx/repro-hub
---

# bouthilx/repro-hub:a9eba05

```bash
$ singularity pull shub://bouthilx/repro-hub:a9eba05
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
    echo "Fetching repro"
    echo "------------------------------------------------------"
    cd /repos
    git clone https://gitlab.com/bouthilx/repro.git
    cd repro
        git fetch
        git checkout --track origin/dev
        git reset --hard a9eba05

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

