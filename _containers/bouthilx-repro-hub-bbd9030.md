---
id: 8665
name: "bouthilx/repro-hub"
branch: "master"
tag: "bbd9030"
commit: "ef354965306a3fa66198c2a426380994f8034a47"
version: "9f4937eee009080d8036de6e8250244d"
build_date: "2019-04-25T22:56:38.595Z"
size_mb: 2473
size: 1511485471
sif: "https://datasets.datalad.org/shub/bouthilx/repro-hub/bbd9030/2019-04-25-ef354965-9f4937ee/9f4937eee009080d8036de6e8250244d.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bouthilx/repro-hub/bbd9030/2019-04-25-ef354965-9f4937ee/
recipe: https://datasets.datalad.org/shub/bouthilx/repro-hub/bbd9030/2019-04-25-ef354965-9f4937ee/Singularity
collection: bouthilx/repro-hub
---

# bouthilx/repro-hub:bbd9030

```bash
$ singularity pull shub://bouthilx/repro-hub:bbd9030
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
        git reset --hard bbd9030
 
    cd ..

    echo "------------------------------------------------------"
    echo "Installing repro"
    echo "------------------------------------------------------"
    pip3 install 'setuptools>=v40.1.0'
    pip3 install --process-dependency-links -e repro[execute,configure]

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

