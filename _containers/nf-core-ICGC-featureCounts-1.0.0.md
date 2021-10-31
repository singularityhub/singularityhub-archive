---
id: 3647
name: "nf-core/ICGC-featureCounts"
branch: "master"
tag: "1.0.0"
commit: "a3130716746c53df6ac8faf1dedef0b79cfb8848"
version: "566db4d761042fb908ef6e5186bdcfd1"
build_date: "2018-08-08T03:56:31.952Z"
size_mb: 1917
size: 638320671
sif: "https://datasets.datalad.org/shub/nf-core/ICGC-featureCounts/1.0.0/2018-08-08-a3130716-566db4d7/566db4d761042fb908ef6e5186bdcfd1.simg"
url: https://datasets.datalad.org/shub/nf-core/ICGC-featureCounts/1.0.0/2018-08-08-a3130716-566db4d7/
recipe: https://datasets.datalad.org/shub/nf-core/ICGC-featureCounts/1.0.0/2018-08-08-a3130716-566db4d7/Singularity
collection: nf-core/ICGC-featureCounts
---

# nf-core/ICGC-featureCounts:1.0.0

```bash
$ singularity pull shub://nf-core/ICGC-featureCounts:1.0.0
```

## Singularity Recipe

```singularity
From:nfcore/base
Bootstrap:docker

%labels
    MAINTAINER Alexander Peltzer <alexander.peltzer@qbic.uni-tuebingen.de>
    DESCRIPTION Singularity image containing all requirements for ICGC-FeatureCounts pipeline
    VERSION 1.0.0

%files
    environment.yml /

%post
    /opt/conda/bin/conda env update -n root -f /environment.yml
    /opt/conda/bin/conda clean -a
```

## Collection

 - Name: [nf-core/ICGC-featureCounts](https://github.com/nf-core/ICGC-featureCounts)
 - License: [MIT License](https://api.github.com/licenses/mit)

