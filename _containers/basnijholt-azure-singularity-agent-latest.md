---
id: 12437
name: "basnijholt/azure-singularity-agent"
branch: "master"
tag: "latest"
commit: "54a481050c5a295de9ef526daa28bc9d8fb2e0a0"
version: "c2a4958a44132fe9e446b62bba270e54"
build_date: "2020-03-05T12:12:38.873Z"
size_mb: 2815.0
size: 1041600543
sif: "https://datasets.datalad.org/shub/basnijholt/azure-singularity-agent/latest/2020-03-05-54a48105-c2a4958a/c2a4958a44132fe9e446b62bba270e54.sif"
url: https://datasets.datalad.org/shub/basnijholt/azure-singularity-agent/latest/2020-03-05-54a48105-c2a4958a/
recipe: https://datasets.datalad.org/shub/basnijholt/azure-singularity-agent/latest/2020-03-05-54a48105-c2a4958a/Singularity
collection: basnijholt/azure-singularity-agent
---

# basnijholt/azure-singularity-agent:latest

```bash
$ singularity pull shub://basnijholt/azure-singularity-agent:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: jupyter/minimal-notebook

%files
    start.sh /azp/start.sh

%post
    echo "APT::Get::Assume-Yes \"true\";" > /etc/apt/apt.conf.d/90assumeyes
    apt-get update && apt-get install software-properties-common
    add-apt-repository "deb http://security.ubuntu.com/ubuntu xenial-security main" && \
      apt-get update && \
      apt-get install -y --no-install-recommends \
          ca-certificates \
          curl \
          jq \
          git \
          iputils-ping \
          libcurl4 \
          libicu55 \
          libunwind8 \
          netcat

%environment
    export XDG_RUNTIME_DIR=""
    export DEBIAN_FRONTEND=noninteractive

%runscript
    echo "Starting the Agent"
    ./start.sh

%labels
    Author Bas Nijholt <bas@nijho.lt>
```

## Collection

 - Name: [basnijholt/azure-singularity-agent](https://github.com/basnijholt/azure-singularity-agent)
 - License: [MIT License](https://api.github.com/licenses/mit)

