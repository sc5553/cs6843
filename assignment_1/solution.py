### welcome_assignment_answers
### Input - All eight questions given in the assignment.
### Output - The right answer for the specific question.

def welcome_assignment_answers(question):
    default_answer = "No"
    if question == "Are encoding and encryption the same? - Yes/No":
        return default_answer
    elif question == "Is it possible to decrypt a message without a key? - Yes/No":
        return default_answer
    elif question == "Is it possible to decode a message without a key? - Yes/No":
        return default_answer
    elif question == "Is a hashed message supposed to be un-hashed? - Yes/No":
        return default_answer
    elif question == "What is the MD5 hashing value to the following message: 'NYU Computer Networking' - Use MD5 hash generator and use the answer in your code":
        return "42b76fe51778764973077a5a94056724"
    elif question == "Is MD5 a secured hashing algorithm? - Yes/No":
        return default_answer
    elif question == "What layer from the TCP/IP model the protocol DHCP belongs to? - The answer should be a numeric number":
        return 3
    elif question == "What layer of the TCP/IP model the protocol TCP belongs to? - The answer should be a numeric number":
        return 2

# Complete all the questions.


if __name__ == "__main__":
   # use this space to debug and verify that the program works
   debug_question = "What layer of the TCP/IP model the protocol TCP belongs to? - The answer should be a numeric number"
   print(welcome_assignment_answers(debug_question))
