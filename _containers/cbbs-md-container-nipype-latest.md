---
id: 15146
name: "cbbs-md/container-nipype"
branch: "main"
tag: "latest"
commit: "43f9e13c5d49e7217740295c370035603f3e4764"
version: "82c7966c5288f256274442a8d683c6c0"
build_date: "2020-12-18T15:29:19.521Z"
size_mb: 955.0
size: 322478111
sif: "https://datasets.datalad.org/shub/cbbs-md/container-nipype/latest/2020-12-18-43f9e13c-82c7966c/82c7966c5288f256274442a8d683c6c0.sif"
url: https://datasets.datalad.org/shub/cbbs-md/container-nipype/latest/2020-12-18-43f9e13c-82c7966c/
recipe: https://datasets.datalad.org/shub/cbbs-md/container-nipype/latest/2020-12-18-43f9e13c-82c7966c/Singularity
collection: cbbs-md/container-nipype
---

# cbbs-md/container-nipype:latest

```bash
$ singularity pull shub://cbbs-md/container-nipype:latest
```

## Singularity Recipe

```singularity
# Generated by: Neurodocker version 0.7.0+0.gdc97516.dirty
# Timestamp: 2020/12/18 13:08:20 UTC
# 
# Thank you for using Neurodocker. If you discover any issues
# or ways to improve this software, please submit an issue or
# pull request on our GitHub repository:
# 
#     https://github.com/ReproNim/neurodocker

Bootstrap: docker
From: debian:stretch

%post
su - root

export ND_ENTRYPOINT="/neurodocker/startup.sh"
apt-get update -qq
apt-get install -y -q --no-install-recommends \
    apt-utils \
    bzip2 \
    ca-certificates \
    curl \
    locales \
    unzip
apt-get clean
rm -rf /var/lib/apt/lists/*
sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen
dpkg-reconfigure --frontend=noninteractive locales
update-locale LANG="en_US.UTF-8"
chmod 777 /opt && chmod a+s /opt
mkdir -p /neurodocker
if [ ! -f "$ND_ENTRYPOINT" ]; then
  echo '#!/usr/bin/env bash' >> "$ND_ENTRYPOINT"
  echo 'set -e' >> "$ND_ENTRYPOINT"
  echo 'export USER="${USER:=`whoami`}"' >> "$ND_ENTRYPOINT"
  echo 'if [ -n "$1" ]; then "$@"; else /usr/bin/env bash; fi' >> "$ND_ENTRYPOINT";
fi
chmod -R 777 /neurodocker && chmod a+s /neurodocker

export PATH="/opt/miniconda-latest/bin:$PATH"
echo "Downloading Miniconda installer ..."
conda_installer="/tmp/miniconda.sh"
curl -fsSL --retry 5 -o "$conda_installer" https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash "$conda_installer" -b -p /opt/miniconda-latest
rm -f "$conda_installer"
conda update -yq -nbase conda
conda config --system --prepend channels conda-forge
conda config --system --set auto_update_conda false
conda config --system --set show_channel_urls true
sync && conda clean -y --all && sync
conda create -y -q --name neuro
conda install -y -q --name neuro \
    "python=3.6" \
    "traits"
sync && conda clean -y --all && sync
bash -c "source activate neuro
  pip install --no-cache-dir  \
      "nipype""
rm -rf ~/.cache/pip/*
sync


echo '{
\n  "pkg_manager": "apt",
\n  "instructions": [
\n    [
\n      "base",
\n      "debian:stretch"
\n    ],
\n    [
\n      "user",
\n      "root"
\n    ],
\n    [
\n      "_header",
\n      {
\n        "version": "generic",
\n        "method": "custom"
\n      }
\n    ],
\n    [
\n      "miniconda",
\n      {
\n        "create_env": "neuro",
\n        "conda_install": [
\n          "python=3.6",
\n          "traits"
\n        ],
\n        "pip_install": [
\n          "nipype"
\n        ]
\n      }
\n    ]
\n  ]
\n}' > /neurodocker/neurodocker_specs.json

%environment
export LANG="en_US.UTF-8"
export LC_ALL="en_US.UTF-8"
export ND_ENTRYPOINT="/neurodocker/startup.sh"
export CONDA_DIR="/opt/miniconda-latest"
export PATH="/opt/miniconda-latest/bin:$PATH"

%runscript
/neurodocker/startup.sh "$@"
```

## Collection

 - Name: [cbbs-md/container-nipype](https://github.com/cbbs-md/container-nipype)
 - License: None
