---
id: 13598
name: "federatedcloud/pulsar-pipeline-container"
branch: "master"
tag: "latest"
commit: "a5a2fa4c21ea0b882a5fb0eb1d99527170805c41"
version: "1e669128561ce12b65ac6c6174c7d9328d6630c750c6599d7c2a88cfa59487cb"
build_date: "2021-02-15T06:21:48.872Z"
size_mb: 1237.1328125
size: 1297227776
sif: "https://datasets.datalad.org/shub/federatedcloud/pulsar-pipeline-container/latest/2021-02-15-a5a2fa4c-1e669128/1e669128561ce12b65ac6c6174c7d9328d6630c750c6599d7c2a88cfa59487cb.sif"
url: https://datasets.datalad.org/shub/federatedcloud/pulsar-pipeline-container/latest/2021-02-15-a5a2fa4c-1e669128/
recipe: https://datasets.datalad.org/shub/federatedcloud/pulsar-pipeline-container/latest/2021-02-15-a5a2fa4c-1e669128/Singularity
collection: federatedcloud/pulsar-pipeline-container
---

# federatedcloud/pulsar-pipeline-container:latest

```bash
$ singularity pull shub://federatedcloud/pulsar-pipeline-container:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: cornellcac/pulsar-pipeline:latest



%labels
    Author pete@CAC
    Version v0.0.1

%help
    This is a container for pulsar searching intended for use on XSEDE
    resources.  It uses the PRESTO base image, and adds a few dependencies
    and codebases.  Also see https://github.com/federatedcloud/pulsar-pipeline-container
```

## Collection

 - Name: [federatedcloud/pulsar-pipeline-container](https://github.com/federatedcloud/pulsar-pipeline-container)
 - License: [BSD 3-Clause "New" or "Revised" License](https://api.github.com/licenses/bsd-3-clause)

