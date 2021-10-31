---
id: 8607
name: "rwblair/singularity_fmriprep"
branch: "master"
tag: "1.3.2"
commit: "a8cdfe5e5f0a5d2eb0188e9fc04858043ca5d9dc"
version: "452b0deda080071e952c34fa336f77b6"
build_date: "2019-04-24T02:14:23.783Z"
size_mb: 12187
size: 4811120671
sif: "https://datasets.datalad.org/shub/rwblair/singularity_fmriprep/1.3.2/2019-04-24-a8cdfe5e-452b0ded/452b0deda080071e952c34fa336f77b6.simg"
url: https://datasets.datalad.org/shub/rwblair/singularity_fmriprep/1.3.2/2019-04-24-a8cdfe5e-452b0ded/
recipe: https://datasets.datalad.org/shub/rwblair/singularity_fmriprep/1.3.2/2019-04-24-a8cdfe5e-452b0ded/Singularity
collection: rwblair/singularity_fmriprep
---

# rwblair/singularity_fmriprep:1.3.2

```bash
$ singularity pull shub://rwblair/singularity_fmriprep:1.3.2
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

 - Name: [rwblair/singularity_fmriprep](https://github.com/rwblair/singularity_fmriprep)
 - License: None

