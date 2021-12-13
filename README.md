Jenkins with Secret
===================

An example, how you can store an secet in an environment variable
when starting jenkins via docker.

## System Setup
Add to `/etc/hosts`:
```
127.0.0.1   ci.firmenessen.de
127.0.0.1   ldap.firmenessen.de
```

## Getting started
Move `example.env` to `.env` and change the secret by running `python3 set_password`
Start it up, go to ldap.firmenessen.de, sign in with 
username: `cn=admin,dc=example,dc=org` and the secret from the `.env`
file.

An user is already created: `gerritadmin`. Go to `ci.firmenesse.de` and login 
with `gerritadmin` and the password from the `.env` file

Create a new Child entry