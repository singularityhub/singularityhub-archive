---
id: 10893
name: "okuisatoshi/singularity-vscode"
branch: "master"
tag: "latest"
commit: "fdd800d3dc8c187cc820d0e2525e13c98892c068"
version: "aa13120a223d592b31a7f1ca5f0adf9d"
build_date: "2019-11-15T16:00:35.916Z"
size_mb: 533.0
size: 172417055
sif: "https://datasets.datalad.org/shub/okuisatoshi/singularity-vscode/latest/2019-11-15-fdd800d3-aa13120a/aa13120a223d592b31a7f1ca5f0adf9d.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/okuisatoshi/singularity-vscode/latest/2019-11-15-fdd800d3-aa13120a/
recipe: https://datasets.datalad.org/shub/okuisatoshi/singularity-vscode/latest/2019-11-15-fdd800d3-aa13120a/Singularity
collection: okuisatoshi/singularity-vscode
---

# okuisatoshi/singularity-vscode:latest

```bash
$ singularity pull shub://okuisatoshi/singularity-vscode:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From: ubuntu:bionic


%post

apt-get update
apt-get install -y wget

wget https://go.microsoft.com/fwlink/?LinkID=760868 -O /tmp/vscode.deb

dpkg -i /tmp/vscode.deb || true
apt-get install -y -f
apt-get install -y libx11-xcb1 libasound2 # x11-common
apt-get clean

# Remove this dirty hack depending on my uid.
# Use singularity run -B /run ... instead.
#mkdir -p /run/user/683402166
#chmod a+rwx /run/user
#chmod a+rwx /run/user/683402166

%runscript

/usr/bin/code
```

## Collection

 - Name: [okuisatoshi/singularity-vscode](https://github.com/okuisatoshi/singularity-vscode)
 - License: None

