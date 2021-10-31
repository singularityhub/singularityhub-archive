---
id: 12102
name: "TomHarrop/assemblers"
branch: "master"
tag: "trinity_2.9.1-patched"
commit: "6e1c59fe856c8ac0355bb540f8adbd7852a02866"
version: "5fa33d5d7ba95383d1eb537262f1c0b43f19b3fa8d5efa139b12501cf44b7029"
build_date: "2021-01-03T22:47:27.670Z"
size_mb: 2367.6484375
size: 2482659328
sif: "https://datasets.datalad.org/shub/TomHarrop/assemblers/trinity_2.9.1-patched/2021-01-03-6e1c59fe-5fa33d5d/5fa33d5d7ba95383d1eb537262f1c0b43f19b3fa8d5efa139b12501cf44b7029.sif"
url: https://datasets.datalad.org/shub/TomHarrop/assemblers/trinity_2.9.1-patched/2021-01-03-6e1c59fe-5fa33d5d/
recipe: https://datasets.datalad.org/shub/TomHarrop/assemblers/trinity_2.9.1-patched/2021-01-03-6e1c59fe-5fa33d5d/Singularity
collection: TomHarrop/assemblers
---

# TomHarrop/assemblers:trinity_2.9.1-patched

```bash
$ singularity pull shub://TomHarrop/assemblers:trinity_2.9.1-patched
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: trinityrnaseq/trinityrnaseq:2.9.1

%help
    Container for Trinity 2.9.1 
    https://github.com/trinityrnaseq/trinityrnaseq


%labels
    VERSION "Trinity 2.9.1"

%environment
    export PATH="${PATH}:/usr/local/bin/trinityrnaseq:/usr/local/bin/trinityrnaseq/util:/usr/local/bin/trinityrnaseq/util/support_scripts:/usr/local/bin/trinityrnaseq/util/misc"

%post
    # replace Node_alignment.py with the patched version 
    cd /usr/local/bin/trinityrnaseq/Analysis/SuperTranscripts/pylib || exit 1
    rm -f Node_alignment.py
    wget https://raw.githubusercontent.com/trinityrnaseq/trinityrnaseq/1a471bda7cd025090c151c7a01c145acbdf179c6/Analysis/SuperTranscripts/pylib/Node_alignment.py
    chmod 755 Node_alignment.py

%runscript
    exec /usr/local/bin/trinityrnaseq/Trinity "$@"
```

## Collection

 - Name: [TomHarrop/assemblers](https://github.com/TomHarrop/assemblers)
 - License: None

