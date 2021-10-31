---
id: 12066
name: "TomHarrop/assemblers"
branch: "master"
tag: "trinity_2.9.0-patched"
commit: "470b5c7c18c8d6a157377e40ef308ec37d415a8e"
version: "1e0dc8ca5e7a0af8ae78b16d5e0448f25046cbae7c4931a21f20b6534cb2d99a"
build_date: "2020-01-22T23:15:05.529Z"
size_mb: 3165.6796875
size: 3319455744
sif: "https://datasets.datalad.org/shub/TomHarrop/assemblers/trinity_2.9.0-patched/2020-01-22-470b5c7c-1e0dc8ca/1e0dc8ca5e7a0af8ae78b16d5e0448f25046cbae7c4931a21f20b6534cb2d99a.sif"
url: https://datasets.datalad.org/shub/TomHarrop/assemblers/trinity_2.9.0-patched/2020-01-22-470b5c7c-1e0dc8ca/
recipe: https://datasets.datalad.org/shub/TomHarrop/assemblers/trinity_2.9.0-patched/2020-01-22-470b5c7c-1e0dc8ca/Singularity
collection: TomHarrop/assemblers
---

# TomHarrop/assemblers:trinity_2.9.0-patched

```bash
$ singularity pull shub://TomHarrop/assemblers:trinity_2.9.0-patched
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: trinityrnaseq/trinityrnaseq:2.9.0

%help
    Container for Trinity 2.9.0 (patched)
    https://github.com/trinityrnaseq/trinityrnaseq/issues/782#issuecomment-577207574
    https://github.com/trinityrnaseq/trinityrnaseq


%labels
    VERSION "Trinity 2.9.0-patched"

%post    
    # replace Node_alignment.py with the patched version 
    cd /usr/local/bin/trinityrnaseq/Analysis/SuperTranscripts/pylib || exit 1
    rm -f Node_alignment.py
    wget https://raw.githubusercontent.com/trinityrnaseq/trinityrnaseq/devel/Analysis/SuperTranscripts/pylib/Node_alignment.py
    chmod 755 Node_alignment.py

%runscript
    exec /usr/local/bin/trinityrnaseq/Trinity "$@"
```

## Collection

 - Name: [TomHarrop/assemblers](https://github.com/TomHarrop/assemblers)
 - License: None

