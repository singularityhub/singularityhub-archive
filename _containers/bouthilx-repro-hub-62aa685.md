---
id: 5978
name: "bouthilx/repro-hub"
branch: "master"
tag: "62aa685"
commit: "aefeff285718d35c7cda72bcac531fe82060d481"
version: "bf1716222afd77b6cf4fd1fd8a5a21ea"
build_date: "2018-12-15T06:55:31.577Z"
size_mb: 2499
size: 1521704991
sif: "https://datasets.datalad.org/shub/bouthilx/repro-hub/62aa685/2018-12-15-aefeff28-bf171622/bf1716222afd77b6cf4fd1fd8a5a21ea.simg"
url: https://datasets.datalad.org/shub/bouthilx/repro-hub/62aa685/2018-12-15-aefeff28-bf171622/
recipe: https://datasets.datalad.org/shub/bouthilx/repro-hub/62aa685/2018-12-15-aefeff28-bf171622/Singularity
collection: bouthilx/repro-hub
---

# bouthilx/repro-hub:62aa685

```bash
$ singularity pull shub://bouthilx/repro-hub:62aa685
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
        git reset --hard 62aa685

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

