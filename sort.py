import openai
import json
import time
import os


def dictToList(d):
    return list(d.keys())
            

def listToString(s):
    str1 = " "
    return (str1.join(s))
    
def main():
    while True:
        #if file is empty do not conitnue
        if os.path.getsize('checklist.json') == 0:
            print("File is empty!")
            break

        else:
            #open file contents
            sort_file = open('checklist.json','r')
            txt1 = json.load(sort_file)
            sort_file.close()

            #dict type
            print(type(txt1), ";", txt1)
            time.sleep(2)

            #convert to list type 
            new_list = (dictToList(txt1))
            print(type(new_list),":",new_list)
            

            #convert list to str type
            string = (listToString(new_list))
            print(type(string),":", string)
            
            API_KEY = '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'
            openai.api_key = API_KEY
            model = 'text-davinci-003'
            prompt = "randomly rank each item from most to least important. return it as a dict type with "" "+ string
            response = openai.Completion.create(
                prompt = prompt,
                model = model,
                temperature=0.1,
                max_tokens=64,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0
                
            )
            for result in response.choices:
                time.sleep(2)
                openai_result = result.text
                
                
                file = open('sort_file.json','w+')
                file.write(openai_result)
                file.close()
                print(type(openai_result),";", openai_result)
            break
            

if __name__ == '__main__':
    main()
