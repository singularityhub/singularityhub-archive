---
id: 8609
name: "rwblair/singularity_fmriprep"
branch: "master"
tag: "1.3.1.post1"
commit: "0b20ae46887fb598253bca485dc0bd527b8db00f"
version: "6e324dc9f6973099537d0092834ac9ea"
build_date: "2019-04-24T02:14:23.792Z"
size_mb: 12186
size: 4810731551
sif: "https://datasets.datalad.org/shub/rwblair/singularity_fmriprep/1.3.1.post1/2019-04-24-0b20ae46-6e324dc9/6e324dc9f6973099537d0092834ac9ea.simg"
url: https://datasets.datalad.org/shub/rwblair/singularity_fmriprep/1.3.1.post1/2019-04-24-0b20ae46-6e324dc9/
recipe: https://datasets.datalad.org/shub/rwblair/singularity_fmriprep/1.3.1.post1/2019-04-24-0b20ae46-6e324dc9/Singularity
collection: rwblair/singularity_fmriprep
---

# rwblair/singularity_fmriprep:1.3.1.post1

```bash
$ singularity pull shub://rwblair/singularity_fmriprep:1.3.1.post1
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

 - Name: [rwblair/singularity_fmriprep](https://github.com/rwblair/singularity_fmriprep)
 - License: None

