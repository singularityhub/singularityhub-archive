---
id: 9361
name: "klabhub/singularity"
branch: "master"
tag: "fmriprep.1.4.1rc1"
commit: "50d990950d53ced4aa3836602f7371d8bdbdaca0"
version: "e4113782df144d5e682a13ebecb19c6d"
build_date: "2019-09-30T18:29:59.920Z"
size_mb: 12142
size: 4780552223
sif: "https://datasets.datalad.org/shub/klabhub/singularity/fmriprep.1.4.1rc1/2019-09-30-50d99095-e4113782/e4113782df144d5e682a13ebecb19c6d.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/klabhub/singularity/fmriprep.1.4.1rc1/2019-09-30-50d99095-e4113782/
recipe: https://datasets.datalad.org/shub/klabhub/singularity/fmriprep.1.4.1rc1/2019-09-30-50d99095-e4113782/Singularity
collection: klabhub/singularity
---

# klabhub/singularity:fmriprep.1.4.1rc1

```bash
$ singularity pull shub://klabhub/singularity:fmriprep.1.4.1rc1
```

## Singularity Recipe

```singularity
#
Bootstrap: docker
From: poldracklab/fmriprep:1.4.1rc1

%post


%environment
export LANG="en_US.UTF-8"
export LC_ALL="en_US.UTF-8"
```

## Collection

 - Name: [klabhub/singularity](https://github.com/klabhub/singularity)
 - License: None

