---
id: 12376
name: "TomHarrop/funannotate-singularity"
branch: "master"
tag: "tetools_1.1"
commit: "bb76746301e841424c8efbec0fab06f0c9f567c0"
version: "7887bd0a6d1891d8014aaed191e5aabc9b536e8fc8b6d7e19bb0aaf6276efb0d"
build_date: "2020-06-17T01:33:01.110Z"
size_mb: 863.78125
size: 905740288
sif: "https://datasets.datalad.org/shub/TomHarrop/funannotate-singularity/tetools_1.1/2020-06-17-bb767463-7887bd0a/7887bd0a6d1891d8014aaed191e5aabc9b536e8fc8b6d7e19bb0aaf6276efb0d.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/funannotate-singularity/tetools_1.1/2020-06-17-bb767463-7887bd0a/
recipe: https://datasets.datalad.org/shub/TomHarrop/funannotate-singularity/tetools_1.1/2020-06-17-bb767463-7887bd0a/Singularity
collection: TomHarrop/funannotate-singularity
---

# TomHarrop/funannotate-singularity:tetools_1.1

```bash
$ singularity pull shub://TomHarrop/funannotate-singularity:tetools_1.1
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: dfam/tetools:1.1

%environment
    export LC_ALL=C
    export PATH="${PATH}:/opt"

%post
    export DEBIAN_FRONTEND=noninteractive
    export LC_ALL=C
    export PATH="${PATH}:/opt"

    # RM is configured for trf to be in /opt/trf
    wget \
        -O /opt/trf \
        http://tandem.bu.edu/trf/downloads/trf409.linux64
    chmod +x /opt/trf

    # allow writing to RM Library dir
    chmod -R 777 /opt/RepeatMasker/Libraries

%runscript
    exec /opt/RepeatMasker/RepeatMasker "$@"
```

## Collection

 - Name: [TomHarrop/funannotate-singularity](https://github.com/TomHarrop/funannotate-singularity)
 - License: [MIT License](https://api.github.com/licenses/mit)

