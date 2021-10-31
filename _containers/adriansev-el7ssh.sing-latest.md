---
id: 13008
name: "adriansev/el7ssh.sing"
branch: "master"
tag: "latest"
commit: "7afd18de19f9f049705cb57775f8824c8ab4af19"
version: "11b4f3e0d0e9e9fb81d7839133a80b40733b24613e3dfb0e75356cef777203d4"
build_date: "2020-05-13T22:16:51.531Z"
size_mb: 72.34375
size: 75857920
sif: "https://datasets.datalad.org/shub/adriansev/el7ssh.sing/latest/2020-05-13-7afd18de-11b4f3e0/11b4f3e0d0e9e9fb81d7839133a80b40733b24613e3dfb0e75356cef777203d4.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/adriansev/el7ssh.sing/latest/2020-05-13-7afd18de-11b4f3e0/
recipe: https://datasets.datalad.org/shub/adriansev/el7ssh.sing/latest/2020-05-13-7afd18de-11b4f3e0/Singularity
collection: adriansev/el7ssh.sing
---

# adriansev/el7ssh.sing:latest

```bash
$ singularity pull shub://adriansev/el7ssh.sing:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: adriansevcenco/el7ssh

%labels
    Author Adrian.Sevcenco@spacescience.ro
    Version 0.0.1
    Description Minimal el7 ssh client


%help
el7 ssh client

%runscript
exec /usr/bin/ssh "${@}"
```

## Collection

 - Name: [adriansev/el7ssh.sing](https://github.com/adriansev/el7ssh.sing)
 - License: None

