---
id: 12064
name: "TomHarrop/assemblers"
branch: "master"
tag: "trinity_2.9.0"
commit: "1b8257344059ccd2791a2f0d66804d2ae291e94a"
version: "b59a17a37699de32c5f0641a5633141637a6a681587805001db0ba4567fb58ee"
build_date: "2020-08-16T22:25:11.720Z"
size_mb: 3165.6796875
size: 3319455744
sif: "https://datasets.datalad.org/shub/TomHarrop/assemblers/trinity_2.9.0/2020-08-16-1b825734-b59a17a3/b59a17a37699de32c5f0641a5633141637a6a681587805001db0ba4567fb58ee.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/assemblers/trinity_2.9.0/2020-08-16-1b825734-b59a17a3/
recipe: https://datasets.datalad.org/shub/TomHarrop/assemblers/trinity_2.9.0/2020-08-16-1b825734-b59a17a3/Singularity
collection: TomHarrop/assemblers
---

# TomHarrop/assemblers:trinity_2.9.0

```bash
$ singularity pull shub://TomHarrop/assemblers:trinity_2.9.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: trinityrnaseq/trinityrnaseq:2.9.0

%help

    Container for Trinity 2.9.0 (patched)
    https://github.com/trinityrnaseq/trinityrnaseq/issues/782#issuecomment-577207574
    https://github.com/trinityrnaseq/trinityrnaseq


%labels

    VERSION "Trinity 2.9.0-patched"

%post
    

%environment


%runscript

    exec /usr/local/bin/trinityrnaseq/Trinity "$@"
```

## Collection

 - Name: [TomHarrop/assemblers](https://github.com/TomHarrop/assemblers)
 - License: None

