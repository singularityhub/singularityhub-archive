---
id: 9629
name: "Clinical-Genomics/BALSAMIC"
branch: "develop"
tag: "miniconda3_4_6_14"
commit: "acb0ef612d4359b7797087471a9259490e3db58b"
version: "e21e45dd896d7646e4bc0f1497335b79"
build_date: "2019-11-11T10:09:26.224Z"
size_mb: 483
size: 180473887
sif: "https://datasets.datalad.org/shub/Clinical-Genomics/BALSAMIC/miniconda3_4_6_14/2019-11-11-acb0ef61-e21e45dd/e21e45dd896d7646e4bc0f1497335b79.simg"
url: https://datasets.datalad.org/shub/Clinical-Genomics/BALSAMIC/miniconda3_4_6_14/2019-11-11-acb0ef61-e21e45dd/
recipe: https://datasets.datalad.org/shub/Clinical-Genomics/BALSAMIC/miniconda3_4_6_14/2019-11-11-acb0ef61-e21e45dd/Singularity
collection: Clinical-Genomics/BALSAMIC
---

# Clinical-Genomics/BALSAMIC:miniconda3_4_6_14

```bash
$ singularity pull shub://Clinical-Genomics/BALSAMIC:miniconda3_4_6_14
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3:4.6.14

%help
    This container is the latest tested conda version for Clinical Genomics

%labels
    Maintainer Hassan Foroughi Asl <hassan.foroughi@scilifelab.se>
    Conda version 4.6.14 container 
    Version 0.0.1

%runscript
  exec "$@"
```

## Collection

 - Name: [Clinical-Genomics/BALSAMIC](https://github.com/Clinical-Genomics/BALSAMIC)
 - License: [MIT License](https://api.github.com/licenses/mit)

