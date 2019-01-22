# Quip Scripts

## Setup

Install python3 and pipenv

```
pipenv sync
```

Remember to export the personal API token as environment variables
`QUIP_TOKEN` before executing any script blow.

## Export document with conversations

First copy the document id from the URL, such as `LeSAAAqaCfc`.

```
pipenv run python export.py LeSAAAqaCfc | tee /tmp/quip.html
```
