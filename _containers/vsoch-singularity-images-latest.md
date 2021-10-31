---
id: 2688
name: "vsoch/singularity-images"
branch: "master"
tag: "latest"
commit: "130504089d5b2b44e2788992d0de75b625da6796"
version: "84a023b73eaadd39255186b5bdeb08f8"
build_date: "2021-04-14T16:14:49.724Z"
size_mb: 96.0
size: 37142559
sif: "https://datasets.datalad.org/shub/vsoch/singularity-images/latest/2021-04-14-13050408-84a023b7/84a023b73eaadd39255186b5bdeb08f8.sif"
url: https://datasets.datalad.org/shub/vsoch/singularity-images/latest/2021-04-14-13050408-84a023b7/
recipe: https://datasets.datalad.org/shub/vsoch/singularity-images/latest/2021-04-14-13050408-84a023b7/Singularity
collection: vsoch/singularity-images
---

# vsoch/singularity-images:latest

```bash
$ singularity pull shub://vsoch/singularity-images:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:ubuntu:16.04

%post

    echo "The sun is shining, the weather is sweeeet..."

%runscript

    exec echo "You say please, but all I see is pizza.."
```

## Collection

 - Name: [vsoch/singularity-images](https://github.com/vsoch/singularity-images)
 - License: None

