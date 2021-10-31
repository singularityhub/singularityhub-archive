---
id: 9948
name: "jemunro/nf-wgs-raxml-ng"
branch: "master"
tag: "r_tidy_bioc.v0.3"
commit: "d57e8829603d10d9429f0dd8d9060895b0cd279c"
version: "a806f577c51a467c8c4f93c1b22a694a"
build_date: "2019-07-04T08:37:38.153Z"
size_mb: 2893
size: 1035202591
sif: "https://datasets.datalad.org/shub/jemunro/nf-wgs-raxml-ng/r_tidy_bioc.v0.3/2019-07-04-d57e8829-a806f577/a806f577c51a467c8c4f93c1b22a694a.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jemunro/nf-wgs-raxml-ng/r_tidy_bioc.v0.3/2019-07-04-d57e8829-a806f577/
recipe: https://datasets.datalad.org/shub/jemunro/nf-wgs-raxml-ng/r_tidy_bioc.v0.3/2019-07-04-d57e8829-a806f577/Singularity
collection: jemunro/nf-wgs-raxml-ng
---

# jemunro/nf-wgs-raxml-ng:r_tidy_bioc.v0.3

```bash
$ singularity pull shub://jemunro/nf-wgs-raxml-ng:r_tidy_bioc.v0.3
```

## Singularity Recipe

```singularity
Bootstrap:docker
From: rocker/verse:3.6.0

%labels
    AUTHOR Jacob Munro

%post
    R --slave -e "install.packages('BiocManager', repos='https://cloud.r-project.org'); \
        BiocManager::install(c('GenomicRanges', 'DECIPHER', 'BioStrings', 'SeqArray', 'SeqVarTools'))"

%environment
    export R_ENVIRON=""
    export R_PROFILE=""
    export R_PROFILE_USER=""
```

## Collection

 - Name: [jemunro/nf-wgs-raxml-ng](https://github.com/jemunro/nf-wgs-raxml-ng)
 - License: None

