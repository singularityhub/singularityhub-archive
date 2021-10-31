---
id: 2284
name: "ucr-singularity/faces-project"
branch: "master"
tag: "latest"
commit: "6cfc2b51712650500e04ffa5a4ddc7671a5a50c4"
version: "21cb2a4e5d9c006eaa09ec36e79182c7"
build_date: "2018-03-26T10:14:22.830Z"
size_mb: 8812
size: 4185964575
sif: "https://datasets.datalad.org/shub/ucr-singularity/faces-project/latest/2018-03-26-6cfc2b51-21cb2a4e/21cb2a4e5d9c006eaa09ec36e79182c7.simg"
url: https://datasets.datalad.org/shub/ucr-singularity/faces-project/latest/2018-03-26-6cfc2b51-21cb2a4e/
recipe: https://datasets.datalad.org/shub/ucr-singularity/faces-project/latest/2018-03-26-6cfc2b51-21cb2a4e/Singularity
collection: ucr-singularity/faces-project
---

# ucr-singularity/faces-project:latest

```bash
$ singularity pull shub://ucr-singularity/faces-project:latest
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: ucr-singularity/ml-software

%post

    # Dependencies for the Faces project.
    # Example:
    # TensorFlow
    # pip install --no-cache-dir tensorflow-gpu==1.5.0
```

## Collection

 - Name: [ucr-singularity/faces-project](https://github.com/ucr-singularity/faces-project)
 - License: None

