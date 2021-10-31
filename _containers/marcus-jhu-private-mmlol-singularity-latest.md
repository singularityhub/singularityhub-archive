---
id: 14252
name: "marcus-jhu-private/mmlol-singularity"
branch: "master"
tag: "latest"
commit: "996b143b1c9ce0fff9bc0fb289d47fbc4298b6f6"
version: "15d7d5caee36900ce7c544b95af74aca"
build_date: "2020-09-14T14:47:17.139Z"
size_mb: 207.0
size: 82804767
sif: "https://datasets.datalad.org/shub/marcus-jhu-private/mmlol-singularity/latest/2020-09-14-996b143b-15d7d5ca/15d7d5caee36900ce7c544b95af74aca.sif"
url: https://datasets.datalad.org/shub/marcus-jhu-private/mmlol-singularity/latest/2020-09-14-996b143b-15d7d5ca/
recipe: https://datasets.datalad.org/shub/marcus-jhu-private/mmlol-singularity/latest/2020-09-14-996b143b-15d7d5ca/Singularity
collection: marcus-jhu-private/mmlol-singularity
---

# marcus-jhu-private/mmlol-singularity:latest

```bash
$ singularity pull shub://marcus-jhu-private/mmlol-singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%post
    apt-get -y update
    apt-get -y install fortune cowsay lolcat figlet

%environment
    export LC_ALL=C
    export PATH=/usr/games:$PATH

%runscript
    figlet "JHPCE" | lolcat
```

## Collection

 - Name: [marcus-jhu-private/mmlol-singularity](https://github.com/marcus-jhu-private/mmlol-singularity)
 - License: None

