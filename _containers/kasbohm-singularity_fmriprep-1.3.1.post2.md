---
id: 7772
name: "kasbohm/singularity_fmriprep"
branch: "master"
tag: "1.3.1.post2"
commit: "8a1b4ed21608eacb1b78b0360ec13d5ce8bc0e5d"
version: "e82fcaee670d57ea7d294977fb94ee9e"
build_date: "2019-03-14T12:02:08.505Z"
size_mb: 12187
size: 4811112479
sif: "https://datasets.datalad.org/shub/kasbohm/singularity_fmriprep/1.3.1.post2/2019-03-14-8a1b4ed2-e82fcaee/e82fcaee670d57ea7d294977fb94ee9e.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/kasbohm/singularity_fmriprep/1.3.1.post2/2019-03-14-8a1b4ed2-e82fcaee/
recipe: https://datasets.datalad.org/shub/kasbohm/singularity_fmriprep/1.3.1.post2/2019-03-14-8a1b4ed2-e82fcaee/Singularity
collection: kasbohm/singularity_fmriprep
---

# kasbohm/singularity_fmriprep:1.3.1.post2

```bash
$ singularity pull shub://kasbohm/singularity_fmriprep:1.3.1.post2
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

 - Name: [kasbohm/singularity_fmriprep](https://github.com/kasbohm/singularity_fmriprep)
 - License: None

