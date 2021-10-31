---
id: 14075
name: "byrdsmyth/custom_highlights_baselines"
branch: "master"
tag: "custom_baselines.def"
commit: "365ba82b1b57caf794f3cbb28737ca1d288ddb55"
version: "8e4e0fd0076bde777f016c5bed79e8db4f48e4faee114b21fc191975304f01a1"
build_date: "2020-08-28T01:27:35.657Z"
size_mb: 2064.48046875
size: 2164764672
sif: "https://datasets.datalad.org/shub/byrdsmyth/custom_highlights_baselines/custom_baselines.def/2020-08-28-365ba82b-8e4e0fd0/8e4e0fd0076bde777f016c5bed79e8db4f48e4faee114b21fc191975304f01a1.sif"
url: https://datasets.datalad.org/shub/byrdsmyth/custom_highlights_baselines/custom_baselines.def/2020-08-28-365ba82b-8e4e0fd0/
recipe: https://datasets.datalad.org/shub/byrdsmyth/custom_highlights_baselines/custom_baselines.def/2020-08-28-365ba82b-8e4e0fd0/Singularity
collection: byrdsmyth/custom_highlights_baselines
---

# byrdsmyth/custom_highlights_baselines:custom_baselines.def

```bash
$ singularity pull shub://byrdsmyth/custom_highlights_baselines:custom_baselines.def
```

## Singularity Recipe

```singularity
BootStrap: docker
From: nvidia/cuda:10.1-cudnn7-devel-ubuntu18.04

%post
    # Downloads the latest package lists (important).
    apt-get update -y
    # Runs apt-get while ensuring that there are no user prompts that would
    # cause the build process to hang.
    # python3-tk is required by matplotlib.
    # python3-dev is needed to install some packages.
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        python3 \
        python3-tk \
        python3-pip \
        python3-dev
    # Reduce the size of the image by deleting the package lists we downloaded,
    # which are useless now.
    rm -rf /var/lib/apt/lists/*
    # Install Pipenv.
    pip3 install pipenv

%setup

%environment
    # Pipenv requires a certain terminal encoding.
    export LANG=C.UTF-8
    export LC_ALL=C.UTF-8
    # This configures Pipenv to store the packages in the current working
    # directory.
    export PIPENV_VENV_IN_PROJECT=1
```

## Collection

 - Name: [byrdsmyth/custom_highlights_baselines](https://github.com/byrdsmyth/custom_highlights_baselines)
 - License: [MIT License](https://api.github.com/licenses/mit)

