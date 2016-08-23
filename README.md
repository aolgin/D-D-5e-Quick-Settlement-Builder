Quick Settlement Builder
========================

This is a small python application created to quickly generate random settlements for an upcoming game of Dungeons and Dragons, 5th Edition.

It uses various elements of our world, Ardon\'Ya, and many elements taken from a quick settlement builder sheet. All it does is generate random numbers over tables, and then format them

This application is still in its infancy. I'm ultimately planning on putting a simplistic gui over it, and making it a bit more parametrized rather than only apply specifically to my crafted world. A CSV export option will also be added.

Important Note on Output
------------------------

This application will create a randomly generated settlement based of tables. Don't plan on using roughly half of them, due to no form of correction to inconsistencies (such as a small farm acting as a major trade center). At the very least, you may gain some inspiration for settlements.

Also, the sheet I used for many of these tables made heavy use of German-sounding names. Not intentional, I just admittedly do not have an alternative at the moment.


Current Usage
-------------

Run the application from the CLI
```
python /path/to/quick-settlement-builder.py
```

To turn on an optional debugging mode, which adds in maany extra print statemetns, simply pass the argument 'True' via CLI.

After starting the applciatn, you will be prompted for a number of settlements to generate. Supply a number, hit Enter, and then record.