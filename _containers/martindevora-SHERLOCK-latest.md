---
id: 14671
name: "martindevora/SHERLOCK"
branch: "master"
tag: "latest"
commit: "5e7492552cbce29e960684a44fd6ad875c8cf60e"
version: "e4dc79f6e589ee6218b581e6d303e50c"
build_date: "2020-10-19T12:02:33.454Z"
size_mb: 4490.0
size: 2444451871
sif: "https://datasets.datalad.org/shub/martindevora/SHERLOCK/latest/2020-10-19-5e749255-e4dc79f6/e4dc79f6e589ee6218b581e6d303e50c.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/martindevora/SHERLOCK/latest/2020-10-19-5e749255-e4dc79f6/
recipe: https://datasets.datalad.org/shub/martindevora/SHERLOCK/latest/2020-10-19-5e749255-e4dc79f6/Singularity
collection: martindevora/SHERLOCK
---

# martindevora/SHERLOCK:latest

```bash
$ singularity pull shub://martindevora/SHERLOCK:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: sherlockpipe/sherlockpipe:latest
IncludeCmd: yes

%post
    echo "Done!"
```

## Collection

 - Name: [martindevora/SHERLOCK](https://github.com/martindevora/SHERLOCK)
 - License: [MIT License](https://api.github.com/licenses/mit)

