+-----------------------+-----------------------+-----------------------+
| Environment           | CI Status             | Website               |
+=======================+=======================+=======================+
| Production            | |pipeline status|     | `ejplatform.org <http |
|                       |                       | s://ejplatform.org>`_ |
|                       |                       | _                     |
+-----------------------+-----------------------+-----------------------+
| Development           | |pipeline status|     | `dev.ejplatform.org < |
|                       |                       | http://dev.ejplatform |
|                       |                       | .org>`__              |
+-----------------------+-----------------------+-----------------------+


===========
EJ Platform
===========

Getting started
===============

Local development (virtualenv)
------------------------------

First install virtualenvwrapper in your machine (``sudo apt-get install virtualenvwrapper`` on
Debian based distributions). Clone this repo and create a virtual environment using
Python 3.6+::

    $ git clone http://github.com/ejplatform/ej-server/
    $ mkvirtualenv ej -p /usr/bin/python3

Now, go into the repository and install the dependencies::

    $ cd ej-server
    $ pip install -r etc/requirements/develop.txt

Grab a cup of coffee while it downloads and install all dependencies.

The next step is to initialize the database. EJ uses Invoke_ to manage tasks.
Invoke allow us to execute a sequence of tasks very easily. The command bellow
will update a few volatile dependencies, run all migrations and populate the
database with fake data for local development::

    $ inv update-deps db db-assets db-fake

This creates a few conversations with comments and votes + several users and
a admin:admin <admin@admin.com> user. Use invoke to start the dev server::

    $ inv run


.. _Invoke: http://www.pyinvoke.org/

Tests are executed with Pytest_::

    $ pytest

.. _Pytest: http://pytest.org


Using docker
------------

If you want to use docker, just clone the repo and start docker compose::

    $ git clone http://github.com/ejplatform/ej-server/
    $ sudo docker-compose -f ./docker/develop/start.yml up -d

After the command, **ej-server** can be accessed at http://localhost:8000.


Tests
-----

There are two ways to locally execute the automated tests using
docker-compose:

-  If you already ran
   ``sudo docker-compose -f ./docker/local/start.yml up -d`` and the
   server is up and running, execute:

.. code:: bash

    sudo docker-compose -f ./docker/local/start.yml exec django pytest

-  If you just want to run the tests without necessarily getting up all
   the services available on local environment, the configuration file
   on docker-compose
   `docker/local/test.yml <https://github.com/ejplatform/ej-server/blob/master/docker/local/test.yml>`__
   will have only the necessary services to run the tests. To run the
   tests, execute:

.. code:: bash

    sudo docker-compose -f ./docker/local/test.yml run --rm django

Environment Variables
---------------------

The
`env.example <https://github.com/ejplatform/ej-server/blob/master/env.example>`__
file has all the environment variables defined to **ej-server**.

Additionally, the docker-compose environment variables files are defined
on their own directory:

-  `docker/local/start.yml <https://github.com/ejplatform/ej-server/blob/master/docker/local/start.yml>`__:
   `docker/local/env/*.env <https://github.com/ejplatform/ej-server/tree/master/docker/local/env>`__
-  `docker/local/idle.yml <https://github.com/ejplatform/ej-server/blob/master/docker/local/idle.yml>`__:
   `docker/local/env/*.env <https://github.com/ejplatform/ej-server/tree/master/docker/local/env>`__
-  `docker/local/test.yml <https://github.com/ejplatform/ej-server/blob/master/docker/local/test.yml>`__:
   `docker/local/env/*.test.env <https://github.com/ejplatform/ej-server/tree/master/docker/local/env>`__
-  `docker/production/deploy.example.yml <https://github.com/ejplatform/ej-server/blob/master/docker/production/deploy.example.yml>`__:
   Example defined on itself

Deployment
----------

An example of deploy in production using docker-compose can be found in
`docker/production/deploy.example.yml <https://github.com/ejplatform/ej-server/blob/master/docker/production/deploy.example.yml>`__.

Continuous Deployment
---------------------

Commits at ``develop`` branch will release to http://dev.ejplatform.org.

Commits at ``master`` branch will release to https://ejplatform.org.

Rocketchat Integration
----------------------

See the guidelines at
`docker/extensions <https://github.com/ejplatform/ej-server/blob/master/docker/extensions#using-rocketchat>`__.

.. |pipeline status| image:: https://gitlab.com/ejplatform/ej-server/badges/master/pipeline.svg
   :target: https://gitlab.com/ejplatform/ej-server/commits/master
.. |pipeline status| image:: https://gitlab.com/ejplatform/ej-server/badges/develop/pipeline.svg
   :target: https://gitlab.com/ejplatform/ej-server/commits/develop
.. |pipeline status| image:: https://gitlab.com/ejplatform/ej-server/badges/master/pipeline.svg
   :target: https://gitlab.com/ejplatform/ej-server/commits/master
.. |pipeline status| image:: https://gitlab.com/ejplatform/ej-server/badges/develop/pipeline.svg
   :target: https://gitlab.com/ejplatform/ej-server/commits/develop