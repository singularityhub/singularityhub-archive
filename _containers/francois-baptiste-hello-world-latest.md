---
id: 3326
name: "francois-baptiste/hello-world"
branch: "master"
tag: "latest"
commit: "3bac21df631874e3cbb3f0cf6fc9af1898f4cc3d"
version: "bf6f5eefe8752e588d741b20b4f82ece"
build_date: "2019-08-19T12:53:13.366Z"
size_mb: 204
size: 65105951
sif: "https://datasets.datalad.org/shub/francois-baptiste/hello-world/latest/2019-08-19-3bac21df-bf6f5eef/bf6f5eefe8752e588d741b20b4f82ece.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/francois-baptiste/hello-world/latest/2019-08-19-3bac21df-bf6f5eef/
recipe: https://datasets.datalad.org/shub/francois-baptiste/hello-world/latest/2019-08-19-3bac21df-bf6f5eef/Singularity
collection: francois-baptiste/hello-world
---

# francois-baptiste/hello-world:latest

```bash
$ singularity pull shub://francois-baptiste/hello-world:latest
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
rawr.sh /rawr.sh

%post
chmod u+x /rawr.sh

%runscript
exec /bin/bash /rawr.sh
```

## Collection

 - Name: [francois-baptiste/hello-world](https://github.com/francois-baptiste/hello-world)
 - License: [MIT License](https://api.github.com/licenses/mit)

