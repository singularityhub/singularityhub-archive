---
id: 12615
name: "adriansev/el7hep.sing"
branch: "master"
tag: "latest"
commit: "a4128ed0abc533fbcc125ea56150e2e75a47694e"
version: "8b6e05de6e3ecafe3872987e34b3e00b4592aae6ce424e1166bf4f8344feedca"
build_date: "2021-04-05T19:08:03.846Z"
size_mb: 230.44921875
size: 241643520
sif: "https://datasets.datalad.org/shub/adriansev/el7hep.sing/latest/2021-04-05-a4128ed0-8b6e05de/8b6e05de6e3ecafe3872987e34b3e00b4592aae6ce424e1166bf4f8344feedca.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/adriansev/el7hep.sing/latest/2021-04-05-a4128ed0-8b6e05de/
recipe: https://datasets.datalad.org/shub/adriansev/el7hep.sing/latest/2021-04-05-a4128ed0-8b6e05de/Singularity
collection: adriansev/el7hep.sing
---

# adriansev/el7hep.sing:latest

```bash
$ singularity pull shub://adriansev/el7hep.sing:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: adriansevcenco/el7hep

%labels
    Author Adrian.Sevcenco@spacescience.ro
    Version 0.0.1
    Description Minimal el7 + HEP_OSlibs container


%help
Generic HEP oriented container (it includes HEP_OSlibs dependency list)
The default is either run the argument list or just start bash

%runscript
[[ -n "${@}" ]] && exec "${@}" || exec bash
```

## Collection

 - Name: [adriansev/el7hep.sing](https://github.com/adriansev/el7hep.sing)
 - License: None

