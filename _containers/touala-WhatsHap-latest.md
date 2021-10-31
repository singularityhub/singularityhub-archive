---
id: 14542
name: "touala/WhatsHap"
branch: "main"
tag: "latest"
commit: "786f2ee45df4e7f92b34674c0e82ed14f6a3db9a"
version: "87b9366ceea39a86b8e55d0310921304"
build_date: "2020-10-03T07:25:50.043Z"
size_mb: 1543.0
size: 619876383
sif: "https://datasets.datalad.org/shub/touala/WhatsHap/latest/2020-10-03-786f2ee4-87b9366c/87b9366ceea39a86b8e55d0310921304.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/touala/WhatsHap/latest/2020-10-03-786f2ee4-87b9366c/
recipe: https://datasets.datalad.org/shub/touala/WhatsHap/latest/2020-10-03-786f2ee4-87b9366c/Singularity
collection: touala/WhatsHap
---

# touala/WhatsHap:latest

```bash
$ singularity pull shub://touala/WhatsHap:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:centos8

%help
For more information, please consult https://github.com/touala/WhatsHap

# Add files to the container
%setup
    cp postInstall /tmp/postInstall

# Install dependencies
%post
    # Install basic dependencies
    dnf check-update && dnf upgrade -y && dnf install -y \
        "langpacks-en" \
        "glibc-all-langpacks"

    # Define working directory
    mkdir /home/whatshap
    cd /home/whatshap

    # Install remaining dependencies
    mv /tmp/postInstall /postInstall
    bash /postInstall

    # Set default behavior
    cat > /.singularity.d/env/99-custom.sh <<EOF
export PS1="\[\033[36m\]\u\[\033[m\]@\[\033[32m\]WhatsHap:\[\033[33;1m\]\w\[\033[m\]$ "
SINGULARITY_SHELL=/bin/bash
EOF

%environment
    export HOME=/home/whatshap

%runscript
    cd /home/whatshap
    exec /bin/bash
```

## Collection

 - Name: [touala/WhatsHap](https://github.com/touala/WhatsHap)
 - License: None

