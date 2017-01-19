#Reverse a sentence by words
def reverse_v1(st):
    words = st.split(" ")
    rev = []
    for i in list(range((len(words)-1),-1,-1)):
        rev.append(words[i])
    return " ".join(rev)
    
def reverse_v2(st):
    return " ".join(st.split(" ")[::-1])
  
#to learn more about python list operations, http://www.diveintopython.net/native_data_types/lists.html
