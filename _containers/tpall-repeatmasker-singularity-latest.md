---
id: 10994
name: "tpall/repeatmasker-singularity"
branch: "conda"
tag: "latest"
commit: "bf6bfac03d40fe1ada0811ac837aea088cf3fbde"
version: "c77e13a4411c4597477b009f94de391a"
build_date: "2021-04-16T20:42:09.864Z"
size_mb: 3382.0
size: 875016223
sif: "https://datasets.datalad.org/shub/tpall/repeatmasker-singularity/latest/2021-04-16-bf6bfac0-c77e13a4/c77e13a4411c4597477b009f94de391a.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/tpall/repeatmasker-singularity/latest/2021-04-16-bf6bfac0-c77e13a4/
recipe: https://datasets.datalad.org/shub/tpall/repeatmasker-singularity/latest/2021-04-16-bf6bfac0-c77e13a4/Singularity
collection: tpall/repeatmasker-singularity
---

# tpall/repeatmasker-singularity:latest

```bash
$ singularity pull shub://tpall/repeatmasker-singularity:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: taavipall/repeatmasker-image:conda

%labels
  Maintainer tpall
  RM_Version 4.0.9
  RMBlast Version 2.9.0
  TRF Version 4.09
  Repbase_Version 20181026

%apprun RepeatMasker
  exec /usr/local/bin/RepeatMasker "${@}"

%runscript
  exec /usr/local/bin/RepeatMasker "${@}"
```

## Collection

 - Name: [tpall/repeatmasker-singularity](https://github.com/tpall/repeatmasker-singularity)
 - License: [MIT License](https://api.github.com/licenses/mit)

