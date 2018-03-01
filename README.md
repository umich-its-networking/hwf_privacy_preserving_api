# hwf_privacy_preserving_api

## Dev Environment

```
virtualenv -p python3 venv
source ./venv/bin/activate
pip install -r requirements.txt
```

## Running

```
export FLASK_APP=api.py
flask run
```

Once `FLASK_APP` is defined in a shell session, the `export` step
may be skipped for subsequent runs.
