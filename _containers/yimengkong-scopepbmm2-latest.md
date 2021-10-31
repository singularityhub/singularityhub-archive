---
id: 15803
name: "yimengkong/scopepbmm2"
branch: "master"
tag: "latest"
commit: "28a7c237e25aa81c31385b5ae6bf53b63deca932"
version: "4894f78956c0e19344d185226f684d2c"
build_date: "2021-03-25T01:48:49.082Z"
size_mb: 3184.0
size: 1228075039
sif: "https://datasets.datalad.org/shub/yimengkong/scopepbmm2/latest/2021-03-25-28a7c237-4894f789/4894f78956c0e19344d185226f684d2c.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/yimengkong/scopepbmm2/latest/2021-03-25-28a7c237-4894f789/
recipe: https://datasets.datalad.org/shub/yimengkong/scopepbmm2/latest/2021-03-25-28a7c237-4894f789/Singularity
collection: yimengkong/scopepbmm2
---

# yimengkong/scopepbmm2:latest

```bash
$ singularity pull shub://yimengkong/scopepbmm2:latest
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
    Version v0.7.28
```

## Collection

 - Name: [yimengkong/scopepbmm2](https://github.com/yimengkong/scopepbmm2)
 - License: [MIT License](https://api.github.com/licenses/mit)

