---
id: 6031
name: "bouthilx/repro-hub"
branch: "master"
tag: "1ca47af"
commit: "fe4823122a437d792814120d7ece23086f2b8a95"
version: "7b5e6cadd0e3873c8ac7e79290485856"
build_date: "2018-12-21T17:01:17.230Z"
size_mb: 2473
size: 1502609439
sif: "https://datasets.datalad.org/shub/bouthilx/repro-hub/1ca47af/2018-12-21-fe482312-7b5e6cad/7b5e6cadd0e3873c8ac7e79290485856.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bouthilx/repro-hub/1ca47af/2018-12-21-fe482312-7b5e6cad/
recipe: https://datasets.datalad.org/shub/bouthilx/repro-hub/1ca47af/2018-12-21-fe482312-7b5e6cad/Singularity
collection: bouthilx/repro-hub
---

# bouthilx/repro-hub:1ca47af

```bash
$ singularity pull shub://bouthilx/repro-hub:1ca47af
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
        git reset --hard 1ca47af

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

