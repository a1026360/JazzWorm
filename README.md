# JazzWorm Chess Engine
An artificial intelligent chess engine, inspired by Paul Puntschart.

## Author
Paul Puntschart

# Test
May use env var 2 boost tf gpu:
Variables name = TF_XLA_FLAGS
Variables value = --tf_xla_enable_xla_devices

# Training
Start fresh training:
* Set "load_model" in main.py to False

Start transition training:
* Set "load_model" in main.py to True
* Take newest .h5 file, and create a copy named "best.h5"
* Take newest .h5.examples file, and create a copy named "best.h5.examples"

## Credits
Thank you Erhard Henkes for your great support.
