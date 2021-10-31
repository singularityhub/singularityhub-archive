---
id: 6984
name: "connor-lab/singularity-recipes"
branch: "master"
tag: "mash"
commit: "5e322d4c80acb21db9d53649a55a0349c4378009"
version: "0d98f382abeda2adb4b9f8ed07ada9fb"
build_date: "2019-02-07T15:45:22.842Z"
size_mb: 103
size: 37777439
sif: "https://datasets.datalad.org/shub/connor-lab/singularity-recipes/mash/2019-02-07-5e322d4c-0d98f382/0d98f382abeda2adb4b9f8ed07ada9fb.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/connor-lab/singularity-recipes/mash/2019-02-07-5e322d4c-0d98f382/
recipe: https://datasets.datalad.org/shub/connor-lab/singularity-recipes/mash/2019-02-07-5e322d4c-0d98f382/Singularity
collection: connor-lab/singularity-recipes
---

# connor-lab/singularity-recipes:mash

```bash
$ singularity pull shub://connor-lab/singularity-recipes:mash
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: alpine:3.8


%post
    apk update
    apk upgrade
    apk add bash curl gcc gcompat
   
    curl -fSSL 'https://github.com/marbl/Mash/releases/download/v2.1/mash-Linux64-v2.1.tar' | tar -x -C /usr/local/bin
    find /usr/local/bin/mash-Linux* -name 'mash' -exec ln -s {} /usr/local/bin \;

%labels
    Maintainer m-bull
    Version mash-2.1
```

## Collection

 - Name: [connor-lab/singularity-recipes](https://github.com/connor-lab/singularity-recipes)
 - License: None

