---
id: 8465
name: "rearmstr/singularity_image_recipes"
branch: "master"
tag: "lsstsims"
commit: "08cc5c2bab50c0da462d55b6d7da07eb6d427de3"
version: "8db3057ed6e0370efa9851f4cc9bb6a2"
build_date: "2019-04-17T14:28:05.113Z"
size_mb: 8038
size: 3892252703
sif: "https://datasets.datalad.org/shub/rearmstr/singularity_image_recipes/lsstsims/2019-04-17-08cc5c2b-8db3057e/8db3057ed6e0370efa9851f4cc9bb6a2.simg"
url: https://datasets.datalad.org/shub/rearmstr/singularity_image_recipes/lsstsims/2019-04-17-08cc5c2b-8db3057e/
recipe: https://datasets.datalad.org/shub/rearmstr/singularity_image_recipes/lsstsims/2019-04-17-08cc5c2b-8db3057e/Singularity
collection: rearmstr/singularity_image_recipes
---

# rearmstr/singularity_image_recipes:lsstsims

```bash
$ singularity pull shub://rearmstr/singularity_image_recipes:lsstsims
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: avillarreal/alcf_run2.0i:latest

%environment
   /DC2/ALCF_1.2i/docker_run.sh

%runscript
exec python /DC2/ALCF_1.2i/scripts/run_imsim.py "$@"
```

## Collection

 - Name: [rearmstr/singularity_image_recipes](https://github.com/rearmstr/singularity_image_recipes)
 - License: None

