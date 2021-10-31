---
id: 15122
name: "JossWhittle/Opt-ID-Env"
branch: "main"
tag: "env-v3-cuda110-dev"
commit: "21a7ef128525fec9366577dfe182b85cfb9097d6"
version: "60d7c4f2689604154b4f3c1a98654c279a6b4db8e9add8936afdf0fe368c0dce"
build_date: "2020-12-14T16:51:44.712Z"
size_mb: 382.41015625
size: 400986112
sif: "https://datasets.datalad.org/shub/JossWhittle/Opt-ID-Env/env-v3-cuda110-dev/2020-12-14-21a7ef12-60d7c4f2/60d7c4f2689604154b4f3c1a98654c279a6b4db8e9add8936afdf0fe368c0dce.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/JossWhittle/Opt-ID-Env/env-v3-cuda110-dev/2020-12-14-21a7ef12-60d7c4f2/
recipe: https://datasets.datalad.org/shub/JossWhittle/Opt-ID-Env/env-v3-cuda110-dev/2020-12-14-21a7ef12-60d7c4f2/Singularity
collection: JossWhittle/Opt-ID-Env
---

# JossWhittle/Opt-ID-Env:env-v3-cuda110-dev

```bash
$ singularity pull shub://JossWhittle/Opt-ID-Env:env-v3-cuda110-dev
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: josswhittle/opt-id:env-v3-cuda110-dev

%test
    python --version
    pip --version

%labels
    Owner   Rosalind Franklin Institute
    Author  joss.whittle@rfi.ac.uk
    Version v3.0

%help
    Provides a Singularity Hub image from the Dockerhub image docker://josswhittle/opt-id:env-v3-cuda110-dev.
```

## Collection

 - Name: [JossWhittle/Opt-ID-Env](https://github.com/JossWhittle/Opt-ID-Env)
 - License: [Apache License 2.0](https://api.github.com/licenses/apache-2.0)

