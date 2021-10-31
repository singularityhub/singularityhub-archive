---
id: 8972
name: "bouthilx/hpop-hub"
branch: "master"
tag: "d0a3569"
commit: "e2ddffaffe5738162aca379ca0c6efabcb70dec5"
version: "5e926d3daae9c5a32e957eeaf9a2d388"
build_date: "2019-05-09T22:11:39.992Z"
size_mb: 2748
size: 1752121375
sif: "https://datasets.datalad.org/shub/bouthilx/hpop-hub/d0a3569/2019-05-09-e2ddffaf-5e926d3d/5e926d3daae9c5a32e957eeaf9a2d388.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bouthilx/hpop-hub/d0a3569/2019-05-09-e2ddffaf-5e926d3d/
recipe: https://datasets.datalad.org/shub/bouthilx/hpop-hub/d0a3569/2019-05-09-e2ddffaf-5e926d3d/Singularity
collection: bouthilx/hpop-hub
---

# bouthilx/hpop-hub:d0a3569

```bash
$ singularity pull shub://bouthilx/hpop-hub:d0a3569
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
            git reset --hard d0a3569

        cd ..

    echo "------------------------------------------------------"
    echo "Installing repro"
    echo "------------------------------------------------------"
    pip3 install --process-dependency-links -e repro[coco,mini]

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

