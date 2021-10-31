---
id: 770
name: "narrative/remoll"
branch: "master"
tag: "latest"
commit: "26506f673fccb9e8ce231c72719f17a2f121eb13"
version: "040634919cf0399bc6ff3e015cc26424"
build_date: "2017-11-09T19:27:46.631Z"
size_mb: 4581
size: 2172317727
sif: "https://datasets.datalad.org/shub/narrative/remoll/latest/2017-11-09-26506f67-04063491/040634919cf0399bc6ff3e015cc26424.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/narrative/remoll/latest/2017-11-09-26506f67-04063491/
recipe: https://datasets.datalad.org/shub/narrative/remoll/latest/2017-11-09-26506f67-04063491/Singularity
collection: narrative/remoll
---

# narrative/remoll:latest

```bash
$ singularity pull shub://narrative/remoll:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:estevenson/remoll:latest 

%files

%labels
MAINTAINER Erik Stevenson

%environment

%runscript
exec /entrypoint.sh "$@"

%post
```

## Collection

 - Name: [narrative/remoll](https://github.com/narrative/remoll)
 - License: None

