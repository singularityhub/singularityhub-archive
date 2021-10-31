---
id: 14849
name: "TomHarrop/assemblers"
branch: "master"
tag: "trinity_2.11.0"
commit: "30eb3fcb686473e1768edcaa7b653ef174d6da86"
version: "2dedef370260ece15edec3221e0cd6f9e28b9c6d4502fb0bf9931962d9c09dba"
build_date: "2020-11-09T20:57:20.241Z"
size_mb: 2415.1171875
size: 2532433920
sif: "https://datasets.datalad.org/shub/TomHarrop/assemblers/trinity_2.11.0/2020-11-09-30eb3fcb-2dedef37/2dedef370260ece15edec3221e0cd6f9e28b9c6d4502fb0bf9931962d9c09dba.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/assemblers/trinity_2.11.0/2020-11-09-30eb3fcb-2dedef37/
recipe: https://datasets.datalad.org/shub/TomHarrop/assemblers/trinity_2.11.0/2020-11-09-30eb3fcb-2dedef37/Singularity
collection: TomHarrop/assemblers
---

# TomHarrop/assemblers:trinity_2.11.0

```bash
$ singularity pull shub://TomHarrop/assemblers:trinity_2.11.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: trinityrnaseq/trinityrnaseq:2.11.0

%help
    Container for Trinity 2.11.0
    https://github.com/trinityrnaseq/trinityrnaseq


%labels
    VERSION "Trinity 2.11.0"

%environment
    export PATH="${PATH}:/usr/local/bin/trinityrnaseq:/usr/local/bin/trinityrnaseq/util:/usr/local/bin/trinityrnaseq/util/support_scripts:/usr/local/bin/trinityrnaseq/util/misc"

%post
    # replace Node_alignment.py with the patched version 
    # cd /usr/local/bin/trinityrnaseq/Analysis/SuperTranscripts/pylib || exit 1
    # rm -f Node_alignment.py
    # wget https://raw.githubusercontent.com/trinityrnaseq/trinityrnaseq/1a471bda7cd025090c151c7a01c145acbdf179c6/Analysis/SuperTranscripts/pylib/Node_alignment.py
    # chmod 755 Node_alignment.py

%runscript
    exec /usr/local/bin/trinityrnaseq/Trinity "$@"
```

## Collection

 - Name: [TomHarrop/assemblers](https://github.com/TomHarrop/assemblers)
 - License: None

