---
id: 11675
name: "nathanjent/i_will_do_science_to_it"
branch: "master"
tag: "latest"
commit: "3b3f5e93e7257816766da55e93344789e38319fe"
version: "749bbda570d784c98a89e5e6c2f10bfa"
build_date: "2019-11-21T13:36:55.661Z"
size_mb: 96.0
size: 46661663
sif: "https://datasets.datalad.org/shub/nathanjent/i_will_do_science_to_it/latest/2019-11-21-3b3f5e93-749bbda5/749bbda570d784c98a89e5e6c2f10bfa.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/nathanjent/i_will_do_science_to_it/latest/2019-11-21-3b3f5e93-749bbda5/
recipe: https://datasets.datalad.org/shub/nathanjent/i_will_do_science_to_it/latest/2019-11-21-3b3f5e93-749bbda5/Singularity
collection: nathanjent/i_will_do_science_to_it
---

# nathanjent/i_will_do_science_to_it:latest

```bash
$ singularity pull shub://nathanjent/i_will_do_science_to_it:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:ubuntu:18.04

%labels
MAINTAINER Vanessasaur
SPECIES Dinosaur

%environment
RAWR_BASE=/code
export RAWR_BASE

%runscript
echo "This gets run when you run the image!" 
exec /bin/bash /code/rawr.sh "$@"  

%post  
echo "This section happens once after bootstrap to build the image."  
mkdir -p /code  
apt-get update
apt-get install -y tidy
echo "RoooAAAAR" >> /code/rawr.sh
chmod u+x /code/rawr.sh
```

## Collection

 - Name: [nathanjent/i_will_do_science_to_it](https://github.com/nathanjent/i_will_do_science_to_it)
 - License: [MIT License](https://api.github.com/licenses/mit)

