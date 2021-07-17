import nltk
from nltk.tokenize import word_tokenize
from nltk import Tree
import matplotlib
matplotlib.use('Agg')


def parse_and_draw(grammar, text):
    """
    this function parses the text and draws the parse tree
    """
    # Define the parser with the input grammar
    parser = nltk.parse.RecursiveDescentParser(grammar)
    
    # Tokenize the input text
    sent = word_tokenize(text)
    
    for tree in parser.parse(sent):
        print("\n", text, "\n", tree)
        
    # Get the tree from the string
    t = Tree.fromstring(str(tree))
    
    # Draw the parse tree
    t.draw()


# Define grammars
grammar1 = nltk.CFG.fromstring("""
            S -> NP VP
            VP -> V NP | V NP PP
            PP -> P NP
            V -> "saw" | "ate" | "walked"
            NP -> "John" | "Mary" | "Bob" | Det N | Det N PP
            Det -> "a" | "an" | "the" | "my"
            N -> "man" | "dog" | "cat" | "telescope" | "park"
            P -> "in" | "on" | "by" | "with"
        """)
    
grammar2 = nltk.CFG.fromstring("""
            S -> NP VP
            NP -> Det Nom | PropN
            Nom -> Adj Nom | N
            VP -> V Adj | V NP | V S | V NP PP
            PP -> P NP
            PropN -> "Buster" | "Chatterer" | "Joe"
            Det -> "the" | "a"
            N -> "bear" | "squirrel" | "tree" | "fish"
            Adj -> "angry" | "frightened" | "little" | "tall"
            V -> "chased" | "said" | "thought" | "was" | "put"
            P -> "on"
        """)

# Define texts
text11 = "Bob saw John"
text12 = "a man in the park saw a cat"
text13 = "John walked with my dog"  
# The above sentence does not fit the grammar. 
# VP should be either V + NP or V + NP + PP, 
# but in the given sentence it is V + P + NP
text21 = "the tree was tall"
text22 = "Joe was frightened"
text23 = "Chatterer said the bear was angry"

# Invoke the function to parse and draw the trees 
parse_and_draw(grammar1, text11)
parse_and_draw(grammar1, text12)
# parse_and_draw(grammar1, text13)  
parse_and_draw(grammar2, text21)
parse_and_draw(grammar2, text22)
parse_and_draw(grammar2, text23)

