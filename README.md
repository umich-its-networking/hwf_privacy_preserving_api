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

## Vagrant
Clone Repo

```
cd Vagrant
vagrant up
vagrant ssh
```
This will start a local Ubuntu instance, configure it and provision it with the code

## AWS
Clone Repo

```
cd aws
run-ansible.sh
```
Set up your variables in run-ansible.sh and build-ec2.yml first, but this will create and configure an EC2 instance

## Postman

The API can be tested and experiments can be run on it using
[Postman](https://www.getpostman.com).  

Start Postman and import the
`hwf_privacy_preserving_api.postman_collection.json` collection file from
this repo.  The collection includes queries for the API's two entry points,
one for the `GET` method and one for `OPTIONS`.