---
id: 13551
name: "CATG-UMAG/tandem-substitution-simulation"
branch: "master"
tag: "latest"
commit: "68e74d984630950247fef4fb2653dda8b7ab352a"
version: "56316a4f7097ed6c3d62da74b173c204"
build_date: "2021-04-19T07:58:51.366Z"
size_mb: 499.0
size: 212033567
sif: "https://datasets.datalad.org/shub/CATG-UMAG/tandem-substitution-simulation/latest/2021-04-19-68e74d98-56316a4f/56316a4f7097ed6c3d62da74b173c204.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/CATG-UMAG/tandem-substitution-simulation/latest/2021-04-19-68e74d98-56316a4f/
recipe: https://datasets.datalad.org/shub/CATG-UMAG/tandem-substitution-simulation/latest/2021-04-19-68e74d98-56316a4f/Singularity
collection: CATG-UMAG/tandem-substitution-simulation
---

# CATG-UMAG/tandem-substitution-simulation:latest

```bash
$ singularity pull shub://CATG-UMAG/tandem-substitution-simulation:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: python:3.8-slim-buster

%labels
    Author Diego Alvarez S. (dialvarezs@gmail.com)
    MyLabel tandem-simulation
    Description to use with https://github.com/CATG-UMAG/tandem-substitution-simulation

%post
    apt update && apt upgrade -y
    pip3 install -r https://raw.githubusercontent.com/CATG-UMAG/tandem-substitution-simulation/master/env/requirements.txt
```

## Collection

 - Name: [CATG-UMAG/tandem-substitution-simulation](https://github.com/CATG-UMAG/tandem-substitution-simulation)
 - License: [MIT License](https://api.github.com/licenses/mit)

