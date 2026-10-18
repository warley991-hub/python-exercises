'''
We have a broken message machine that introduces noise to our incoming messages. We know that our messages can't be written using %$&/#·@|º\ª. Unfortunately our machine introduces noise, which means that our message arrives with characters like: %$&/#·@|º\ª within our original message.

Your mission is to write a function which removes this noise from the message.

Notice that noise can only be %$&/#·@|º\ª characters, other characters are not considered to be noise

Examples (input --> output)
"h%e&·%$·llo w&%or&$l·$%d" --> "hello world"
"" --> ""
"%$" --> ""
"abcd" --> "abcd"
"º¤£ª" --> "¤£"

def remove_noise(st):
    pass
'''

def remove_noise(st):
    noise = ['%','$','&','/','#','·','@','|','º','ª','\\']
    for char in noise:
        if char in st:
            st = st.replace(char,'')
    return st