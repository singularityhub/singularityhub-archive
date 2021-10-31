# Singularity Hub UI

This is a small search interface to allow you to search over the image names and Singularity recipe
contents of the [Singularity Hub archive](https://singularity-hub.org) that is [hosted on datalad](http://datasets.datalad.org/?dir=/shub).

![assets/img/logo.png](assets/img/logo.png)

## Generation

To first retrieve all the Singularity recipe files, we run this preprocessing script
from the root here:

```bash
$ pip install -r requirements.txt
$ python scripts/get-recipes.py
```

Since recipes are relatively small, it is reasonable to store them here for search, organized by
the name and tags. Note that after generation, there is [one file](_containers/feilong-neurodebian_singularity-beaver_2019-01-14.md)
that needed a raw/endraw added.

Since we can't generate in one go, we have to generate incrementally. So you should do:

```bash
./build.sh
bundle exec jekyll serve --incremental
```

And then pull the gh-pages branch from the _site root, or just push to the main branch
to run the CI to do this update.
