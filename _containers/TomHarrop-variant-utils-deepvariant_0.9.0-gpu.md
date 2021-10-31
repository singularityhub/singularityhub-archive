---
id: 11755
name: "TomHarrop/variant-utils"
branch: "master"
tag: "deepvariant_0.9.0-gpu"
commit: "5f5b18ff949bf741746ec8984783f088b1b089cf"
version: "cb3290434f9bed4c1f5cb9799047c409c48feca22e1d87ddaa5cab5348eb0417"
build_date: "2019-12-04T23:42:02.352Z"
size_mb: 3656.94921875
size: 3834589184
sif: "https://datasets.datalad.org/shub/TomHarrop/variant-utils/deepvariant_0.9.0-gpu/2019-12-04-5f5b18ff-cb329043/cb3290434f9bed4c1f5cb9799047c409c48feca22e1d87ddaa5cab5348eb0417.sif"
url: https://datasets.datalad.org/shub/TomHarrop/variant-utils/deepvariant_0.9.0-gpu/2019-12-04-5f5b18ff-cb329043/
recipe: https://datasets.datalad.org/shub/TomHarrop/variant-utils/deepvariant_0.9.0-gpu/2019-12-04-5f5b18ff-cb329043/Singularity
collection: TomHarrop/variant-utils
---

# TomHarrop/variant-utils:deepvariant_0.9.0-gpu

```bash
$ singularity pull shub://TomHarrop/variant-utils:deepvariant_0.9.0-gpu
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: google/deepvariant:0.9.0-gpu


%post
    apt-get update
    apt-get install -y \
        libopenblas-base

%environment
    export PATH="${PATH}:/opt/deepvariant/bin"

%runscript
    exec /opt/deepvariant/bin/run_deepvariant "$@"
```

## Collection

 - Name: [TomHarrop/variant-utils](https://github.com/TomHarrop/variant-utils)
 - License: None

