---
id: 3802
name: "Deadlyelder/Singularity-hello-world"
branch: "master"
tag: "latest"
commit: "78dee2c971145f14b58e6a3e04e4434b6998c61c"
version: "36d8e6760606fbe3be5bfb27ba29eb3f"
build_date: "2020-04-21T19:58:40.048Z"
size_mb: 203
size: 67432479
sif: "https://datasets.datalad.org/shub/Deadlyelder/Singularity-hello-world/latest/2020-04-21-78dee2c9-36d8e676/36d8e6760606fbe3be5bfb27ba29eb3f.simg"
url: https://datasets.datalad.org/shub/Deadlyelder/Singularity-hello-world/latest/2020-04-21-78dee2c9-36d8e676/
recipe: https://datasets.datalad.org/shub/Deadlyelder/Singularity-hello-world/latest/2020-04-21-78dee2c9-36d8e676/Singularity
collection: Deadlyelder/Singularity-hello-world
---

# Deadlyelder/Singularity-hello-world:latest

```bash
$ singularity pull shub://Deadlyelder/Singularity-hello-world:latest
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

