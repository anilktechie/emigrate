emigrate
========

Emigrate is Python application for create and manage database migration (now support only MySQL).

### Quick start

1. Initialize migration system

    ```bash
    $ python -m emigrate init
    ```

2. Creating new migration in ".migration" directory:

    ```bash
    $ python -m emigrate create
    ```

3. Change migration source code

    ```py
    class Migration_20140212165434(Migration):
        """ Create `users` tables and insert admin account
        """

        def up(self):
            """ Update

            - Create table `users`
            - Create table `user_pendings`

            """
            query = "CREATE TABLE `users` ..."
            self.execute(query)

            query = "CREATE TABLE `user_pending` ..."
            self.execute(query)


        def down(self):
            """ Revert

            - Delete table `users`
            - Delete table `user_pending`

            """
            query = "DROP TABLE `users`"
            self.execute(query)

            query = "DROP TABLE `user_pending`"
            self.execute(query)

    ```

4. Setup environment in "emigrate.xml"

    ```xml
    <?xml version="1.0" encoding="utf-8" ?>

    <emigrate version="0.5">
        <connection name="default">
            <option name="driver" value="mysql" />
            <option name="schema" value="smm" />
            <option name="host" value="127.0.0.1" />
            <option name="port" value="3333" />
            <option name="username" value="root" />
            <option name="password" value="******" />
        </connection>
    </emigrate>
    ```

5. Migration command: "status", "up" or "down".

    ```bash
    $ python -m emigrate status
    ```

# Isolation

All operation working in autocommit mode by default and you should create transaction scope
by hand for working inside transaction.

You may understand that create transaction start in separate connection.
