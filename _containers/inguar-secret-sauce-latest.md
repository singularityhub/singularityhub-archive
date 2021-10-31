---
id: 6825
name: "inguar/secret-sauce"
branch: "master"
tag: "latest"
commit: "a672c8f2c5491c4d5c06b1bcb55fa0ebd3a612e8"
version: "a16491ec43a9593b4852dcb4ebe1f89e"
build_date: "2019-06-12T15:53:26.039Z"
size_mb: 869
size: 305500191
sif: "https://datasets.datalad.org/shub/inguar/secret-sauce/latest/2019-06-12-a672c8f2-a16491ec/a16491ec43a9593b4852dcb4ebe1f89e.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/inguar/secret-sauce/latest/2019-06-12-a672c8f2-a16491ec/
recipe: https://datasets.datalad.org/shub/inguar/secret-sauce/latest/2019-06-12-a672c8f2-a16491ec/Singularity
collection: inguar/secret-sauce
---

# inguar/secret-sauce:latest

```bash
$ singularity pull shub://inguar/secret-sauce:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: 525253251/micro

%post
    echo "building things from inside Singularity is tricky..."
    
    # add mount point for Quest's "/projects"
    mkdir /run/user
    mkdir /projects
    chmod g-w,o-w /usr/local/share/zsh/site-functions
    
%environment
    export SHELL=/bin/zsh
    export HOME=`ls -d /home/* | head -n 1`
    export JULIA_PKGDIR=~/.julia

%runscript
    #zsh -c 
    $*

%labels
    Author "Igor Zakhlebin <zahl.igor@gmail.com>"
```

## Collection

 - Name: [inguar/secret-sauce](https://github.com/inguar/secret-sauce)
 - License: None

