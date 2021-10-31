---
id: 3803
name: "Deadlyelder/Singularity-hello-world"
branch: "master"
tag: "build"
commit: "ec7d83c90ce7967b141ddf8d960f735e053eac6a"
version: "766d99393275d236d34c24a3b7b4fcc6"
build_date: "2018-08-01T12:24:35.822Z"
size_mb: 203
size: 67432479
sif: "https://datasets.datalad.org/shub/Deadlyelder/Singularity-hello-world/build/2018-08-01-ec7d83c9-766d9939/766d99393275d236d34c24a3b7b4fcc6.simg"
url: https://datasets.datalad.org/shub/Deadlyelder/Singularity-hello-world/build/2018-08-01-ec7d83c9-766d9939/
recipe: https://datasets.datalad.org/shub/Deadlyelder/Singularity-hello-world/build/2018-08-01-ec7d83c9-766d9939/Singularity
collection: Deadlyelder/Singularity-hello-world
---

# Deadlyelder/Singularity-hello-world:build

```bash
$ singularity pull shub://Deadlyelder/Singularity-hello-world:build
```

## Singularity Recipe

```singularity
BootStrap: debootstrap
OSVersion: stable
MirrorURL: http://ftp.us.debian.org/debian/

%runscript
    echo "This is what happens when you run the container..."

%post
    echo "Hello from inside the container"
    apt-get update
    apt-get -y install vim
    apt-get clean
```

## Collection

 - Name: [Deadlyelder/Singularity-hello-world](https://github.com/Deadlyelder/Singularity-hello-world)
 - License: [MIT License](https://api.github.com/licenses/mit)

