---
id: 6150
name: "bahlolab/nf-pacbio-amplicon-analysis"
branch: "master"
tag: "rocker_verse"
commit: "1d38343370072d80bc44780b7f0959bda0dc38e8"
version: "d418fea939f659fe3bbd76a63fd338f9"
build_date: "2019-01-09T08:35:39.962Z"
size_mb: 2447
size: 915968031
sif: "https://datasets.datalad.org/shub/bahlolab/nf-pacbio-amplicon-analysis/rocker_verse/2019-01-09-1d383433-d418fea9/d418fea939f659fe3bbd76a63fd338f9.simg"
url: https://datasets.datalad.org/shub/bahlolab/nf-pacbio-amplicon-analysis/rocker_verse/2019-01-09-1d383433-d418fea9/
recipe: https://datasets.datalad.org/shub/bahlolab/nf-pacbio-amplicon-analysis/rocker_verse/2019-01-09-1d383433-d418fea9/Singularity
collection: bahlolab/nf-pacbio-amplicon-analysis
---

# bahlolab/nf-pacbio-amplicon-analysis:rocker_verse

```bash
$ singularity pull shub://bahlolab/nf-pacbio-amplicon-analysis:rocker_verse
```

## Singularity Recipe

```singularity
Bootstrap:docker
From: rocker/verse:3.5.0

%labels
  AUTHOR Jacob Munro
  AUTHOR bahlolab

%environment
    export R_ENVIRON=""
    export R_PROFILE=""
    export R_PROFILE_USER=""
```

## Collection

 - Name: [bahlolab/nf-pacbio-amplicon-analysis](https://github.com/bahlolab/nf-pacbio-amplicon-analysis)
 - License: None

