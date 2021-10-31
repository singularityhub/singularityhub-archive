---
id: 905
name: "bbbbbrie/singularity-cookbook"
branch: "master"
tag: "latest"
commit: "60dc9b08eb07b0e7276f2c017443003278582619"
version: "d89ce593b3203629a4b7b78f00625901"
build_date: "2020-09-21T08:16:17.663Z"
size_mb: 1922
size: 1105956895
sif: "https://datasets.datalad.org/shub/bbbbbrie/singularity-cookbook/latest/2020-09-21-60dc9b08-d89ce593/d89ce593b3203629a4b7b78f00625901.simg"
url: https://datasets.datalad.org/shub/bbbbbrie/singularity-cookbook/latest/2020-09-21-60dc9b08-d89ce593/
recipe: https://datasets.datalad.org/shub/bbbbbrie/singularity-cookbook/latest/2020-09-21-60dc9b08-d89ce593/Singularity
collection: bbbbbrie/singularity-cookbook
---

# bbbbbrie/singularity-cookbook:latest

```bash
$ singularity pull shub://bbbbbrie/singularity-cookbook:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:artful

%post
    apt-get -y update && apt-get -y install python3 python3-pip texlive-xetex && pip3 install jupyter && pip3 install --upgrade pip
```

## Collection

 - Name: [bbbbbrie/singularity-cookbook](https://github.com/bbbbbrie/singularity-cookbook)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

