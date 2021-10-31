---
id: 8966
name: "bouthilx/hpop-hub"
branch: "master"
tag: "725ee25"
commit: "cb8601f3f2f0bb5adde884334fccfa7ce72ad746"
version: "5fa667daa3b8abbb784571decb86cf05"
build_date: "2019-05-09T13:15:27.248Z"
size_mb: 2748
size: 1752104991
sif: "https://datasets.datalad.org/shub/bouthilx/hpop-hub/725ee25/2019-05-09-cb8601f3-5fa667da/5fa667daa3b8abbb784571decb86cf05.simg"
url: https://datasets.datalad.org/shub/bouthilx/hpop-hub/725ee25/2019-05-09-cb8601f3-5fa667da/
recipe: https://datasets.datalad.org/shub/bouthilx/hpop-hub/725ee25/2019-05-09-cb8601f3-5fa667da/Singularity
collection: bouthilx/hpop-hub
---

# bouthilx/hpop-hub:725ee25

```bash
$ singularity pull shub://bouthilx/hpop-hub:725ee25
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
            git reset --hard 725ee25

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

