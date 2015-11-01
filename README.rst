.. _Nikola: https://getnikola.com/

cathedralcafes
==============

Cathedral Cafes is a basically a fancy Python blog app built on the Nikola_ static site generator.

Installation
------------

Clone the git repository into a directory of your choice::

    $ git clone https://github.com/noisyboiler/cathedralcafes.git

Set up a `virtualenv` for the project::

    $ virtualenv /path/to/your/envs/cathedralcafes
    $ source /path/to/your/envs/cathedralcafes/bin/activate

Install cathedralcafes::

    $ cd cathedralcafes
    $ pip install -r requirements.txt

Build the project::

	nikola build
