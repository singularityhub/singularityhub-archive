---
id: 3017
name: "singularityhub/rar"
branch: "master"
tag: "latest"
commit: "3990b8ce92000673631d793875d494f688be0eae"
version: "5a8cb417f6d742faf0d03f9b5d532df8"
build_date: "2020-05-24T05:54:44.987Z"
size_mb: 136
size: 67948575
sif: "https://datasets.datalad.org/shub/singularityhub/rar/latest/2020-05-24-3990b8ce-5a8cb417/5a8cb417f6d742faf0d03f9b5d532df8.simg"
url: https://datasets.datalad.org/shub/singularityhub/rar/latest/2020-05-24-3990b8ce-5a8cb417/
recipe: https://datasets.datalad.org/shub/singularityhub/rar/latest/2020-05-24-3990b8ce-5a8cb417/Singularity
collection: singularityhub/rar
---

# singularityhub/rar:latest

```bash
$ singularity pull shub://singularityhub/rar:latest
```

## Singularity Recipe

```singularity
From: ubuntu:16.04
Bootstrap: docker

# rar/unrar tool for working with rar archives
# sudo singularity build rar.simg Singularity

%apprun create
    exec rar a "$@"

%apphelp create
    Create a rar archive.
        singularity run --app create rar.simg folder.rar folder/

    See "man rar" for other options.


%apphelp extract
    Extract a rar archive.
        singularity run --app extract rar.simg folder.rar folder/

    See "man unrar" for other options.

%apprun extract
    exec unrar x "$@"

%help
    This container provides the rar and unrar utilities. Running the container
    as is is akin to running the rar utility on Linux:
       ./rar.simg --help

    If you want to create or extract an archive, you can also use one of the apps
    provided:

        singularity apps rar.simg
          create
          extract

    Or ask for help for usage for one:

        $ singularity help --app create rar.simg 
        $ singularity help --app extract rar.simg 
   
%runscript
    exec rar "$@"

%post
    apt-get update && apt-get install -y rar unrar
```

## Collection

 - Name: [singularityhub/rar](https://github.com/singularityhub/rar)
 - License: [BSD 3-Clause "New" or "Revised" License](https://api.github.com/licenses/bsd-3-clause)

