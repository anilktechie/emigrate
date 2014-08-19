emigrate
========

Emigrate is Python 2.x console application to migration MySQL database store on Python migration scenarios.

### Quick start and example

1. Create migration in ".migrations" directory of your product

```py
class Migration_20140212165434(Migration):
    def up(self):
        # Step 1. Create table (we may also check database exist to provide idempotency)
        query = "CREATE TABLE `example` ..."
        self.execute(query)
        # Step 2. You may execute insert SQL
        query = "INSERT ..."
        self.execute(query)
        # Step 3. Another way to populate database
        self.insert("")

    def down(self):
        # Step 1. Drop table
        query = "DROP TABLE `example`"
        self.execute(query)
```

2. Create ".emigrate" this is settings

```
[core]
db.type=mysql
db.schema="smm"
db.host=...
db.port=...
db.username=...
db.password=...
```

3. Emigrate your migrations to "up".
```bash
$ emig up
```

4. ...

5. PROFIT
