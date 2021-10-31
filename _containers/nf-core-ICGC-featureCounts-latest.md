---
id: 3641
name: "nf-core/ICGC-featureCounts"
branch: "master"
tag: "latest"
commit: "21438279f482a164902a93a347d7d77bd660164c"
version: "2378e4d376999456f024c0873d132c71"
build_date: "2018-07-24T19:19:06.024Z"
size_mb: 1830
size: 632463391
sif: "https://datasets.datalad.org/shub/nf-core/ICGC-featureCounts/latest/2018-07-24-21438279-2378e4d3/2378e4d376999456f024c0873d132c71.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/nf-core/ICGC-featureCounts/latest/2018-07-24-21438279-2378e4d3/
recipe: https://datasets.datalad.org/shub/nf-core/ICGC-featureCounts/latest/2018-07-24-21438279-2378e4d3/Singularity
collection: nf-core/ICGC-featureCounts
---

# nf-core/ICGC-featureCounts:latest

```bash
$ singularity pull shub://nf-core/ICGC-featureCounts:latest
```

## Singularity Recipe

```singularity
From:nfcore/base
Bootstrap:docker

%labels
    MAINTAINER Alexander Peltzer <alexander.peltzer@qbic.uni-tuebingen.de>
    DESCRIPTION Singularity image containing all requirements for ICGC-FeatureCounts pipeline
    VERSION 1.0.0dev

%files
    environment.yml /

%post
    /opt/conda/bin/conda env update -n root -f /environment.yml
    /opt/conda/bin/conda clean -a
```

## Collection

 - Name: [nf-core/ICGC-featureCounts](https://github.com/nf-core/ICGC-featureCounts)
 - License: [MIT License](https://api.github.com/licenses/mit)

