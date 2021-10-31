---
id: 2540
name: "bouthilx/qtrack"
branch: "master"
tag: "flow"
commit: "a0194a86d4f11a2bbf39bdef4ed20fc2ea064dd5"
version: "1dae58e223f181f36016eb1c3d5b2580"
build_date: "2018-04-15T03:24:04.340Z"
size_mb: 2216
size: 1013133343
sif: "https://datasets.datalad.org/shub/bouthilx/qtrack/flow/2018-04-15-a0194a86-1dae58e2/1dae58e223f181f36016eb1c3d5b2580.simg"
url: https://datasets.datalad.org/shub/bouthilx/qtrack/flow/2018-04-15-a0194a86-1dae58e2/
recipe: https://datasets.datalad.org/shub/bouthilx/qtrack/flow/2018-04-15-a0194a86-1dae58e2/Singularity
collection: bouthilx/qtrack
---

# bouthilx/qtrack:flow

```bash
$ singularity pull shub://bouthilx/qtrack:flow
```

## Singularity Recipe

```singularity
BootStrap: shub
From: bouthilx/flow:pytorch.0.3.1

%labels
   AUTHOR xavier.bouthillier@umontreal.ca

%post
	export GITHUB_TOKEN="e209b24443c2fefa895c81d80957b838df6c68d7"

    echo "------------------------------------------------------"
    echo "Installing Tensorflow for tensor-board"
    echo "------------------------------------------------------"
	pip3 install tensorflow==1.5

    echo "------------------------------------------------------"
    echo "Installing custom Sacred"
    echo "------------------------------------------------------"
    cd /repos
	git clone https://${GITHUB_TOKEN}@github.com/bouthilx/impn.git qtrack
    cd qtrack
        git fetch
        git checkout --track origin/qtrack
        git submodule init
        git submodule update
        cd protopt
            git submodule init
            git submodule update
        cd ..

        # pip3 install git+https://${GITHUB_TOKEN}@github.com/bouthilx/sacred.git@b4b90b859df83e880b51bc60f79ebd2f93747749

        pip3 install protopt/sacred

        echo "------------------------------------------------------"
        echo "Installing custom SmartDispatch"
        echo "------------------------------------------------------"

        # pip3 install git+https://${GITHUB_TOKEN}@github.com/bouthilx/smartdispatch.git@971960ae65c9da42732284904d0860c3009c0b77

        pip3 install protopt/smartdispatch

    cd ..

    echo "------------------------------------------------------"
    echo "Installing Protopt"
    echo "------------------------------------------------------"
    pip3 install qtrack/protopt

    echo "------------------------------------------------------"
    echo "Installing IMPN"
    echo "------------------------------------------------------"
    # pip3 install future
    pip3 install qtrack/

    echo "------------------------------------------------------"
    echo "Cleaning up"
    echo "------------------------------------------------------"
    apt-get clean
    apt-get autoclean
    rm -rf /var/lib/apt/lists/*
```

## Collection

 - Name: [bouthilx/qtrack](https://github.com/bouthilx/qtrack)
 - License: None

