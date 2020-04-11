string = """
These are the emails you will be censoring. 
The open() function is opening the text file
that the emails are contained in and the .read() 
method is allowing us to save their contexts 
to the following variables:"""

email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

#print(email_two)
shortlist = ["emails", "open", "method", "read"]

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

def censor_word(source, text):
  return source.replace(text, "")

#print(censor_word(email_two))

def censor2(string, shortlist):
  print(string, "\n")
  ns = []
  new_s = string.split(" ")
  print(new_s, "\n")
  new_l = []
  for i in shortlist:
    new_l.append(i.lower())
    new_l.append(i.upper())
    new_l.append(i.title())
    if i not in new_l:
      new_l.append(i)
  print(new_l, "\n")
  
  
  for i in new_l:        
    string = string.replace(i, "***")
  return string
    
#print(censor2(string, shortlist)) 
print(censor2(email_two, proprietary_terms))

"""
  for i in new_s:        # i = "Investors,\n\nLots"
       
    
    new_j = []
    new_j = i.split("\n")  # new_j = ['Investors,', '', 'Lots']
    new_k = []             #['Investors', 'Lots']
    for k in new_j:                # k = "Investors,"     #czemu w k 3 razy robi ?
      k = k.strip(" ,\n.:;()?!")
      k = k.replace(i, "***")
      
      new_k.append(k.strip(" ,\n.:;()?!"))   # k = "Investors"
      #print(new_j, k, i)    #['Investors,', '', 'Lots'] "Investors" "Investors,\n\nLots"
    print(new_j, new_k)      #['Investors,', '', 'Lots'] ['Investors', '', 'Lots']
    

    for i in range(len(new_l)):
      if new_k[i] in new_l:

        
    if new_k not in new_l:
      ns.append(i)   # i = "Investors,\n\nLots"
    else:
      ns.append("*****")
"""

"""
  ns = [i for i in string.split() if i not in shortlist]
  
  ns = " ".join(ns)
  return ns
""" 


negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]




######## OFFICAL SOLUTION (IMHOP so so)

# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

def censor_one(input_text, censor):
  censored_item = ""
  for x in range(0,len(censor)):
    if censor[x] == " ":
      censored_item = censored_item + " "
    else:
    	censored_item = censored_item + "X"
  return input_text.replace(censor, censored_item)

# print(censor_one(email_one, "learning algorithm"))

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself", "Helena"]

def censor_two(input_text, censored_list):
  for word in censored_list:
    censored_word = ""
    for x in range(0,len(word)):
      if word[x] == " ":
        censored_word = censored_word + " "
      else:
        censored_word = censored_word + "X"
    input_text = input_text.replace(word, censored_word)
  return input_text

# print(censor_two(email_two, proprietary_terms))

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

def censor_three(input_text, censored_list, negative_words):
  input_text_words = []
  for x in input_text.split(" "):
    x1 = x.split("\n")
    for word in x1:
      input_text_words.append(word)
  for i in range(0,len(input_text_words)):
    if (input_text_words[i] in censored_list) == True:
      word_clean = input_text_words[i]
      censored_word = ""
      for x in range(0,len(word_clean)):
        censored_word = censored_word + "X"
      input_text_words[i] = input_text_words[i].replace(word_clean, censored_word)
    count = 0
    for i in range(0,len(input_text_words)):
      if (input_text_words[i] in negative_words) == True:
        count += 1
        if count > 2:
          word_clean = input_text_words[i]
          for x in punctuation:
            word_clean = word_clean.strip(x)
          censored_word = ""
          for x in range(0,len(word_clean)):
            censored_word = censored_word + "X"
          input_text_words[i] = input_text_words[i].replace(word_clean, censored_word)
  return " ".join(input_text_words)

# print(censor_three(email_three, proprietary_terms, negative_words))

punctuation = [",", "!", "?", ".", "%", "/", "(", ")"]

def censor_four(input_text, censored_list):
  input_text_words = []
  for x in input_text.split(" "):
    x1 = x.split("\n")
    for word in x1:
      input_text_words.append(word)
      
  for i in range(0,len(input_text_words)):
    checked_word = input_text_words[i].lower()
    for x in punctuation:
      checked_word = checked_word.strip(x)
    if checked_word in censored_list:

      # Censoring the targeted word
      word_clean = input_text_words[i]
      censored_word = ""
      for x in punctuation:
        word_clean = word_clean.strip(x)
      for x in range(0,len(word_clean)):
        censored_word = censored_word + "X"
      input_text_words[i] = input_text_words[i].replace(word_clean, censored_word)

      # Censoring the word before the targeted word
      word_before = input_text_words[i-1]
      for x in punctuation:
        word_before = word_before.strip(x)
      censored_word_before = ""
      for x in range(0,len(word_before)):
        censored_word_before = censored_word_before + "X"
      input_text_words[i-1] = input_text_words[i-1].replace(word_before, censored_word_before)

      # Censoring the word after the targeted word
      word_after = input_text_words[i+1]
      for x in punctuation:
        word_after = word_after.strip(x)
      censored_word_after = ""
      for x in range(0,len(word_after)):
        censored_word_after = censored_word_after + "X"
      input_text_words[i+1] = input_text_words[i+1].replace(word_after, censored_word_after)
  return " ".join(input_text_words)

censor_all = proprietary_terms + negative_words

print(email_four, "\n")
print(censor_four(email_four, censor_all))



