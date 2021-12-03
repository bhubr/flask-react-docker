# Flask - MySQL - React - Docker Compose

It's been a while since I practiced Docker and Compose&hellip; Just practicing!

The app is a simple "todo app", consisting of:

* A Python/Flask backend,
* A MySQL database where the backend stores its data,
* A React app

## Issues

* `/docker-entrypoint-initdb.d` containing `schema.sql`, but still no table created &rarr; had to `rm -rf` the `mysql-data` folder, mapped to `/var/lib/mysql`, which had been created **before** we actually put the schema in the right place.
* Flask app attempting to connect to the `db` service before it's ready &rarr; <https://docs.docker.com/compose/startup-order/> (wait for the quick'n'dirty solution based on [https://github.com/vishnubob/wait-for-it](wait-for-it.sh))
* Flask up and running, but not accessible from host &rarr; comment from `xeonman9000` on [this answer](https://stackoverflow.com/a/39647200/1534675)
* `command` in Compose config (`flask run`) overriding `CMD` in `Dockerfile`&hellip; use `flask run --host=0.0.0.0` (but issuing `wait-for-it` causes `standard_init_linux.go:228: exec user process caused: exec format error`)