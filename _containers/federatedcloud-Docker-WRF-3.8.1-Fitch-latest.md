---
id: 15627
name: "federatedcloud/Docker-WRF-3.8.1-Fitch"
branch: "main"
tag: "latest"
commit: "f3696601fa2630b1dfcef0c3607c0d7a0f33825c"
version: "572b28c7ee2e305f261f7df6f74ecb217b34b6b972f071c0aa0d4a7d6c69b193"
build_date: "2021-03-03T20:43:11.548Z"
size_mb: 485.5078125
size: 509091840
sif: "https://datasets.datalad.org/shub/federatedcloud/Docker-WRF-3.8.1-Fitch/latest/2021-03-03-f3696601-572b28c7/572b28c7ee2e305f261f7df6f74ecb217b34b6b972f071c0aa0d4a7d6c69b193.sif"
url: https://datasets.datalad.org/shub/federatedcloud/Docker-WRF-3.8.1-Fitch/latest/2021-03-03-f3696601-572b28c7/
recipe: https://datasets.datalad.org/shub/federatedcloud/Docker-WRF-3.8.1-Fitch/latest/2021-03-03-f3696601-572b28c7/Singularity
collection: federatedcloud/Docker-WRF-3.8.1-Fitch
---

# federatedcloud/Docker-WRF-3.8.1-Fitch:latest

```bash
$ singularity pull shub://federatedcloud/Docker-WRF-3.8.1-Fitch:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: cornellcac/wrf:3.8.1-fitch


%labels
    Author pete@CAC
    Version v0.0.1

%help
    This is a container for WRF benchmarking intended for use on XSEDE
    resources.  It uses a Ubuntu base image, adds a few dependencies,
    and compiles WPS and WRF in bash.
```

## Collection

 - Name: [federatedcloud/Docker-WRF-3.8.1-Fitch](https://github.com/federatedcloud/Docker-WRF-3.8.1-Fitch)
 - License: [BSD 3-Clause "New" or "Revised" License](https://api.github.com/licenses/bsd-3-clause)

