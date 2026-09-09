# LMSC-261 Problem Sets 0

### How is the Phone Book Search algorithm working?

**First**, the computer is picking up and opening the book. These steps only need to be done *once* during this process unlike some future steps.

**Then**, the computer is using else/if commands to *methodically* look through the phone book for Mike Smith, and even starting back at the middle of the book if it can't find him.

The steps in the middle are repeated until Mike Smith is found, and once he is he may be called. If the computer can't find him at all, there is an else command telling the computer to quit. This algorithm has accounted for the computer finding Mike Smith immediately, finding him after searching the whole book, and even not finding him at all. There is a path for every possibility of this situation. Unless of course Mike Smith is in there multiple times. I wonder what would happen then. 