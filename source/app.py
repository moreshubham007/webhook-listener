from flask import Flask, request, render_template
import pandas as pd
import os
from datetime import date
app = Flask(__name__)

# @Authur of code shubhammore07@outlook.com 

# global variables
json_file = 'payload'
false = 'false'
null = 'Empty'

def createFile(file_path,file_name,output,location):
    if file_path:
        output.to_csv(os.path.join(location), mode='a', index=True, header=False)
        print("######### File Already Existing: "+file_name+"\n######### File updated")
    else:
        print('######### File Not Found\nNew File Creating With Name: '+file_name+'\n ######### File Updated')
        output.to_csv(os.path.join(location), mode='a', index=True, header=True)  
    return True
    
def folder(today):
    dir = os.path.join("/data/",today)
    if not os.path.exists(dir):
         os.mkdir(dir)
         print('######### New Folder Created: '+today)
    return True


@app.route('/')
def index():
    # today=str(date.today())
    # data = request.get_json()
    # load = data[json_file]
    # output = pd.json_normalize(load)
    # print(output)
    # folder(str(date.today()))
    # file_name ='all_data '+str(date.today())+'.csv'
    # location ='./'+str(date.today())+'/'+file_name
    # file_path= os.path.isfile(os.path.join(location))
    # createFile(file_path,file_name,output,location)
    return render_template('index.html')
# Individual Accounts

@app.route('/individual',methods=['GET','POST'])
def individual():
    # today=str(date.today())
    data = request.get_json()
    load = data[json_file]
    output = pd.json_normalize(load)
    folder(str(date.today()))
    file_name ='NON-TL_data '+str(date.today())+'.csv'
    location ='/data/'+str(date.today())+'/'+file_name
    file_path= os.path.isfile(os.path.join(location))
    createFile(file_path,file_name,output,location)
    
    return('NON-TL_Data')


# click rate app
@app.route('/click',methods=['GET','POST'])
def click():
    data = request.get_json()
     # production will use "payload" instead of "message dict"
    load = data[json_file]
    # print(load)
    output = pd.json_normalize(load)
    file_name ='click_data '+str(date.today())+'.csv'
    folder(str(date.today()))
    location ='/data/'+str(date.today())+'/'+file_name
    file_path= os.path.isfile(os.path.join(location))
    createFile(file_path,file_name,output,location)
    return('click page')

#open rate app
@app.route('/open',methods=['GET','POST'])
def open():
    data = request.get_json()
     # production will use "payload" instead of "message dict"
    load = data[json_file]
    # print(load)
    output = pd.json_normalize(load)
    file_name ='open_data '+str(date.today())+'.csv'
    folder(str(date.today()))
    location ='/data/'+str(date.today())+'/'+file_name
    file_path= os.path.isfile(os.path.join(location))
    createFile(file_path,file_name,output,location)
    return('open page')

# all event include (sent,bounced,hardfail)
@app.route('/all_events',methods=['GET','POST'])
def allEvents():
    data = request.get_json()
     # production will use "payload" instead of "message dict"
    load = data[json_file]
    # print(load)
    output = pd.json_normalize(load)
    file_name ='all_data '+str(date.today())+'.csv'
    folder(str(date.today()))
    location ='/data/'+str(date.today())+'/'+file_name
    file_path= os.path.isfile(os.path.join(location))
    createFile(file_path,file_name,output,location)
    return('all_event_page')

# include only hardfail and bounces
@app.route('/hardfail_bounces',methods=['GET','POST'])
def deliveryFaild():
    data = request.get_json()
     # production will use "payload" instead of "message dict"
    load = data[json_file]
    # print(load)
    output = pd.json_normalize(load)
    file_name ='delivery_fail_data '+str(date.today())+'.csv'
    folder(today=str(date.today()))
    location ='/data/'+str(date.today())+'/'+file_name
    file_path= os.path.isfile(os.path.join(location))
    createFile(file_path,file_name,output,location)
    return('delivery_failed_page')

# include held messages page
@app.route('/held_messages',methods=['GET','POST'])
def heldMessages():
    data = request.get_json()
     # production will use "payload" instead of "message dict"
    load = data[json_file]
    output = pd.json_normalize(load)
    file_name ='held_data '+str(date.today())+'.csv'
    folder(today=str(date.today()))
    location ='/data/'+str(date.today())+'/'+file_name
    file_path= os.path.isfile(os.path.join(location))
    createFile(file_path,file_name,output,location)
    return ('held_page')
    
if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0',port='8181')