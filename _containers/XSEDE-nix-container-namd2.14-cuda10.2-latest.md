---
id: 15899
name: "XSEDE/nix-container-namd2.14-cuda10.2"
branch: "main"
tag: "latest"
commit: "45b9a0fc983ea226e0ec87a667a2ef0e6c16be7f"
version: "d924d1a8146518e2b7e0d22c6f72af187935cdbe914324d5ec9f57710a4d5f70"
build_date: "2021-04-14T19:51:48.662Z"
size_mb: 2650.50390625
size: 2779254784
sif: "https://datasets.datalad.org/shub/XSEDE/nix-container-namd2.14-cuda10.2/latest/2021-04-14-45b9a0fc-d924d1a8/d924d1a8146518e2b7e0d22c6f72af187935cdbe914324d5ec9f57710a4d5f70.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/XSEDE/nix-container-namd2.14-cuda10.2/latest/2021-04-14-45b9a0fc-d924d1a8/
recipe: https://datasets.datalad.org/shub/XSEDE/nix-container-namd2.14-cuda10.2/latest/2021-04-14-45b9a0fc-d924d1a8/Singularity
collection: XSEDE/nix-container-namd2.14-cuda10.2
---

# XSEDE/nix-container-namd2.14-cuda10.2:latest

```bash
$ singularity pull shub://XSEDE/nix-container-namd2.14-cuda10.2:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: xsede/nix-namd2-14-cuda10.2:latest
# The above container does not yet exist in a public repo - for now
#  replace this with a reference to the one built locally from the included
#  Dockerfile.

%runscript
#Simply pass any commandline arguments to namd2
/usr/bin/namd2 $@

%help
 This contains NAMD 2.14 built with CUDA 10.2.89 support.
```

## Collection

 - Name: [XSEDE/nix-container-namd2.14-cuda10.2](https://github.com/XSEDE/nix-container-namd2.14-cuda10.2)
 - License: [MIT License](https://api.github.com/licenses/mit)

