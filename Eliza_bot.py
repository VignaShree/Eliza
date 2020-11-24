#AIT 590 
#Vigna Shree Telukunta
import random
import re
#welcome message
print("="*75)
print("Hi I am Eliza psychotherapist.How can I help you today ?")
print("="*75)
print("may I know your name please")
user_name = input('~')
#Greeting the user with user name
print("Hello, "+user_name+". How can I help you today?")
reply = ''
#possible words to quit the chat
quit_words = ['Goodbye', 'Bye', 'Exit','bye', 'goodbye', 'exit', 'tata']

pairs = {
            "(.*)":
         ["Please elaborate %1","I would like to know more about %1","Please proceed","Go ahead and carry on"],
    "I want (.*)":
        ["how do you want to %1?","What will you do after you finish %1?"],
    "I need (.*)":
        ["Why do you need %1?","Can you share me the reason why you need %1?"],
    "I would like (.*)":
        ["Why would you like %1?","Could tell me the reason why you would like %1?"],
    "I am (.*)":
        ["Good to hear!Go ahead","carry on ..let's speak more"],
    "no":
        ["You are being a bit negative","why are you not accepting this"],
    "(.*) may be":
        ["whats the reason for the uncertainity?"],
    "(.*) dont know":
        [""],
    "I'm (.*)":
        ["Sounds interesting!","Explain me briefly about %1"],
    "I feel(.*)":
        ["I too feel the same","You have more chnaces in life"],
    "I will (.*)":
        ["I hope you do %1","Believe in you.You will surely %1"],
    "I am going to (.*)":
        ["when are you coming back from %1?","So happy that you are going to %1"],
    "I am stressed(.*)":
        ["why are you stressed?Trust yourself","Believe in you","Don't take things so personally"],
    "What (.*)":
        ["Do you want me to discuss about %1","Can you elaborate %1"],
    "How (.*)":
        ["Do you know how to approach?","Please try elaborating more about it"],
    "(.*) mother(.*)":
        ["Can you share your beautiful moments with your mother","Do you see your self in your mother?"],
    "(.*) father(.*)":
        ["Do you like your father?","I would like to know more about your father","what is your favorite moment with your father?"],
    "(.*) sister(.*)":
        ["Is your sister elder than you?","Do you like spending time with your sister?"],
    "(.*) child(.*)":
        ["Do you like your life as a child?","what is your favorite moment in your childhood?"],
    "(.*) family(.*)":
        ["How big is your family?","how many people stay with you?"],
    "(.*) home(.*)":
        ["How many people stay with you at your home?","where is your home located?","How far is your home from shore?"],
    "(.*) school(.*)":
        ["what is your first school?","how far is your school from your home?"],
    "(.*) friend(.*)":
        ["who is your best friend?","what qualities do you like the most in your best friend"],
    "(.*) problems(.*)":
        ["Do you think big about small problems?","what is your longstanding problem?",
        "Do you think you have more problems compared to your friends?","Try to find a temporary solution for a permanent problem"],
    "(.*) book(.*)":
        ["Which is the best of all the books that you read so far?","When did you start reading books?"],
    "(.*) science(.*)":
        ["Do you like advancement in science and technology?","What are the latest inventions in science","Who is your favorite science teacher?"],
    "It is (.*)":
        [ "You seem very confident.","yeah it is %1 .Tell me more "],
    "(.*)maybe (.*)":
        ["You seem very confident.","Don't feel uncertain about %1,It will happen no matter What"],
    "(.*) bus(.*)":
        ["Do you like travelling in bus?","Do you prefer bus journey over train journey?"],
    "(.*) food(.*)":
        ["What is your favorite food?","Why you like that food?"],
     
}
#dictionary for reflective words
#Our eliza bot uses the following reflections
reflections = {
    "am" : "are","i" : "you","me" : "you",
    "was" : "were","my" : "your","you'd" : "I would",
    "you've" : "I have","you'll"  : "I will","you" : "I",
    "are" : "am","your" : "my","yours" : "mine",
    "mine" : "yours","i'd"  : "you would","i've"  : "you have",
    "i'll"  : "you will","i'm"  : "you are","you're"  : "I am"
    }
#transformation function is used to transform the words into sententences
def transformation(org_str):
#to convert the sentence to lower case
    org_str= org_str.lower()
#split the sentence to words
    words=re.split(r'[\s\t\n]+', org_str)
    new_words=[]
    for word in words:
        new_words.append(replace(word, reflections))
    transformed = ' '.join(new_words)
    return transformed
#replace function is defined to replace the singular person with reflections
#original_word: word to be replaced
#reflections:used to replace the word
def replace(original_word, reflections):
    for key in reflections.keys():
        if original_word == key:
            return reflections.get(key)
    return original_word
#respond function is used to get the sententence from the user and search in the pattern
def respond(ques, question_list):
    answer="Can you tell more about it?"#default answer
#Check if the user is replying Yes.
    if re.match(r'Yes|yes', ques):
        answer = "You seem confident.please elaborate."
#loop through the keys in dictionary            
    else:
        for x in question_list:
            xl = re.compile(x, re.IGNORECASE)
            is_match = re.match(xl, ques)
            if is_match:
                answer = random.choice(question_list[x])
                position = answer.find('%')
                while position > -1:
                    count = int(answer[position+1:position+2])
                    answer = answer[:position] + \
                    transformation(is_match.group(count)) + \
                    answer[position+2:]
                    position = answer.find('%')
                 
    return answer
#prolonged_conversation is used to check if the user wants to quit or continue the conversation with eliza
def prolonged_conversation(reply):
    if reply in quit_words:
        print("It was great speaking with you,see you soon")
    else:
        re = transformation(reply)
        strReply=respond(reply, pairs)
        print(re+". "+strReply)
    return

#checking the continuation of the conversation
while reply not in quit_words:
    try:
        reply = input("~")
        prolonged_conversation(reply)        
    except EOFError:
        print("Bye")
        exit()