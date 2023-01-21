def talk(phrase):
  def say(word):
    print(word)

  words = phrase.split(' ')
  for word in words:
    say(word)

talk("I am going to buy milk.")

def count():
  count = 0

  def increment():
    nonlocal count #used to declare a variable outside of the function
    count = count + 1
    print(count)
  
  increment()
count()