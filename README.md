# git-plot
Some tooling to get nice plot based on git stats

## Get source data

### All tags from a repository per tagger name
```bash
git for-each-ref --sort=refname --format '%(refname:short) - %(taggername) - %(creatordate)' refs/tags | grep -v RC
```
