---
id: 8944
name: "kasbohm/singularity_smriprep"
branch: "master"
tag: "latest"
commit: "82e4f82dad0d3c69d8f4a39db9244043b31d7320"
version: "e369de1a1cd5abbf7c5c1e1e48fdfd63"
build_date: "2019-05-08T15:10:10.810Z"
size_mb: 11783
size: 4558282783
sif: "https://datasets.datalad.org/shub/kasbohm/singularity_smriprep/latest/2019-05-08-82e4f82d-e369de1a/e369de1a1cd5abbf7c5c1e1e48fdfd63.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/kasbohm/singularity_smriprep/latest/2019-05-08-82e4f82d-e369de1a/
recipe: https://datasets.datalad.org/shub/kasbohm/singularity_smriprep/latest/2019-05-08-82e4f82d-e369de1a/Singularity
collection: kasbohm/singularity_smriprep
---

# kasbohm/singularity_smriprep:latest

```bash
$ singularity pull shub://kasbohm/singularity_smriprep:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: poldracklab/smriprep:latest
IncludeCmd: yes

%post
    mkdir -p /tsd /usit /cluster /scratch
```

## Collection

 - Name: [kasbohm/singularity_smriprep](https://github.com/kasbohm/singularity_smriprep)
 - License: [MIT License](https://api.github.com/licenses/mit)

