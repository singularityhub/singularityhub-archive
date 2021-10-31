---
id: 5981
name: "bouthilx/repro-hub"
branch: "master"
tag: "6f8b90a"
commit: "4dbc4032630ecd3113b7dafa918162babef8245b"
version: "43a46309edab0fca1214c0a102fa0943"
build_date: "2018-12-16T10:26:35.850Z"
size_mb: 2499
size: 1521713183
sif: "https://datasets.datalad.org/shub/bouthilx/repro-hub/6f8b90a/2018-12-16-4dbc4032-43a46309/43a46309edab0fca1214c0a102fa0943.simg"
url: https://datasets.datalad.org/shub/bouthilx/repro-hub/6f8b90a/2018-12-16-4dbc4032-43a46309/
recipe: https://datasets.datalad.org/shub/bouthilx/repro-hub/6f8b90a/2018-12-16-4dbc4032-43a46309/Singularity
collection: bouthilx/repro-hub
---

# bouthilx/repro-hub:6f8b90a

```bash
$ singularity pull shub://bouthilx/repro-hub:6f8b90a
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
        git reset --hard 6f8b90a

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

