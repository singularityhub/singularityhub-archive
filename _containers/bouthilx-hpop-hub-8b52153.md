---
id: 8969
name: "bouthilx/hpop-hub"
branch: "master"
tag: "8b52153"
commit: "d6b57f7f2560e7ceef41c3b9f4c79e723afd4865"
version: "a2d16ffbdf19211a40dbc75c191166e8"
build_date: "2019-05-09T22:11:40.004Z"
size_mb: 2748
size: 1752113183
sif: "https://datasets.datalad.org/shub/bouthilx/hpop-hub/8b52153/2019-05-09-d6b57f7f-a2d16ffb/a2d16ffbdf19211a40dbc75c191166e8.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bouthilx/hpop-hub/8b52153/2019-05-09-d6b57f7f-a2d16ffb/
recipe: https://datasets.datalad.org/shub/bouthilx/hpop-hub/8b52153/2019-05-09-d6b57f7f-a2d16ffb/Singularity
collection: bouthilx/hpop-hub
---

# bouthilx/hpop-hub:8b52153

```bash
$ singularity pull shub://bouthilx/hpop-hub:8b52153
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
            git reset --hard 8b52153

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

