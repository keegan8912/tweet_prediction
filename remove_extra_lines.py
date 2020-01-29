import re

text_1 = "This is some text, that can be used. I am not sure! How many characters? This is an extra line "
text_2 = "What the hell ?"
text_3 = "whoopwhoop."
text_4 = "This is crazyyyyy "
text_5 = "This is some kind of a test. Yeaah."

def remove_extra_lines(text):
    list_of_suffix = [".", ",", "!", "?"]
    idx = []
    for suffix in list_of_suffix:
        idx.append(text.rfind(suffix))

    for suffix in list_of_suffix:
        if text.endswith(suffix, 0, len(text)):
            #save index, take the largest index here
            return text
        # elif text.rfind(suffix) != -1:
        else:
            return text[0:max(idx)+1]

if __name__ == "__main__":
    text = remove_extra_lines(text_1)
    print(text)