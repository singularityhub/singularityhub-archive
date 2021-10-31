---
id: 1446
name: "whit2333/bubble_chamber"
branch: "master"
tag: "latest"
commit: "0e6da3ed764fee433dc192f6fb74c422f73ae3c7"
version: "404e0e3879cac4333299d39ae626b932"
build_date: "2018-02-17T22:08:50.986Z"
size_mb: 3356
size: 1263124511
sif: "https://datasets.datalad.org/shub/whit2333/bubble_chamber/latest/2018-02-17-0e6da3ed-404e0e38/404e0e3879cac4333299d39ae626b932.simg"
url: https://datasets.datalad.org/shub/whit2333/bubble_chamber/latest/2018-02-17-0e6da3ed-404e0e38/
recipe: https://datasets.datalad.org/shub/whit2333/bubble_chamber/latest/2018-02-17-0e6da3ed-404e0e38/Singularity
collection: whit2333/bubble_chamber
---

# whit2333/bubble_chamber:latest

```bash
$ singularity pull shub://whit2333/bubble_chamber:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: docker://whit2333/bubble_sim:latest


%runscript
  #echo "This is what happens when you run the container..."
  derp=
  if [ -p /dev/stdin ]; then
    # If we want to read the input line by line
    while IFS= read line; do
      #echo "Line: ${line}"
      if [ -z ${derp} ]; then
        derp="${line}"
      else 
        derp="${derp}\n${line}"
      fi
    done
  fi
  /bin/bash <<EOF
  source /usr/local/bin/geant4.sh
  echo -e ${derp} | bubble_chamber $@
EOF
  #exec /usr/local/bin/run_bubble_sim "$@"


%post
  echo "Hello from inside the container"


%help
  Help me. I'm in the container.


%labels
  Maintainer "Whitney Armstrong"
  Version v1.0
```

## Collection

 - Name: [whit2333/bubble_chamber](https://github.com/whit2333/bubble_chamber)
 - License: None

