---
id: 2309
name: "researchapps/sherlock"
branch: "master"
tag: "pvacseq"
commit: "84011d3a460036dcb42ee9b64fd3e7da6f0bbc95"
version: "19b2b7c17a1fe40e5af74e1eb5df8eab"
build_date: "2021-03-15T23:49:44.707Z"
size_mb: 4437
size: 1814982687
sif: "https://datasets.datalad.org/shub/researchapps/sherlock/pvacseq/2021-03-15-84011d3a-19b2b7c1/19b2b7c17a1fe40e5af74e1eb5df8eab.simg"
url: https://datasets.datalad.org/shub/researchapps/sherlock/pvacseq/2021-03-15-84011d3a-19b2b7c1/
recipe: https://datasets.datalad.org/shub/researchapps/sherlock/pvacseq/2021-03-15-84011d3a-19b2b7c1/Singularity
collection: researchapps/sherlock
---

# researchapps/sherlock:pvacseq

```bash
$ singularity pull shub://researchapps/sherlock:pvacseq
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: vanessa/sherlock:pvacseq

# sudo singularity build pvacseq Singularity.pvacseq

%environment
    PATH=/opt/conda/bin:$PATH
    export PATH
    
%runscript
    exec scif "$@"
```

## Collection

 - Name: [researchapps/sherlock](https://github.com/researchapps/sherlock)
 - License: [MIT License](https://api.github.com/licenses/mit)

