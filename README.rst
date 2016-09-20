=========
helga-elo
=========

Provide a system through which you may compare players of arbitrary games

Installation
============

After installing and configuring helga, use::

    pip install helga-elo

Add ``elo`` to your settings and restart helga.

Usage
=====

Note: Please use punctuation in your text. This is a tough sticking point in
practice, but it is important to be able to differentiate sentences.

Command syntax::

    elo add <game_type> <winning_player_name> <losing_player_name>
    elo list <game_type> <player_name>
    elo drop <game_type>

Arguments
---------

``game_type``: An identifier for the type of game played. This allows for
different types of games or tournament results to be saved separately.

``player_name``: Name of participant to list details

``winning_player_name``: Name of participant who won game

``losing_player_name``: Name of participant who lost game

Examples
========

The following are different ways you may usage helga-elo

Adding results of a game
------------------------

.. code-block::

    !elo add pingpong jrobison helga
    helga> jrobison now has 805 elo, helga has 795 elo

See player rating
-----------------

.. code-block::

    !elo pingpong jrobison
    helga> jrobison has 805 elo for pingpong

Remove ALL elo for a game_type
------------------------------

.. code-block::

    !elo drop pingpong
    helga> consider it done

License
=======

Copyright (c) 2016 Jon Robison

See included LICENSE for licensing information
