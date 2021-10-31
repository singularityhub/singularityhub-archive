---
id: 12046
name: "touala/smtm"
branch: "master"
tag: "latest"
commit: "5911b80fec72bf6d11de15ea9835b1db8031ab36"
version: "8d222b87294de1f027d54c329d944b6d"
build_date: "2020-02-15T16:31:40.498Z"
size_mb: 3559.0
size: 1975193631
sif: "https://datasets.datalad.org/shub/touala/smtm/latest/2020-02-15-5911b80f-8d222b87/8d222b87294de1f027d54c329d944b6d.sif"
url: https://datasets.datalad.org/shub/touala/smtm/latest/2020-02-15-5911b80f-8d222b87/
recipe: https://datasets.datalad.org/shub/touala/smtm/latest/2020-02-15-5911b80f-8d222b87/Singularity
collection: touala/smtm
---

# touala/smtm:latest

```bash
$ singularity pull shub://touala/smtm:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: rocker/r-ver:3.5.3

%help
For more information, please consult https://github.com/touala/nanodisco

# Add files to the container
%files
    postInstall /
    code /tmp/code

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

    # Include nanodisco toolbox
    mkdir /home/nanodisco
    mv /tmp/code /home/nanodisco/code

    # Install remaining dependencies from sources (nanopolish, bwa, samtools, R packages, MEME, bedtools)
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

 - Name: [touala/smtm](https://github.com/touala/smtm)
 - License: None

