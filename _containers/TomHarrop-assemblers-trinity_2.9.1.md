---
id: 12069
name: "TomHarrop/assemblers"
branch: "master"
tag: "trinity_2.9.1"
commit: "416dc940afae223066ae889ba54552564867cf27"
version: "99914684036c1fcdc93080ffc2782cbf4f2ccc64314dcd51da5c7cde03b163be"
build_date: "2020-11-04T20:17:35.395Z"
size_mb: 2367.6484375
size: 2482659328
sif: "https://datasets.datalad.org/shub/TomHarrop/assemblers/trinity_2.9.1/2020-11-04-416dc940-99914684/99914684036c1fcdc93080ffc2782cbf4f2ccc64314dcd51da5c7cde03b163be.sif"
url: https://datasets.datalad.org/shub/TomHarrop/assemblers/trinity_2.9.1/2020-11-04-416dc940-99914684/
recipe: https://datasets.datalad.org/shub/TomHarrop/assemblers/trinity_2.9.1/2020-11-04-416dc940-99914684/Singularity
collection: TomHarrop/assemblers
---

# TomHarrop/assemblers:trinity_2.9.1

```bash
$ singularity pull shub://TomHarrop/assemblers:trinity_2.9.1
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

%runscript
    exec /usr/local/bin/trinityrnaseq/Trinity "$@"
```

## Collection

 - Name: [TomHarrop/assemblers](https://github.com/TomHarrop/assemblers)
 - License: None

