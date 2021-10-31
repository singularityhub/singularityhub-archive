---
id: 10398
name: "TomHarrop/funannotate-singularity"
branch: "master"
tag: "repeatmasker_4.0.9p2"
commit: "04f73656bdbbaca3cddffc9d49d8205d462862b3"
version: "92c38e0aa6283404d184c553b35bbbeae2cb711da2b1d9514b157716b6aa0dc9"
build_date: "2021-01-18T00:25:23.383Z"
size_mb: 866.6015625
size: 908697600
sif: "https://datasets.datalad.org/shub/TomHarrop/funannotate-singularity/repeatmasker_4.0.9p2/2021-01-18-04f73656-92c38e0a/92c38e0aa6283404d184c553b35bbbeae2cb711da2b1d9514b157716b6aa0dc9.sif"
url: https://datasets.datalad.org/shub/TomHarrop/funannotate-singularity/repeatmasker_4.0.9p2/2021-01-18-04f73656-92c38e0a/
recipe: https://datasets.datalad.org/shub/TomHarrop/funannotate-singularity/repeatmasker_4.0.9p2/2021-01-18-04f73656-92c38e0a/Singularity
collection: TomHarrop/funannotate-singularity
---

# TomHarrop/funannotate-singularity:repeatmasker_4.0.9p2

```bash
$ singularity pull shub://TomHarrop/funannotate-singularity:repeatmasker_4.0.9p2
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tomharrop/funannotate-singularity:repeatmasker-4.0.9p2

%runscript
    exec /usr/local/RepeatMasker/RepeatMasker "$@"

%post
    export DEBIAN_FRONTEND=noninteractive

    # configure repeatmasker
    apt-get install -y expect
    (
        cd /usr/local/RepeatMasker || exit 1
        expect -c "
        spawn perl configure
        expect \"Enter path *\"
        send \"\n\"
        expect \"Enter Selection*\"
        send \"5\n\"
        interact"
    )
```

## Collection

 - Name: [TomHarrop/funannotate-singularity](https://github.com/TomHarrop/funannotate-singularity)
 - License: [MIT License](https://api.github.com/licenses/mit)

