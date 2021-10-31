---
id: 15898
name: "XSEDE/nix-container-sc-benchmark"
branch: "master"
tag: "latest"
commit: "1a06b25e8e84c226b9b2b2b443d2a80cae2d05d2"
version: "553cf7a12de0ab737bc5902da235dbdd1979f0935952253bd054115fb7d0c504"
build_date: "2021-04-14T19:40:47.574Z"
size_mb: 733.9140625
size: 769564672
sif: "https://datasets.datalad.org/shub/XSEDE/nix-container-sc-benchmark/latest/2021-04-14-1a06b25e-553cf7a1/553cf7a12de0ab737bc5902da235dbdd1979f0935952253bd054115fb7d0c504.sif"
url: https://datasets.datalad.org/shub/XSEDE/nix-container-sc-benchmark/latest/2021-04-14-1a06b25e-553cf7a1/
recipe: https://datasets.datalad.org/shub/XSEDE/nix-container-sc-benchmark/latest/2021-04-14-1a06b25e-553cf7a1/Singularity
collection: XSEDE/nix-container-sc-benchmark
---

# XSEDE/nix-container-sc-benchmark:latest

```bash
$ singularity pull shub://XSEDE/nix-container-sc-benchmark:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: xsede/nix-sc-benchmark:testing


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
    Author steve@XCI
    Version v0.0.2

%help
    This is a testing container for converting our base CentOS Nix
    docker image into a singularity container.
```

## Collection

 - Name: [XSEDE/nix-container-sc-benchmark](https://github.com/XSEDE/nix-container-sc-benchmark)
 - License: [MIT License](https://api.github.com/licenses/mit)

