---
id: 15688
name: "yimengkong/scope9"
branch: "master"
tag: "latest"
commit: "cc734fb390894e5edca8a279da59c76b7577017f"
version: "716950837acdb8258ec6bcf33ea26f19"
build_date: "2021-03-18T20:47:43.906Z"
size_mb: 3173.0
size: 1223606303
sif: "https://datasets.datalad.org/shub/yimengkong/scope9/latest/2021-03-18-cc734fb3-71695083/716950837acdb8258ec6bcf33ea26f19.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/yimengkong/scope9/latest/2021-03-18-cc734fb3-71695083/
recipe: https://datasets.datalad.org/shub/yimengkong/scope9/latest/2021-03-18-cc734fb3-71695083/Singularity
collection: yimengkong/scope9
---

# yimengkong/scope9:latest

```bash
$ singularity pull shub://yimengkong/scope9:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:centos8

%help
For more information about 6mASCOPE, please consult https://github.com/yimengkong/6mASCOPE

# Add files to the container
%setup
    cp postInstall /tmp/postInstall
    cp -r code /tmp/code


    
# Install dependencies
%post
    # Install basic dependencies
    dnf check-update && dnf upgrade -y

    dnf install -y \
        "glibc-locale-source" \
        "glibc-langpack-en" \
        "wget" \
        "bzip2" \
        "make" \
        "perl" \
        "git" \
	    "which"


    # Include 6mASCOPE toolbox
    mkdir /sc
    mkdir /home/6mASCOPE
    
    
    # Install remaining dependencies
    mv /tmp/code /home/6mASCOPE/code
    mv /tmp/postInstall /postInstall
    bash /postInstall

    # Define working directory
    cd /home/6mASCOPE
    

    # Set default behavior
    cat > /.singularity.d/env/99-custom.sh <<EOF
export PS1="\[\033[36m\]\u\[\033[m\]@\[\033[32m\]6mASCOPE:\[\033[33;1m\]\w\[\033[m\]$ "
SINGULARITY_SHELL=/bin/bash
EOF

%environment
    export HOME=/home/6mASCOPE

%runscript
    cd /home/6mASCOPE
    exec /bin/bash

%labels
    Version v0.7.27
```

## Collection

 - Name: [yimengkong/scope9](https://github.com/yimengkong/scope9)
 - License: [MIT License](https://api.github.com/licenses/mit)

