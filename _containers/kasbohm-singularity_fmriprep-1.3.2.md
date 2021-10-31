---
id: 8070
name: "kasbohm/singularity_fmriprep"
branch: "master"
tag: "1.3.2"
commit: "a8cdfe5e5f0a5d2eb0188e9fc04858043ca5d9dc"
version: "d0a2ee08d9687e785fe2307a5b9272dc"
build_date: "2019-07-25T17:55:32.008Z"
size_mb: 12187
size: 4811120671
sif: "https://datasets.datalad.org/shub/kasbohm/singularity_fmriprep/1.3.2/2019-07-25-a8cdfe5e-d0a2ee08/d0a2ee08d9687e785fe2307a5b9272dc.simg"
url: https://datasets.datalad.org/shub/kasbohm/singularity_fmriprep/1.3.2/2019-07-25-a8cdfe5e-d0a2ee08/
recipe: https://datasets.datalad.org/shub/kasbohm/singularity_fmriprep/1.3.2/2019-07-25-a8cdfe5e-d0a2ee08/Singularity
collection: kasbohm/singularity_fmriprep
---

# kasbohm/singularity_fmriprep:1.3.2

```bash
$ singularity pull shub://kasbohm/singularity_fmriprep:1.3.2
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: poldracklab/fmriprep:1.3.2
IncludeCmd: yes

%post
    mkdir -p /tsd /usit /cluster /scratch
```

## Collection

 - Name: [kasbohm/singularity_fmriprep](https://github.com/kasbohm/singularity_fmriprep)
 - License: None

