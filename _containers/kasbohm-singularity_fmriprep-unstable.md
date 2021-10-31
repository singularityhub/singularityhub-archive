---
id: 8943
name: "kasbohm/singularity_fmriprep"
branch: "master"
tag: "unstable"
commit: "b9f1a6ddf3040c47bf59f0019a22d39f0b38251e"
version: "b4390b39ad1d1287108127c0e7463757"
build_date: "2019-05-08T15:10:09.592Z"
size_mb: 12141
size: 4780351519
sif: "https://datasets.datalad.org/shub/kasbohm/singularity_fmriprep/unstable/2019-05-08-b9f1a6dd-b4390b39/b4390b39ad1d1287108127c0e7463757.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/kasbohm/singularity_fmriprep/unstable/2019-05-08-b9f1a6dd-b4390b39/
recipe: https://datasets.datalad.org/shub/kasbohm/singularity_fmriprep/unstable/2019-05-08-b9f1a6dd-b4390b39/Singularity
collection: kasbohm/singularity_fmriprep
---

# kasbohm/singularity_fmriprep:unstable

```bash
$ singularity pull shub://kasbohm/singularity_fmriprep:unstable
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: poldracklab/fmriprep:unstable
IncludeCmd: yes

%post
    mkdir -p /tsd /usit /cluster /scratch
```

## Collection

 - Name: [kasbohm/singularity_fmriprep](https://github.com/kasbohm/singularity_fmriprep)
 - License: None

