---
id: 8594
name: "alan0415/singularity_swift"
branch: "master"
tag: "v1"
commit: "623771d691bd24f3f09018831b570851269913c5"
version: "a20980548e45a21432e2f3defee9a123"
build_date: "2019-04-23T20:55:38.837Z"
size_mb: 1671
size: 430342175
sif: "https://datasets.datalad.org/shub/alan0415/singularity_swift/v1/2019-04-23-623771d6-a2098054/a20980548e45a21432e2f3defee9a123.simg"
url: https://datasets.datalad.org/shub/alan0415/singularity_swift/v1/2019-04-23-623771d6-a2098054/
recipe: https://datasets.datalad.org/shub/alan0415/singularity_swift/v1/2019-04-23-623771d6-a2098054/Singularity
collection: alan0415/singularity_swift
---

# alan0415/singularity_swift:v1

```bash
$ singularity pull shub://alan0415/singularity_swift:v1
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From: alan0415/swift:v1

%post  
echo "This section happens once after bootstrap to build the image."
```

## Collection

 - Name: [alan0415/singularity_swift](https://github.com/alan0415/singularity_swift)
 - License: None

