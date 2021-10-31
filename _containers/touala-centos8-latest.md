---
id: 15106
name: "touala/centos8"
branch: "main"
tag: "latest"
commit: "07cd06832fac88ec039e8afd31c210413aed5fb5"
version: "c0c60bca445746a18db532f2e68b5b1e"
build_date: "2020-12-14T07:43:47.293Z"
size_mb: 647.0
size: 288174111
sif: "https://datasets.datalad.org/shub/touala/centos8/latest/2020-12-14-07cd0683-c0c60bca/c0c60bca445746a18db532f2e68b5b1e.sif"
url: https://datasets.datalad.org/shub/touala/centos8/latest/2020-12-14-07cd0683-c0c60bca/
recipe: https://datasets.datalad.org/shub/touala/centos8/latest/2020-12-14-07cd0683-c0c60bca/Singularity
collection: touala/centos8
---

# touala/centos8:latest

```bash
$ singularity pull shub://touala/centos8:latest
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
    dnf check-update
    dnf upgrade -y
    dnf install -y \
        "langpacks-en" \
        "glibc-all-langpacks"

    # Define working directory
    mkdir /home/centos8
    cd /home/centos8

    # Install remaining dependencies
    mv /tmp/postInstall /postInstall
    bash /postInstall

    # Set default behavior
    cat > /.singularity.d/env/99-custom.sh <<EOF
export PS1="\[\033[36m\]\u\[\033[m\]@\[\033[32m\]centos8:\[\033[33;1m\]\w\[\033[m\]$ "
SINGULARITY_SHELL=/bin/bash
EOF

%environment
    export HOME=/home/centos8

%runscript
    cd /home/centos8
    exec /bin/bash
```

## Collection

 - Name: [touala/centos8](https://github.com/touala/centos8)
 - License: None

