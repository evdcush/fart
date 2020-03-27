::

             _____                    _____                    _____                _____
            /\    \                  /\    \                  /\    \              /\    \
           /::\    \                /::\    \                /::\    \            /::\    \
          /::::\    \              /::::\    \              /::::\    \           \:::\    \
         /::::::\    \            /::::::\    \            /::::::\    \           \:::\    \
        /:::/\:::\    \          /:::/\:::\    \          /:::/\:::\    \           \:::\    \
       /:::/__\:::\    \        /:::/__\:::\    \        /:::/__\:::\    \           \:::\    \
      /::::\   \:::\    \      /::::\   \:::\    \      /::::\   \:::\    \          /::::\    \
     /::::::\   \:::\    \    /::::::\   \:::\    \    /::::::\   \:::\    \        /::::::\    \
    /:::/\:::\   \:::\    \  /:::/\:::\   \:::\    \  /:::/\:::\   \:::\____\      /:::/\:::\    \
   /:::/  \:::\   \:::\____\/:::/  \:::\   \:::\____\/:::/  \:::\   \:::|    |    /:::/  \:::\____\
   \::/    \:::\   \::/    /\::/    \:::\  /:::/    /\::/   |::::\  /:::|____|   /:::/    \::/    /
    \/____/ \:::\   \/____/  \/____/ \:::\/:::/    /  \/____|:::::\/:::/    /   /:::/    / \/____/
             \:::\    \               \::::::/    /         |:::::::::/    /   /:::/    /
              \:::\____\               \::::/    /          |::|\::::/    /   /:::/    /
               \::/    /               /:::/    /           |::| \::/____/    \::/    /
                \/____/               /:::/    /            |::|  ~|           \/____/
      __                _            /:::/    /             |::|   |
     / _|  __ _   _ _  | |_         /:::/    /              \::|   |
    |  _| / _` | | '_| |  _|        \::/    /                \:|   |
    |_|   \__,_| |_|    \__|         \/____/                  \|___|

       ,...
     .d' ""                    mm         ,dPYb,                           I8
     dM`                       MM         IP'`Yb                           I8
    mMMmm   ,6"Yb.  `7Mb,od8 mmMMmm       I8  8I                        88888888
     MM    8)   MM    MM' "'   MM         I8  8'                           I8
     MM     ,pm9MM    MM       MM         I8 dP     ,gggg,gg   ,gggggg,    I8
     MM    8M   MM    MM       MM         I8dP     dP"  "Y8I   dP""""8I    I8
   .JMML.  `Moo9^Yo..JMML.     `Mbmo      I8P     i8'    ,8I  ,8'    8I   ,I8,
                                         ,d8b,_  ,d8,   ,d8b,,dP     Y8, ,d88b,
                                         PI8"8888P"Y8888P"`Y88P      `Y888P""Y88
    _______  _______  ______    _______  I8 `8,
   |       ||   _   ||    _ |  |       | I8  `8,       ___       __  ___
   |    ___||  |_|  ||   | ||  |_     _| I8   8I      |__   /\  |__)  |
   |   |___ |       ||   |_||_   |   |   I8   8I      |    /~~\ |  \  |
   |    ___||       ||    __  |  |   |   I8, ,8'
   |   |    |   _   ||   |  | |  |   |    "Y8P'
   |___|    |__| |__||___|  |_|  |___|

            _               _                   _             _
           /\ \            / /\                /\ \          /\ \
          /  \ \          / /  \              /  \ \         \_\ \
         / /\ \ \        / / /\ \            / /\ \ \        /\__ \
        / / /\ \_\      / / /\ \ \          / / /\ \_\      / /_ \ \
       / /_/_ \/_/     / / /  \ \ \        / / /_/ / /     / / /\ \ \
      / /____/\       / / /___/ /\ \      / / /__\/ /     / / /  \/_/
     / /\____\/      / / /_____/ /\ \    / / /_____/     / / /
    / / /           / /_________/\ \ \  / / /\ \ \      / / /
   / / /           / / /_       __\ \_\/ / /  \ \ \    /_/ /
   \/_/            \_\___\     /____/_/\/_/    \_\/    \_\/

              ███████  █████   ██████  ████████  ██
              ██      ██   ██  ██   ██    ██     ██
              █████   ███████  ██████     ██     ██
              ██      ██   ██  ██   ██    ██
              ██      ██   ██  ██   ██    ██     ██



.. image:: https://img.shields.io/pypi/v/fart.svg
    :target: https://pypi.python.org/pypi/fart
    :alt: Latest PyPI version

Make text banners to visually divide segments in your code with fart.

What's a fart?

.. code-block::

    //-----------------------------------------------------------------------------//
    //                               This is a fart.                               //
    //-----------------------------------------------------------------------------//


    #=============================================================================#
    #              ____              _           _     _       _                  #
    #             / ___|    ___     (_)  ___    | |_  | |__   (_)  ___            #
    #             \___ \   / _ \    | | / __|   | __| | '_ \  | | / __|           #
    #              ___) | | (_) |   | | \__ \   | |_  | | | | | | \__ \           #
    #             |____/   \___/    |_| |___/    \__| |_| |_| |_| |___/           #
    #                                                                             #
    #=============================================================================#




Fart is short for Figlet ART. This program is very similar to Figlet, and most fonts are borrowed from from it. Fart is focused on making text banners for use in code documentation.

As such, all generated text is **encapsulated by commenting characters** and copied to clipboard, so you can easily paste your fart into your code.



Usage
=====
There are two types of farts currently supported:

.. code-block::

    $ fart text-box style

    #=============================================================================#
    #                                text-box style                               #
    #=============================================================================#



and...

.. code-block::

    $ fart figlet style --font big

    #=============================================================================#
    #        __   _           _          _             _             _            #
    #       / _| (_)         | |        | |           | |           | |           #
    #      | |_   _    __ _  | |   ___  | |_     ___  | |_   _   _  | |   ___     #
    #      |  _| | |  / _` | | |  / _ \ | __|   / __| | __| | | | | | |  / _ \    #
    #      | |   | | | (_| | | | |  __/ | |_    \__ \ | |_  | |_| | | | |  __/    #
    #      |_|   |_|  \__, | |_|  \___|  \__|   |___/  \__|  \__, | |_|  \___|    #
    #                  __/ |                                  __/ |               #
    #                 |___/                                  |___/                #
    #                                                                             #
    #=============================================================================#



You can specify which characters to use for the commenting char ("cap") and line char ("line").
For example::

    $ fart C++ -f georgia11 -c // -l '#'

    //#############################################################################//
    //                                                                             //
    //                         .g8"""bgd                                           //
    //                       .dP'     `M                                           //
    //                       dM'       `     M         M                           //
    //                       MM              M         M                           //
    //                       MM.         mmmmMmmmm mmmmMmmmm                       //
    //                       `Mb.     ,'     M         M                           //
    //                         `"bmmmd'      M         M                           //
    //                                                                             //
    //#############################################################################//



Farts are automatically copied to your clipboard for convenience. To disable this functionality, make sure to flag your farts with ``-n``.


To see all available fonts and their supported character-sets, enter ``fart -s`` or ``fart --sample``.


Installation
============
Install through pip::

    pip install fart


Requirements
------------
Package was built for use in python 3. Probably works in python 2.

Additional required packages:

- pyperclip



Acknowledgements
================
FIGlet fonts are licensed under the BSD-3 by the original authors at http://www.figlet.org.

Big thanks to the members of the `Laboratory of Plasma Physics (LPP) <https://github.com/LaboratoryOfPlasmaPhysics>`_ who were the original farters on PyPi with `Find All Roots with a Tree <https://github.com/LaboratoryOfPlasmaPhysics/fart>`_, but graciously allowed me fart on PyPi.


License
-------
Code is licensed under `BSD-3`_ and any font assets are copyright by original authors.


.. Substitutions:


.. LOCAL FILES:
.. _BSD-3: LICENSE
