Gears Bootstrap
===============

Twitter's Bootstrap_, bundled for Gears.

Bundled version: **3.1.1**.

Installation
------------

Install `Gears`, `gears-less` and `gears-bootstrap` from git:

.. code-block:: bash

    pip install -e git+http://github.com/gears/gears.git@develop#egg=Gears
    pip install -e git+http://github.com/gears/gears-less.git@develop#egg=gears-less
    pip install -e git+http://github.com/yumike/gears-bootstrap.git@develop#egg=gears-bootstrap

If you use ``Environment.register_entry_points()`` in your setup,
`gears-bootstrap` adds itself to the environment automatically. If not,
add it manually::

    from gears_bootstrap import register
    register(environment)

Requirements
------------

`gears-bootstrap` uses `gears-less`, which requires node.js to be installed in
your system.

Usage
-----

Import Bootstrap into a LESS file to get all of Bootstrap's styles, mixins and
variables. For example, in ``css/style.less``::

    @import 'bootstrap.less';

    // You can override any Bootstrap variable here:
    @font-size-base: 12px;
    @navbar-height: 40px;

Use ``//= require`` directive to include Bootstrap javascripts. All of them:

.. code-block:: javascript

    //= require bootstrap

Or individual modules:

.. code-block:: javascript

    //= require bootstrap/modal
    //= require bootstrap/dropdown

.. _Bootstrap: http://getbootstrap.com/
