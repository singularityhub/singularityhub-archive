---
id: 6681
name: "bahlolab/nf-pacbio-amplicon-analysis"
branch: "master"
tag: "r_v0.1"
commit: "dacbc3811248fac591099a58bc8e46fe6c9a788a"
version: "f6a81dfb577f3bc0bdfa34f8829b102b"
build_date: "2019-01-29T08:08:17.756Z"
size_mb: 2456
size: 919265311
sif: "https://datasets.datalad.org/shub/bahlolab/nf-pacbio-amplicon-analysis/r_v0.1/2019-01-29-dacbc381-f6a81dfb/f6a81dfb577f3bc0bdfa34f8829b102b.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bahlolab/nf-pacbio-amplicon-analysis/r_v0.1/2019-01-29-dacbc381-f6a81dfb/
recipe: https://datasets.datalad.org/shub/bahlolab/nf-pacbio-amplicon-analysis/r_v0.1/2019-01-29-dacbc381-f6a81dfb/Singularity
collection: bahlolab/nf-pacbio-amplicon-analysis
---

# bahlolab/nf-pacbio-amplicon-analysis:r_v0.1

```bash
$ singularity pull shub://bahlolab/nf-pacbio-amplicon-analysis:r_v0.1
```

## Singularity Recipe

```singularity
Bootstrap:docker
From: rocker/verse:3.5.0

%labels
  AUTHOR Jacob Munro

%post
    R --slave -e "install.packages(c('plotly', 'crosstalk'), repos='https://cloud.r-project.org')"

%environment
    export R_ENVIRON=""
    export R_PROFILE=""
    export R_PROFILE_USER=""
```

## Collection

 - Name: [bahlolab/nf-pacbio-amplicon-analysis](https://github.com/bahlolab/nf-pacbio-amplicon-analysis)
 - License: None

