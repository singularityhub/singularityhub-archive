---
id: 11656
name: "TomHarrop/variant-utils"
branch: "master"
tag: "deepvariant_0.9.0"
commit: "a18dfc3d78096b264a6f4691effbc00d810c0b77"
version: "bee1b957307388a0e93c1d8f474c6695a2a58096b7a2cae3ed6f93ef8c4cc3df"
build_date: "2020-08-29T06:32:56.277Z"
size_mb: 1681.10546875
size: 1762766848
sif: "https://datasets.datalad.org/shub/TomHarrop/variant-utils/deepvariant_0.9.0/2020-08-29-a18dfc3d-bee1b957/bee1b957307388a0e93c1d8f474c6695a2a58096b7a2cae3ed6f93ef8c4cc3df.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/variant-utils/deepvariant_0.9.0/2020-08-29-a18dfc3d-bee1b957/
recipe: https://datasets.datalad.org/shub/TomHarrop/variant-utils/deepvariant_0.9.0/2020-08-29-a18dfc3d-bee1b957/Singularity
collection: TomHarrop/variant-utils
---

# TomHarrop/variant-utils:deepvariant_0.9.0

```bash
$ singularity pull shub://TomHarrop/variant-utils:deepvariant_0.9.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
Registry: gcr.io
From: deepvariant-docker/deepvariant:0.9.0

%environment
    export PATH="${PATH}:/opt/deepvariant/bin"

%runscript
    exec /opt/deepvariant/bin/run_deepvariant "$@"
```

## Collection

 - Name: [TomHarrop/variant-utils](https://github.com/TomHarrop/variant-utils)
 - License: None

