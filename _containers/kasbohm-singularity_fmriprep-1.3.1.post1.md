---
id: 7768
name: "kasbohm/singularity_fmriprep"
branch: "master"
tag: "1.3.1.post1"
commit: "0b20ae46887fb598253bca485dc0bd527b8db00f"
version: "0297fed22d734ef59b9e2a7b7de1decf"
build_date: "2019-03-14T11:48:13.687Z"
size_mb: 12186
size: 4810731551
sif: "https://datasets.datalad.org/shub/kasbohm/singularity_fmriprep/1.3.1.post1/2019-03-14-0b20ae46-0297fed2/0297fed22d734ef59b9e2a7b7de1decf.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/kasbohm/singularity_fmriprep/1.3.1.post1/2019-03-14-0b20ae46-0297fed2/
recipe: https://datasets.datalad.org/shub/kasbohm/singularity_fmriprep/1.3.1.post1/2019-03-14-0b20ae46-0297fed2/Singularity
collection: kasbohm/singularity_fmriprep
---

# kasbohm/singularity_fmriprep:1.3.1.post1

```bash
$ singularity pull shub://kasbohm/singularity_fmriprep:1.3.1.post1
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: poldracklab/fmriprep:1.3.1.post1
IncludeCmd: yes

%post
    mkdir -p /tsd /usit /cluster /scratch
#
```

## Collection

 - Name: [kasbohm/singularity_fmriprep](https://github.com/kasbohm/singularity_fmriprep)
 - License: None

