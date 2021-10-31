---
id: 15121
name: "JossWhittle/Opt-ID-Env"
branch: "main"
tag: "env-v3-dev"
commit: "21a7ef128525fec9366577dfe182b85cfb9097d6"
version: "4e7235e1df7ea487d8b802ff1a6dfc7f6d8d107458fc10b27b7ec661b3c6994b"
build_date: "2020-12-14T16:43:40.425Z"
size_mb: 253.5859375
size: 265904128
sif: "https://datasets.datalad.org/shub/JossWhittle/Opt-ID-Env/env-v3-dev/2020-12-14-21a7ef12-4e7235e1/4e7235e1df7ea487d8b802ff1a6dfc7f6d8d107458fc10b27b7ec661b3c6994b.sif"
url: https://datasets.datalad.org/shub/JossWhittle/Opt-ID-Env/env-v3-dev/2020-12-14-21a7ef12-4e7235e1/
recipe: https://datasets.datalad.org/shub/JossWhittle/Opt-ID-Env/env-v3-dev/2020-12-14-21a7ef12-4e7235e1/Singularity
collection: JossWhittle/Opt-ID-Env
---

# JossWhittle/Opt-ID-Env:env-v3-dev

```bash
$ singularity pull shub://JossWhittle/Opt-ID-Env:env-v3-dev
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: josswhittle/opt-id:env-v3-dev

%test
    python --version
    pip --version

%labels
    Owner   Rosalind Franklin Institute
    Author  joss.whittle@rfi.ac.uk
    Version v3.0

%help
    Provides a Singularity Hub image from the Dockerhub image docker://josswhittle/opt-id:env-v3-dev.
```

## Collection

 - Name: [JossWhittle/Opt-ID-Env](https://github.com/JossWhittle/Opt-ID-Env)
 - License: [Apache License 2.0](https://api.github.com/licenses/apache-2.0)

