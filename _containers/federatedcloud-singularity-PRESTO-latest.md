---
id: 13526
name: "federatedcloud/singularity-PRESTO"
branch: "master"
tag: "latest"
commit: "7507790f93b9d6bea32a1ad3660e35f698fbbba9"
version: "aec4800c74a6e744152de63450e74a5ba4b6d7a242d61ed329f7280d278d34d5"
build_date: "2020-11-07T20:45:03.143Z"
size_mb: 1177.51171875
size: 1234710528
sif: "https://datasets.datalad.org/shub/federatedcloud/singularity-PRESTO/latest/2020-11-07-7507790f-aec4800c/aec4800c74a6e744152de63450e74a5ba4b6d7a242d61ed329f7280d278d34d5.sif"
url: https://datasets.datalad.org/shub/federatedcloud/singularity-PRESTO/latest/2020-11-07-7507790f-aec4800c/
recipe: https://datasets.datalad.org/shub/federatedcloud/singularity-PRESTO/latest/2020-11-07-7507790f-aec4800c/Singularity
collection: federatedcloud/singularity-PRESTO
---

# federatedcloud/singularity-PRESTO:latest

```bash
$ singularity pull shub://federatedcloud/singularity-PRESTO:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: cornellcac/presto:latest



%labels
    Author pete@CAC
    Version v0.0.1

%help
    This is a base container for PRESTO and dependencies intended for use on XSEDE
    resources.  Original Dockerfile from: https://github.com/federatedcloud/docker-PRESTO
```

## Collection

 - Name: [federatedcloud/singularity-PRESTO](https://github.com/federatedcloud/singularity-PRESTO)
 - License: [BSD 3-Clause "New" or "Revised" License](https://api.github.com/licenses/bsd-3-clause)

