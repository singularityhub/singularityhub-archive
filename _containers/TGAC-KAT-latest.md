---
id: 5047
name: "TGAC/KAT"
branch: "develop"
tag: "latest"
commit: "f2a9789a743cb66ef767a1e0b6f81e4e0e79495d"
version: "81dd908b7e933a67b1a2a673e22c6c91"
build_date: "2021-02-20T14:26:30.303Z"
size_mb: 1014
size: 352874527
sif: "https://datasets.datalad.org/shub/TGAC/KAT/latest/2021-02-20-f2a9789a-81dd908b/81dd908b7e933a67b1a2a673e22c6c91.simg"
url: https://datasets.datalad.org/shub/TGAC/KAT/latest/2021-02-20-f2a9789a-81dd908b/
recipe: https://datasets.datalad.org/shub/TGAC/KAT/latest/2021-02-20-f2a9789a-81dd908b/Singularity
collection: TGAC/KAT
---

# TGAC/KAT:latest

```bash
$ singularity pull shub://TGAC/KAT:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: maplesond/kat:2.4.2

%post

	# Test
	kat --version
```

## Collection

 - Name: [TGAC/KAT](https://github.com/TGAC/KAT)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

