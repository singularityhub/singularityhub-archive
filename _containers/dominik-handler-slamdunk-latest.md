---
id: 1770
name: "dominik-handler/slamdunk"
branch: "singularity"
tag: "latest"
commit: "a9f28bb632a58fd3a6b26f469f929ed94394a89b"
version: "703b4d19d5813b716c61a27e4e6ed16b"
build_date: "2018-02-19T14:56:31.796Z"
size_mb: 1532
size: 541261855
sif: "https://datasets.datalad.org/shub/dominik-handler/slamdunk/latest/2018-02-19-a9f28bb6-703b4d19/703b4d19d5813b716c61a27e4e6ed16b.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/dominik-handler/slamdunk/latest/2018-02-19-a9f28bb6-703b4d19/
recipe: https://datasets.datalad.org/shub/dominik-handler/slamdunk/latest/2018-02-19-a9f28bb6-703b4d19/Singularity
collection: dominik-handler/slamdunk
---

# dominik-handler/slamdunk:latest

```bash
$ singularity pull shub://dominik-handler/slamdunk:latest
```

## Singularity Recipe

```singularity
BootStrap:docker
From:tobneu/slamdunk
%runscript

%post
# Tobias Neumann <tobias.neumann.at@gmail.com>
export SLAMDUNK_VERSION=0.2.3-dev
echo "
export SLAMDUNK_VERSION=0.2.3-dev" >> /environment
mkdir /clustertmp
mkdir /scratch
mkdir /scratch-ii2
mkdir /groups
```

## Collection

 - Name: [dominik-handler/slamdunk](https://github.com/dominik-handler/slamdunk)
 - License: None

