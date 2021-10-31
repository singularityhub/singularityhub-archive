---
id: 2254
name: "mjstealey/r-base"
branch: "master"
tag: "latest"
commit: "9cf8d49e9a35ab138d3f02450633265b70ca801e"
version: "a572a355ba90a9de385e819245c28d85"
build_date: "2020-08-12T10:57:45.638Z"
size_mb: 666
size: 259964959
sif: "https://datasets.datalad.org/shub/mjstealey/r-base/latest/2020-08-12-9cf8d49e-a572a355/a572a355ba90a9de385e819245c28d85.simg"
url: https://datasets.datalad.org/shub/mjstealey/r-base/latest/2020-08-12-9cf8d49e-a572a355/
recipe: https://datasets.datalad.org/shub/mjstealey/r-base/latest/2020-08-12-9cf8d49e-a572a355/Singularity
collection: mjstealey/r-base
---

# mjstealey/r-base:latest

```bash
$ singularity pull shub://mjstealey/r-base:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
FROM: r-base:3.4.4

%help
  R version 3.4.4 (2018-03-15) -- "Someone to Lean On"
  Copyright (C) 2018 The R Foundation for Statistical Computing
  Platform: x86_64-pc-linux-gnu (64-bit)

  Usage:
  $ singularity run r-base.3.4.4.simg [args]
  $ singularity run --app R r-base.3.4.4.simg [args]
  $ singularity run --app Rscript r-base.3.4.4.simg [args]

%setup

%files

%labels
  Maintainer Michael J. Stealey
  Maintainer_Email stealey@renci.org
  R_Version 3.4.4

%environment
  R_BASE_VERSION=3.4.4
  LC_ALL=en_US.UTF-8
  LANG=en_US.UTF-8

%post

%apprun R
  exec R "${@}"

%apprun Rscript
  exec Rscript "${@}"

%runscript
  exec R "${@}"

%test
  exec R --version
```

## Collection

 - Name: [mjstealey/r-base](https://github.com/mjstealey/r-base)
 - License: [MIT License](https://api.github.com/licenses/mit)

