---
id: 11859
name: "matthew-kusz/singularity-hello-world"
branch: "master"
tag: "latest"
commit: "140b00306327c908a6cc412fb52bc214d5615291"
version: "cb67e805908cc09d981b62b58b79e7b9"
build_date: "2020-01-27T18:45:57.061Z"
size_mb: 158.0
size: 65302559
sif: "https://datasets.datalad.org/shub/matthew-kusz/singularity-hello-world/latest/2020-01-27-140b0030-cb67e805/cb67e805908cc09d981b62b58b79e7b9.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/matthew-kusz/singularity-hello-world/latest/2020-01-27-140b0030-cb67e805/
recipe: https://datasets.datalad.org/shub/matthew-kusz/singularity-hello-world/latest/2020-01-27-140b0030-cb67e805/Singularity
collection: matthew-kusz/singularity-hello-world
---

# matthew-kusz/singularity-hello-world:latest

```bash
$ singularity pull shub://matthew-kusz/singularity-hello-world:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:ubuntu:18.04

%runscript
echo "This gets run when you run the image!"
exec /bin/bash /code/hi_there.sh "$@"

%post  
echo "This section happens once after bootstrap to build the image."
echo "You can use this section to install things."
mkdir -p /code
apt-get update -y
apt-get install -y vim
apt-get clean
echo 'echo 'Hi there'' >> /code/hi_there.sh
chmod u+x /code/hi_there.sh
```

## Collection

 - Name: [matthew-kusz/singularity-hello-world](https://github.com/matthew-kusz/singularity-hello-world)
 - License: None

