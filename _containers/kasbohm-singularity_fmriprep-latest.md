---
id: 7763
name: "kasbohm/singularity_fmriprep"
branch: "master"
tag: "latest"
commit: "7bd45578b89ca551ae348998a7b311b11513d065"
version: "e6f3c126352e8847214f7ed3aa920d65"
build_date: "2019-11-11T16:31:29.270Z"
size_mb: 12187
size: 4811120671
sif: "https://datasets.datalad.org/shub/kasbohm/singularity_fmriprep/latest/2019-11-11-7bd45578-e6f3c126/e6f3c126352e8847214f7ed3aa920d65.simg"
url: https://datasets.datalad.org/shub/kasbohm/singularity_fmriprep/latest/2019-11-11-7bd45578-e6f3c126/
recipe: https://datasets.datalad.org/shub/kasbohm/singularity_fmriprep/latest/2019-11-11-7bd45578-e6f3c126/Singularity
collection: kasbohm/singularity_fmriprep
---

# kasbohm/singularity_fmriprep:latest

```bash
$ singularity pull shub://kasbohm/singularity_fmriprep:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: poldracklab/fmriprep:latest
IncludeCmd: yes

%post
    mkdir -p /tsd /usit /cluster /scratch

# Bump
```

## Collection

 - Name: [kasbohm/singularity_fmriprep](https://github.com/kasbohm/singularity_fmriprep)
 - License: None

