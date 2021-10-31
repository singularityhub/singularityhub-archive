---
id: 8526
name: "bouthilx/repro-hub"
branch: "master"
tag: "5bff981"
commit: "acb80c104d92d4fd967ad5ce258728513747e43a"
version: "d5e611231a7875e721e35373292a8240"
build_date: "2019-04-21T09:06:19.302Z"
size_mb: 2473
size: 1511415839
sif: "https://datasets.datalad.org/shub/bouthilx/repro-hub/5bff981/2019-04-21-acb80c10-d5e61123/d5e611231a7875e721e35373292a8240.simg"
url: https://datasets.datalad.org/shub/bouthilx/repro-hub/5bff981/2019-04-21-acb80c10-d5e61123/
recipe: https://datasets.datalad.org/shub/bouthilx/repro-hub/5bff981/2019-04-21-acb80c10-d5e61123/Singularity
collection: bouthilx/repro-hub
---

# bouthilx/repro-hub:5bff981

```bash
$ singularity pull shub://bouthilx/repro-hub:5bff981
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
        git reset --hard 5bff981
 
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

