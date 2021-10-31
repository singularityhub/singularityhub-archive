---
id: 14776
name: "JossWhittle/Opt-ID-Env"
branch: "main"
tag: "env-v3"
commit: "21a7ef128525fec9366577dfe182b85cfb9097d6"
version: "a1c24632a1b6756b2a3ca6fd5a246b761f4e1ccd876f33a679d2814338d7b5d2"
build_date: "2020-12-14T16:37:45.452Z"
size_mb: 253.5859375
size: 265904128
sif: "https://datasets.datalad.org/shub/JossWhittle/Opt-ID-Env/env-v3/2020-12-14-21a7ef12-a1c24632/a1c24632a1b6756b2a3ca6fd5a246b761f4e1ccd876f33a679d2814338d7b5d2.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/JossWhittle/Opt-ID-Env/env-v3/2020-12-14-21a7ef12-a1c24632/
recipe: https://datasets.datalad.org/shub/JossWhittle/Opt-ID-Env/env-v3/2020-12-14-21a7ef12-a1c24632/Singularity
collection: JossWhittle/Opt-ID-Env
---

# JossWhittle/Opt-ID-Env:env-v3

```bash
$ singularity pull shub://JossWhittle/Opt-ID-Env:env-v3
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: josswhittle/opt-id:env-v3

%test
    python --version
    pip --version

%labels
    Owner   Rosalind Franklin Institute
    Author  joss.whittle@rfi.ac.uk
    Version v3.0

%help
    Provides a Singularity Hub image from the Dockerhub image docker://josswhittle/opt-id:env-v3.
```

## Collection

 - Name: [JossWhittle/Opt-ID-Env](https://github.com/JossWhittle/Opt-ID-Env)
 - License: [Apache License 2.0](https://api.github.com/licenses/apache-2.0)

