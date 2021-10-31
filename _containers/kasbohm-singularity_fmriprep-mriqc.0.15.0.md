---
id: 8648
name: "kasbohm/singularity_fmriprep"
branch: "master"
tag: "mriqc.0.15.0"
commit: "a158d22902867004ff348fdc784e1b2f64ad7138"
version: "44a13123cfbcac30ccf462c9703bae9b"
build_date: "2019-04-25T15:46:04.940Z"
size_mb: 7631
size: 2961776671
sif: "https://datasets.datalad.org/shub/kasbohm/singularity_fmriprep/mriqc.0.15.0/2019-04-25-a158d229-44a13123/44a13123cfbcac30ccf462c9703bae9b.simg"
url: https://datasets.datalad.org/shub/kasbohm/singularity_fmriprep/mriqc.0.15.0/2019-04-25-a158d229-44a13123/
recipe: https://datasets.datalad.org/shub/kasbohm/singularity_fmriprep/mriqc.0.15.0/2019-04-25-a158d229-44a13123/Singularity
collection: kasbohm/singularity_fmriprep
---

# kasbohm/singularity_fmriprep:mriqc.0.15.0

```bash
$ singularity pull shub://kasbohm/singularity_fmriprep:mriqc.0.15.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
FROM: poldracklab/mriqc:0.15.0

%post
    apt-get update && apt-get -y purge libgsl2 && apt-get -y  install libgsl2
    mkdir /tsd /cluster /scratch /usit
```

## Collection

 - Name: [kasbohm/singularity_fmriprep](https://github.com/kasbohm/singularity_fmriprep)
 - License: None

