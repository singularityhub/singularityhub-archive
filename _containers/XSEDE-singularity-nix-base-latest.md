---
id: 13394
name: "XSEDE/singularity-nix-base"
branch: "master"
tag: "latest"
commit: "5e00031e0786f143107f46d825719fe97b4796a0"
version: "3fbb49762dc64ab98a55307deebe0671ad587a376153e6b817f6fc1fb64d634a"
build_date: "2020-06-18T16:32:24.797Z"
size_mb: 191.453125
size: 200753152
sif: "https://datasets.datalad.org/shub/XSEDE/singularity-nix-base/latest/2020-06-18-5e00031e-3fbb4976/3fbb49762dc64ab98a55307deebe0671ad587a376153e6b817f6fc1fb64d634a.sif"
url: https://datasets.datalad.org/shub/XSEDE/singularity-nix-base/latest/2020-06-18-5e00031e-3fbb4976/
recipe: https://datasets.datalad.org/shub/XSEDE/singularity-nix-base/latest/2020-06-18-5e00031e-3fbb4976/Singularity
collection: XSEDE/singularity-nix-base
---

# XSEDE/singularity-nix-base:latest

```bash
$ singularity pull shub://XSEDE/singularity-nix-base:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: xsede/centos-nix-base:latest


%runscript
    exec echo "Hello world!"
    nix-store --verify --check-contents

%test
    grep -q NAME=\"CentOS\ Linux\" /etc/os-release
    if [ $? -eq 0 ]; then
        echo "Container base is CentOS as expected."
    else
        echo "Container base is not CentOS :-("
    fi

%labels
    Author pete@XCI
    Version v0.0.1

%help
    This is a testing container for converting our base CentOS Nix
    docker image into a singularity container.
```

## Collection

 - Name: [XSEDE/singularity-nix-base](https://github.com/XSEDE/singularity-nix-base)
 - License: [MIT License](https://api.github.com/licenses/mit)

