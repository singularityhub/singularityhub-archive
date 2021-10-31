---
id: 4763
name: "nuitrcs/hello-world"
branch: "master"
tag: "latest"
commit: "3554400ce3bed89ba4fc325287798f433d71e91e"
version: "f0f7f7336bd21fe552250cab6f2ee36e"
build_date: "2020-12-11T23:35:36.796Z"
size_mb: 196
size: 62603295
sif: "https://datasets.datalad.org/shub/nuitrcs/hello-world/latest/2020-12-11-3554400c-f0f7f733/f0f7f7336bd21fe552250cab6f2ee36e.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/nuitrcs/hello-world/latest/2020-12-11-3554400c-f0f7f733/
recipe: https://datasets.datalad.org/shub/nuitrcs/hello-world/latest/2020-12-11-3554400c-f0f7f733/Singularity
collection: nuitrcs/hello-world
---

# nuitrcs/hello-world:latest

```bash
$ singularity pull shub://nuitrcs/hello-world:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:14.04

%labels
MAINTAINER vanessasaur
WHATAMI dinosaur

%environment
DINOSAUR=vanessasaurus
export DINOSAUR

%files
hello.sh /hello.sh

%post
chmod u+x /hello.sh

%runscript
exec /bin/bash /hello.sh
```

## Collection

 - Name: [nuitrcs/hello-world](https://github.com/nuitrcs/hello-world)
 - License: [MIT License](https://api.github.com/licenses/mit)

