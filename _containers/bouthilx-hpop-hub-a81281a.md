---
id: 8971
name: "bouthilx/hpop-hub"
branch: "master"
tag: "a81281a"
commit: "b8f22f3abb88f33a2475f99ac2fa263780052995"
version: "1022dfeb6d67f63d8ca4a4e3d96c692b"
build_date: "2019-05-09T22:11:39.998Z"
size_mb: 2748
size: 1752100895
sif: "https://datasets.datalad.org/shub/bouthilx/hpop-hub/a81281a/2019-05-09-b8f22f3a-1022dfeb/1022dfeb6d67f63d8ca4a4e3d96c692b.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bouthilx/hpop-hub/a81281a/2019-05-09-b8f22f3a-1022dfeb/
recipe: https://datasets.datalad.org/shub/bouthilx/hpop-hub/a81281a/2019-05-09-b8f22f3a-1022dfeb/Singularity
collection: bouthilx/hpop-hub
---

# bouthilx/hpop-hub:a81281a

```bash
$ singularity pull shub://bouthilx/hpop-hub:a81281a
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
            git reset --hard a81281a

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

