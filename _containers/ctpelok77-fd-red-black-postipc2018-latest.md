---
id: 13386
name: "ctpelok77/fd-red-black-postipc2018"
branch: "master"
tag: "latest"
commit: "2e3a9e74356587113af9d550e155a0dbbdf80cd1"
version: "e34291a2a04d7deadf2529189d30b41306612f3f44fb9f49e172e23c2363900f"
build_date: "2021-04-06T11:55:11.543Z"
size_mb: 37.5859375
size: 39411712
sif: "https://datasets.datalad.org/shub/ctpelok77/fd-red-black-postipc2018/latest/2021-04-06-2e3a9e74-e34291a2/e34291a2a04d7deadf2529189d30b41306612f3f44fb9f49e172e23c2363900f.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/ctpelok77/fd-red-black-postipc2018/latest/2021-04-06-2e3a9e74-e34291a2/
recipe: https://datasets.datalad.org/shub/ctpelok77/fd-red-black-postipc2018/latest/2021-04-06-2e3a9e74-e34291a2/Singularity
collection: ctpelok77/fd-red-black-postipc2018
---

# ctpelok77/fd-red-black-postipc2018:latest

```bash
$ singularity pull shub://ctpelok77/fd-red-black-postipc2018:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ctpelok77/cerberus:latest

%setup
    # Just for diagnosis purposes
    hostname -f > $SINGULARITY_ROOTFS/etc/build_host
%runscript
    # This will be called whenever the Singularity container is invoked
    python3 /workspace/cerberus/fast-downward.py $@

%post

## Cerberus planner
%labels
Name        Cerberus
Description Red-black planning heuristic with native support for conditional effects, h^2 mutexes, novelty heuristic for search guidance. Post-IPC 2018 version.
Authors     Michael Katz <michael.katz1@ibm.com>
```

## Collection

 - Name: [ctpelok77/fd-red-black-postipc2018](https://github.com/ctpelok77/fd-red-black-postipc2018)
 - License: None

