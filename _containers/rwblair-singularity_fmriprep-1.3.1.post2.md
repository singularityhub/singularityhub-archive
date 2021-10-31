---
id: 8608
name: "rwblair/singularity_fmriprep"
branch: "master"
tag: "1.3.1.post2"
commit: "8a1b4ed21608eacb1b78b0360ec13d5ce8bc0e5d"
version: "d3631e12ae84ea975260d8c2b3732560"
build_date: "2019-04-24T02:14:23.777Z"
size_mb: 12187
size: 4811112479
sif: "https://datasets.datalad.org/shub/rwblair/singularity_fmriprep/1.3.1.post2/2019-04-24-8a1b4ed2-d3631e12/d3631e12ae84ea975260d8c2b3732560.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/rwblair/singularity_fmriprep/1.3.1.post2/2019-04-24-8a1b4ed2-d3631e12/
recipe: https://datasets.datalad.org/shub/rwblair/singularity_fmriprep/1.3.1.post2/2019-04-24-8a1b4ed2-d3631e12/Singularity
collection: rwblair/singularity_fmriprep
---

# rwblair/singularity_fmriprep:1.3.1.post2

```bash
$ singularity pull shub://rwblair/singularity_fmriprep:1.3.1.post2
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: poldracklab/fmriprep:1.3.1.post2
IncludeCmd: yes

%post
    mkdir -p /tsd /usit /cluster /scratch
#
```

## Collection

 - Name: [rwblair/singularity_fmriprep](https://github.com/rwblair/singularity_fmriprep)
 - License: None

