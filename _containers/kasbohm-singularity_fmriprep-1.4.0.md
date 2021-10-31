---
id: 9109
name: "kasbohm/singularity_fmriprep"
branch: "master"
tag: "1.4.0"
commit: "51c9ad48208ebba7e429900aa3972c786e9f79c9"
version: "577cb0926d855dee47fa095c13a95a69"
build_date: "2019-07-26T20:23:30.812Z"
size_mb: 12142
size: 4780552223
sif: "https://datasets.datalad.org/shub/kasbohm/singularity_fmriprep/1.4.0/2019-07-26-51c9ad48-577cb092/577cb0926d855dee47fa095c13a95a69.simg"
url: https://datasets.datalad.org/shub/kasbohm/singularity_fmriprep/1.4.0/2019-07-26-51c9ad48-577cb092/
recipe: https://datasets.datalad.org/shub/kasbohm/singularity_fmriprep/1.4.0/2019-07-26-51c9ad48-577cb092/Singularity
collection: kasbohm/singularity_fmriprep
---

# kasbohm/singularity_fmriprep:1.4.0

```bash
$ singularity pull shub://kasbohm/singularity_fmriprep:1.4.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: poldracklab/fmriprep:1.4.0
IncludeCmd: yes

%post
    mkdir -p /tsd /usit /cluster /scratch
```

## Collection

 - Name: [kasbohm/singularity_fmriprep](https://github.com/kasbohm/singularity_fmriprep)
 - License: None

