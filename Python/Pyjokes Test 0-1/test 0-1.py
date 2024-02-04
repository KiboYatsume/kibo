import pyjokes
import Artrimus as a
# Get a random joke
joke = pyjokes.get_joke()

# Print the joke
print(joke)
a.speak(joke)
