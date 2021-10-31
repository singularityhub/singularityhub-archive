---
id: 12146
name: "touala/meme"
branch: "master"
tag: "latest"
commit: "20ced9f2606ad9cdafb90e3be51ecbb39e5f9565"
version: "41788dea9e870ba23aa448a8dec20452"
build_date: "2020-01-31T16:50:14.581Z"
size_mb: 1198.0
size: 399503391
sif: "https://datasets.datalad.org/shub/touala/meme/latest/2020-01-31-20ced9f2-41788dea/41788dea9e870ba23aa448a8dec20452.sif"
url: https://datasets.datalad.org/shub/touala/meme/latest/2020-01-31-20ced9f2-41788dea/
recipe: https://datasets.datalad.org/shub/touala/meme/latest/2020-01-31-20ced9f2-41788dea/Singularity
collection: touala/meme
---

# touala/meme:latest

```bash
$ singularity pull shub://touala/meme:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: rocker/r-ver:3.5.3

%files
    postInstall /
    
%post
    # Install basic dependencies
    apt-get update && apt-get install -y --no-install-recommends \
    "vim" \
    "git" \
    "wget" \
    "bzip2" \
    "parallel" \
    "python" \
    "ghostscript" \
    "libcurl4-openssl-dev" \
    "libssl-dev" \
    "libxml2-dev" \
    "libxslt1-dev" \
    "zlib1g-dev" \
    "libncurses5-dev" \
    "libncursesw5-dev" \
    "libexpat1-dev" \
    "libjson-perl" \
    "libhtml-tree-perl" \
    "libbz2-dev" \
    "liblzma-dev" \
    "openmpi-bin" \
    "libopenmpi-dev" \
    "openssh-client" \
    "openssh-server" \
    "libibverbs-dev" \
    && rm -rf /var/lib/apt/lists/*

    mkdir /home/meme
    bash /postInstall

    # Define working directory
    cd /home/meme

    # Create folders for analysis
    mkdir /home/meme/analysis
    mkdir /home/meme/dataset

%environment
    export HOME=/home/meme
```

## Collection

 - Name: [touala/meme](https://github.com/touala/meme)
 - License: None

