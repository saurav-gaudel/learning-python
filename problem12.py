# . Write a program to create a dictionary of Nepali words with values as their English translation. Provide user with an option to look it up!
words = {
    "kitab" :  "book",
    "kalam" : "pensil",
    "masi"  : "ink"
}
a= input("Enter any word in Neplai\n")
a= a.lower()
if a in words:
    print(words[a])
else:
    print("Entered word not in dictionary.")

