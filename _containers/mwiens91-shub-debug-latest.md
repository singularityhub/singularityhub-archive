---
id: 3984
name: "mwiens91/shub-debug"
branch: "master"
tag: "latest"
commit: "d13898a106f9678c695ab479335e285c634d3686"
version: "07299790f4a52fdfeb6e95aa6fa97eaf"
build_date: "2020-12-21T16:26:44.651Z"
size_mb: 172
size: 78774303
sif: "https://datasets.datalad.org/shub/mwiens91/shub-debug/latest/2020-12-21-d13898a1-07299790/07299790f4a52fdfeb6e95aa6fa97eaf.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/mwiens91/shub-debug/latest/2020-12-21-d13898a1-07299790/
recipe: https://datasets.datalad.org/shub/mwiens91/shub-debug/latest/2020-12-21-d13898a1-07299790/Singularity
collection: mwiens91/shub-debug
---

# mwiens91/shub-debug:latest

```bash
$ singularity pull shub://mwiens91/shub-debug:latest
```

## Singularity Recipe

```singularity
BootStrap: debootstrap
OSVersion: stable
MirrorURL: http://ftp.us.debian.org/debian/

%runscript
    echo "Hello world 2! :D"
```

## Collection

 - Name: [mwiens91/shub-debug](https://github.com/mwiens91/shub-debug)
 - License: None

