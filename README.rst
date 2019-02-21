Management command to dump Django local db and media for backup purposes (and optionally remove old backup files)

usage: manage.py dump_local_data [-h] [--version] [-v {0,1,2,3}]
                                 [--settings SETTINGS]
                                 [--pythonpath PYTHONPATH] [--traceback]
                                 [--no-color] [--dry-run] [--max-age MAX_AGE]
                                 [--no-gzip] [--legacy]
                                 target

positional arguments:
  target                choices: db, media, all

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  -v {0,1,2,3}, --verbosity {0,1,2,3}
                        Verbosity level; 0=minimal output, 1=normal output,
                        2=verbose output, 3=very verbose output
  --settings SETTINGS   The Python path to a settings module, e.g.
                        "myproject.settings.main". If this isn't provided, the
                        DJANGO_SETTINGS_MODULE environment variable will be
                        used.
  --pythonpath PYTHONPATH
                        A directory to add to the Python path, e.g.
                        "/home/djangoprojects/myproject".
  --traceback           Raise on CommandError exceptions
  --no-color            Don't colorize the command output.
  --dry-run, -d         Dry run (simulation)
  --max-age MAX_AGE, -m MAX_AGE
                        If > 0, remove backup files old "MAX_AGE days" or more
  --no-gzip             Do not compress result
  --legacy              use legacy Postgresql command syntax


Settings
--------

DUMP_LOCAL_DATA_TARGET_FOLDER
  Target folder for backup files
  Defaults to: os.path.join(settings.BASE_DIR, '..', 'dumps', 'localhost')


Sample usage
------------

::

    python manage.py dump_local_data all -m 1 -d

    # pg_dump --dbname=myproject | gzip > "/Users/morlandi/src2/brainstorm/myproject/dumps/localhost/2019-02-21_11.42.36_myproject.sql.gz"
    # tar -C "/Users/morlandi/src2/brainstorm/myproject/public" -zcvf "/Users/morlandi/src2/brainstorm/myproject/dumps/localhost/2019-02-21_11.42.36_myproject.media.tar.gz" "media"
    Removing 2019-02-19_11.42.10_myproject.media.tar.gz [dated:2019-02-19, age=2]
    # rm /Users/morlandi/src2/brainstorm/myproject/dumps/localhost/2019-02-19_11.42.10_myproject.media.tar.gz
    Removing 2019-02-20_11.42.10_myproject.sql.gz [dated:2019-02-20, age=1]
    # rm /Users/morlandi/src2/brainstorm/myproject/dumps/localhost/2019-02-20_11.42.10_myproject.sql.gz
    Removing 2019-02-20_11.42.10_myproject.media.tar.gz [dated:2019-02-20, age=1]
    # rm /Users/morlandi/src2/brainstorm/myproject/dumps/localhost/2019-02-20_11.42.10_myproject.media.tar.gz
    Removing 2019-02-19_11.42.10_myproject.sql.gz [dated:2019-02-19, age=2]
    # rm /Users/morlandi/src2/brainstorm/myproject/dumps/localhost/2019-02-19_11.42.10_myproject.sql.gz
