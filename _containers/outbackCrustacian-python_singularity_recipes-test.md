---
id: 3789
name: "outbackCrustacian/python_singularity_recipes"
branch: "master"
tag: "test"
commit: "7199e3f03e351d5719828ecfe7b0e88c256e57d5"
version: "e2f36b2a01320c015a970f933aef16fa"
build_date: "2018-07-31T15:32:55.858Z"
size_mb: 774
size: 224743455
sif: "https://datasets.datalad.org/shub/outbackCrustacian/python_singularity_recipes/test/2018-07-31-7199e3f0-e2f36b2a/e2f36b2a01320c015a970f933aef16fa.simg"
url: https://datasets.datalad.org/shub/outbackCrustacian/python_singularity_recipes/test/2018-07-31-7199e3f0-e2f36b2a/
recipe: https://datasets.datalad.org/shub/outbackCrustacian/python_singularity_recipes/test/2018-07-31-7199e3f0-e2f36b2a/Singularity
collection: outbackCrustacian/python_singularity_recipes
---

# outbackCrustacian/python_singularity_recipes:test

```bash
$ singularity pull shub://outbackCrustacian/python_singularity_recipes:test
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: jtchilders/singularity_mpi_test_recipe:latest

%setup
   cp hello.py ${SINGULARITY_ROOTFS}/

%post
   ls
   python hello.py
```

## Collection

 - Name: [outbackCrustacian/python_singularity_recipes](https://github.com/outbackCrustacian/python_singularity_recipes)
 - License: None

