string = "These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:"

email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

#print(email_two)
shortlist = ["emails", "open", "save"]

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

def censor_word(source, text):
  return source.replace(text, "")

#print(censor_word(email_two))

def censor3(string, shortlist):
  """
  ns = []
  new = string.split()
  for i in new:
    if i not in shortlist:
      ns.append(i)
  return ns
  """
  ns = [i for i in string.split() if i not in shortlist]
  ns = " ".join(ns)
  return ns

print(censor3(string, shortlist)) 

"""
def censor_all(email, words):
  ns = "email"
  for i in words:
    ns += ".replace("+i+", \"\")"
    print(ns, "\n")
  return ns
"""    
  #for i in range(len(words)):
  #  words[i]
    
"""   
def censor_all(email, words):
  print(email, "\n")
  ns = []
  string = email.split()
  for i in range(len(string)):
    for w in words:
      print(string[i], w)
      if string[i] == w:
        ns.append("XXX")
      elif ns[i] != string[i]:
        ns.append(string[i])
  print(ns)
  string = " ".join(ns)
  return string     
"""
"""
def censor_all(email, words):
  print(email, "\n")
  ns = []
  string = email.split()
  for i in string:
    for w in words:
      print(i, w)
      if i == w:
        ns.append("")
      elif ns[i] != i:
        ns.append(i)
"""       

#print(censor_all(string, words))
