---
id: 8856
name: "kasbohm/bidscoin"
branch: "master"
tag: "latest"
commit: "72f0592743848846c680ba86f677411a19b86bcd"
version: "f5506eaccbc51b1e6c5715437430f1ea"
build_date: "2019-05-06T15:37:43.876Z"
size_mb: 421
size: 168898591
sif: "https://datasets.datalad.org/shub/kasbohm/bidscoin/latest/2019-05-06-72f05927-f5506eac/f5506eaccbc51b1e6c5715437430f1ea.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/kasbohm/bidscoin/latest/2019-05-06-72f05927-f5506eac/
recipe: https://datasets.datalad.org/shub/kasbohm/bidscoin/latest/2019-05-06-72f05927-f5506eac/Singularity
collection: kasbohm/bidscoin
---

# kasbohm/bidscoin:latest

```bash
$ singularity pull shub://kasbohm/bidscoin:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
FROM: kasbohm/bidscoin:latest

%post
    mkdir /tsd /cluster /scratch /usit
```

## Collection

 - Name: [kasbohm/bidscoin](https://github.com/kasbohm/bidscoin)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

