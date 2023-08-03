def get_input(word_type: str):
    user_input: str =input(f"Enter a {word_type}:")
    return user_input

Noun1= get_input("Noun1")
Adj1=get_input("Adj1")
Verb1= get_input("Verb1")
Pronoun1=get_input("Pronoun1")
Pronoun2=get_input("Pronoun2")
Noun2= get_input("Noun2")
Verb2= get_input("Verb2")

Story= f"""
Once upon a time,  there was a {Adj1} {Pronoun1} who loved to read his books all the time. 
One day {Noun2} came into his room and caught {Noun1} buried in his books.

{Noun2}: "What are you doing BoomBoom?" 
{Noun1}:"I am just {Verb1}, do you need my help?
{Noun2}:"Why don't you take a break and we can go for some ice cream?"
{Noun1}:" I would love to do that {Pronoun2}!"

And so {Noun1} and his {Pronoun2} went off to {Verb2} ice cream and had a great time.

The end.
"""
print(Story)