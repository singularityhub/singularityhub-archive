---
id: 3958
name: "riyas-org/r-base"
branch: "master"
tag: "latest"
commit: "9cf8d49e9a35ab138d3f02450633265b70ca801e"
version: "4bc0bcdb8e3b4e168239ce18684f1083"
build_date: "2020-04-14T12:22:27.264Z"
size_mb: 669
size: 260358175
sif: "https://datasets.datalad.org/shub/riyas-org/r-base/latest/2020-04-14-9cf8d49e-4bc0bcdb/4bc0bcdb8e3b4e168239ce18684f1083.simg"
url: https://datasets.datalad.org/shub/riyas-org/r-base/latest/2020-04-14-9cf8d49e-4bc0bcdb/
recipe: https://datasets.datalad.org/shub/riyas-org/r-base/latest/2020-04-14-9cf8d49e-4bc0bcdb/Singularity
collection: riyas-org/r-base
---

# riyas-org/r-base:latest

```bash
$ singularity pull shub://riyas-org/r-base:latest
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

 - Name: [riyas-org/r-base](https://github.com/riyas-org/r-base)
 - License: [MIT License](https://api.github.com/licenses/mit)

