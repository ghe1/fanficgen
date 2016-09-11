# Fan Fiction Generator
Markov generator designed to emulate Fan Fictions (stories written by fans of existing universes). This particular one was trained on texts from the two of the most popular universes at the time of this writing: Pokemon and Harry Potter.

This is intended as a fun example of a Markov generator. It is not intended to offend or insult any particular author or style. Be warned that ouput is random and can be NSFW.

The generator is written entirely in Python and uses Pickle to maintain memory.

# Usage
## fanficgen.py
Run fanficgen py with the following arguments:
* -f / --file   : Passing an existing Pickle file with a generated suffix table
* -s / --split  : Pass the number of words to split phrases by, 2 is the most useful split
* -m / --minlen : Minimum length of output by number of words. Note that the generator will always try to finish a sentence.
* -p / --permatable : Save the generated suffix table
* -o / --output : Output file name
* --retrain : Provided a new training text, will either add to suffix table (if used with -f) or create new suffix table
* --help  : Print help list of options

# Training texts
Current training texts are stored in the training folder. These are not the only texts the generator will work on, however fan fiction in general provides a huge source of stories that are freely available.

# But, why?
I thought it would be a fun exercise. The output of the random generator is often shockingly readable. Please feel free to let me know if this generates any entertaining reads!




