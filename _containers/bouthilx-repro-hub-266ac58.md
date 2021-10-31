---
id: 6136
name: "bouthilx/repro-hub"
branch: "master"
tag: "266ac58"
commit: "93eeb8d95163414b92e9b4e35b438fe1fbb52ddb"
version: "43e893db4418da895c99f8ac9fb35b50"
build_date: "2019-01-07T08:46:00.845Z"
size_mb: 2486
size: 1508577311
sif: "https://datasets.datalad.org/shub/bouthilx/repro-hub/266ac58/2019-01-07-93eeb8d9-43e893db/43e893db4418da895c99f8ac9fb35b50.simg"
url: https://datasets.datalad.org/shub/bouthilx/repro-hub/266ac58/2019-01-07-93eeb8d9-43e893db/
recipe: https://datasets.datalad.org/shub/bouthilx/repro-hub/266ac58/2019-01-07-93eeb8d9-43e893db/Singularity
collection: bouthilx/repro-hub
---

# bouthilx/repro-hub:266ac58

```bash
$ singularity pull shub://bouthilx/repro-hub:266ac58
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
        git reset --hard 266ac58

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

