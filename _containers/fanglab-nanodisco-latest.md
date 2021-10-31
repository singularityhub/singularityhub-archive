---
id: 15132
name: "fanglab/nanodisco"
branch: "master"
tag: "latest"
commit: "11c4334091f4637c9d62e6131dc7a6b90bcc6327"
version: "5bbc988da1eaacc68bddcdca8b200380"
build_date: "2021-04-19T00:48:46.596Z"
size_mb: 3774.0
size: 2002186271
sif: "https://datasets.datalad.org/shub/fanglab/nanodisco/latest/2021-04-19-11c43340-5bbc988d/5bbc988da1eaacc68bddcdca8b200380.sif"
url: https://datasets.datalad.org/shub/fanglab/nanodisco/latest/2021-04-19-11c43340-5bbc988d/
recipe: https://datasets.datalad.org/shub/fanglab/nanodisco/latest/2021-04-19-11c43340-5bbc988d/Singularity
collection: fanglab/nanodisco
---

# fanglab/nanodisco:latest

```bash
$ singularity pull shub://fanglab/nanodisco:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: rocker/r-ver:3.5.3

%help
For more information, please consult https://github.com/fanglab/nanodisco

# Add files to the container
%setup
    cp postInstall /tmp/postInstall
    cp -r code /tmp/code

# Install dependencies
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
    && rm -rf /var/lib/apt/lists/*

    # Prepare for devtools dependencies
    apt-get update && apt-get install -y --no-install-recommends "cmake" "libgit2-dev" && rm -rf /var/lib/apt/lists/*

    # Include nanodisco toolbox
    mkdir /home/nanodisco
    mv /tmp/code /home/nanodisco/code

    # Install remaining dependencies from sources (nanopolish, bwa, samtools, R packages, MEME, bedtools)
    mv /tmp/postInstall /postInstall
    bash /postInstall

    # Define working directory
    cd /home/nanodisco

    # Create folders for analysis
    mkdir /home/nanodisco/analysis
    mkdir /home/nanodisco/dataset
    
    # Set default behavior
    cat > /.singularity.d/env/99-custom.sh <<EOF
export PS1="\[\033[36m\]\u\[\033[m\]@\[\033[32m\]nanodisco:\[\033[33;1m\]\w\[\033[m\]$ "
SINGULARITY_SHELL=/bin/bash
EOF

%environment
    export HOME=/home/nanodisco

%runscript
    cd /home/nanodisco
    exec /bin/bash
```

## Collection

 - Name: [fanglab/nanodisco](https://github.com/fanglab/nanodisco)
 - License: None

