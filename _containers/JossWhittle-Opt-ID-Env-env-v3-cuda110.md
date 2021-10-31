---
id: 15123
name: "JossWhittle/Opt-ID-Env"
branch: "main"
tag: "env-v3-cuda110"
commit: "21a7ef128525fec9366577dfe182b85cfb9097d6"
version: "0c862c4493ad0f5594f03631024ce7e5039c5c097879a6d1da38dcdfa8f1af5a"
build_date: "2020-12-14T16:59:53.897Z"
size_mb: 382.41015625
size: 400986112
sif: "https://datasets.datalad.org/shub/JossWhittle/Opt-ID-Env/env-v3-cuda110/2020-12-14-21a7ef12-0c862c44/0c862c4493ad0f5594f03631024ce7e5039c5c097879a6d1da38dcdfa8f1af5a.sif"
url: https://datasets.datalad.org/shub/JossWhittle/Opt-ID-Env/env-v3-cuda110/2020-12-14-21a7ef12-0c862c44/
recipe: https://datasets.datalad.org/shub/JossWhittle/Opt-ID-Env/env-v3-cuda110/2020-12-14-21a7ef12-0c862c44/Singularity
collection: JossWhittle/Opt-ID-Env
---

# JossWhittle/Opt-ID-Env:env-v3-cuda110

```bash
$ singularity pull shub://JossWhittle/Opt-ID-Env:env-v3-cuda110
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: josswhittle/opt-id:env-v3-cuda110

%test
    python --version
    pip --version

%labels
    Owner   Rosalind Franklin Institute
    Author  joss.whittle@rfi.ac.uk
    Version v3.0

%help
    Provides a Singularity Hub image from the Dockerhub image docker://josswhittle/opt-id:env-v3-cuda110.
```

## Collection

 - Name: [JossWhittle/Opt-ID-Env](https://github.com/JossWhittle/Opt-ID-Env)
 - License: [Apache License 2.0](https://api.github.com/licenses/apache-2.0)

