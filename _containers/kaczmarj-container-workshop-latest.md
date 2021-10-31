---
id: 1258
name: "kaczmarj/container-workshop"
branch: "master"
tag: "latest"
commit: "969e0c7a5173b9d43c9cf99fd00b29742d2a181c"
version: "32ed4b2c6c0be1f6f0b44ba26c716ae8"
build_date: "2018-01-10T22:51:11.538Z"
size_mb: 225
size: 77090847
sif: "https://datasets.datalad.org/shub/kaczmarj/container-workshop/latest/2018-01-10-969e0c7a-32ed4b2c/32ed4b2c6c0be1f6f0b44ba26c716ae8.simg"
url: https://datasets.datalad.org/shub/kaczmarj/container-workshop/latest/2018-01-10-969e0c7a-32ed4b2c/
recipe: https://datasets.datalad.org/shub/kaczmarj/container-workshop/latest/2018-01-10-969e0c7a-32ed4b2c/Singularity
collection: kaczmarj/container-workshop
---

# kaczmarj/container-workshop:latest

```bash
$ singularity pull shub://kaczmarj/container-workshop:latest
```

## Singularity Recipe

```singularity
# Start off with a fresh Ubuntu 16.04 base.
Bootstrap: docker
From: ubuntu:16.04

%post
# Install packages.
apt-get update -qq
apt-get install -y -q git python3
# Remove unnecessary files to keep our image small.
apt-get clean
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

%files
# Copy file from the host machine into the container.
helloworld.py /opt/helloworld.py

%runscript
python3 /opt/helloworld.py
```

## Collection

 - Name: [kaczmarj/container-workshop](https://github.com/kaczmarj/container-workshop)
 - License: None

