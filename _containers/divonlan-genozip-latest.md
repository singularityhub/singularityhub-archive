---
id: 12565
name: "divonlan/genozip"
branch: "master"
tag: "latest"
commit: "f45684e44175c685dfb89c9beb202d3e0901de95"
version: "cd4ba27811a6c26b92d32cd2bba83ba7"
build_date: "2020-04-03T00:14:28.692Z"
size_mb: 70.0
size: 25853983
sif: "https://datasets.datalad.org/shub/divonlan/genozip/latest/2020-04-03-f45684e4-cd4ba278/cd4ba27811a6c26b92d32cd2bba83ba7.sif"
url: https://datasets.datalad.org/shub/divonlan/genozip/latest/2020-04-03-f45684e4-cd4ba278/
recipe: https://datasets.datalad.org/shub/divonlan/genozip/latest/2020-04-03-f45684e4-cd4ba278/Singularity
collection: divonlan/genozip
---

# divonlan/genozip:latest

```bash
$ singularity pull shub://divonlan/genozip:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:ubuntu

%labels
    Maintainer divonlan

%help
Help me. I'm in the container.

%environment
    PATH=/code:${PATH}
    export PATH

%post
    #echo "Installing genozip into container..."
    
%runscript
    exec /code/genozip "$@"

# apps

%apprun genozip
    exec /code/genozip "$@"

%apprun genounzip
    exec /code/genounzip "$@"

%apprun genocat
    exec /code/genocat "$@"

%apprun genols
    exec /code/genols "$@"

%apphelp genozip
    This is the help for genozip app.

%apphelp genounzip
    This is the help for genounzip app.

%apphelp genocat
    This is the help for genocat app.

%apphelp genols
    This is the help for genols app.
```

## Collection

 - Name: [divonlan/genozip](https://github.com/divonlan/genozip)
 - License: [Other](None)

