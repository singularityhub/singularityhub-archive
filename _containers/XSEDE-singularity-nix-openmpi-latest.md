---
id: 13399
name: "XSEDE/singularity-nix-openmpi"
branch: "master"
tag: "latest"
commit: "659a655f736fa377e443278f29a6b773d9f08e56"
version: "0f16369e959bf0fa6bdec7395bb6699fbfad1b196e9a9d35944354c9121ec665"
build_date: "2021-03-05T21:24:48.722Z"
size_mb: 439.1875
size: 460521472
sif: "https://datasets.datalad.org/shub/XSEDE/singularity-nix-openmpi/latest/2021-03-05-659a655f-0f16369e/0f16369e959bf0fa6bdec7395bb6699fbfad1b196e9a9d35944354c9121ec665.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/XSEDE/singularity-nix-openmpi/latest/2021-03-05-659a655f-0f16369e/
recipe: https://datasets.datalad.org/shub/XSEDE/singularity-nix-openmpi/latest/2021-03-05-659a655f-0f16369e/Singularity
collection: XSEDE/singularity-nix-openmpi
---

# XSEDE/singularity-nix-openmpi:latest

```bash
$ singularity pull shub://XSEDE/singularity-nix-openmpi:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: xsede/centos-nix-openmpi:latest


%runscript
    #nix-store --verify --check-contents
    nix-shell /root/dev.nix

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
    This is a testing container for OpenMPI in a docker image
    based on CentOS with Nix converted to a singularity container.
    Original dockerfile from:
    https://github.com/XSEDE/docker-centos-nix-openmpi
```

## Collection

 - Name: [XSEDE/singularity-nix-openmpi](https://github.com/XSEDE/singularity-nix-openmpi)
 - License: [MIT License](https://api.github.com/licenses/mit)

