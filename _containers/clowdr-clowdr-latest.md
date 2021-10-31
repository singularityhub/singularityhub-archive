---
id: 1892
name: "clowdr/clowdr"
branch: "master"
tag: "latest"
commit: "f882994e8ec7ea0cf034662fceb1ef517ff72710"
version: "1985ab9121d27aec03daade523c0d64b"
build_date: "2021-01-24T02:14:56.761Z"
size_mb: 351
size: 98971679
sif: "https://datasets.datalad.org/shub/clowdr/clowdr/latest/2021-01-24-f882994e-1985ab91/1985ab9121d27aec03daade523c0d64b.simg"
url: https://datasets.datalad.org/shub/clowdr/clowdr/latest/2021-01-24-f882994e-1985ab91/
recipe: https://datasets.datalad.org/shub/clowdr/clowdr/latest/2021-01-24-f882994e-1985ab91/Singularity
collection: clowdr/clowdr
---

# clowdr/clowdr:latest

```bash
$ singularity pull shub://clowdr/clowdr:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: clowdr/clowdr

%runscript
    exec clowdr "$@"

%labels
Author greg.kiar@mail.mcgill.ca
Build-date 28/02/2018
Vendor Alpine

%post
    echo "For more information on clowdr, go to:"
    echo "http://clowdr.github.io"
```

## Collection

 - Name: [clowdr/clowdr](https://github.com/clowdr/clowdr)
 - License: [MIT License](https://api.github.com/licenses/mit)

