---
id: 1771
name: "poojabhat1690/slamdunk"
branch: "master"
tag: "latest"
commit: "05a58332f731fb25e8bcee3b88379dc93e38e3ce"
version: "649d8717fee7cdede6856a3f8d32de5d"
build_date: "2019-10-08T17:47:27.941Z"
size_mb: 120
size: 41754655
sif: "https://datasets.datalad.org/shub/poojabhat1690/slamdunk/latest/2019-10-08-05a58332-649d8717/649d8717fee7cdede6856a3f8d32de5d.simg"
url: https://datasets.datalad.org/shub/poojabhat1690/slamdunk/latest/2019-10-08-05a58332-649d8717/
recipe: https://datasets.datalad.org/shub/poojabhat1690/slamdunk/latest/2019-10-08-05a58332-649d8717/Singularity
collection: poojabhat1690/slamdunk
---

# poojabhat1690/slamdunk:latest

```bash
$ singularity pull shub://poojabhat1690/slamdunk:latest
```

## Singularity Recipe

```singularity
bootstrap:docker
From:ubuntu

%post
# Tobias Neumann <tobias.neumann.at@gmail.com>
export SLAMDUNK_VERSION=0.2.3-dev
echo "
export SLAMDUNK_VERSION=0.2.3-dev" >> /environment
```

## Collection

 - Name: [poojabhat1690/slamdunk](https://github.com/poojabhat1690/slamdunk)
 - License: None

