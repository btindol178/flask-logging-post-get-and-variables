from flask import Flask,request,json
import requests


#import logging
from datetime import datetime
#and the access its now method simpler
app = Flask(__name__)
 
#logging.basicConfig(filename='record.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')


#https://stackoverflow.com/questions/15974730/how-do-i-get-the-different-parts-of-a-flask-requests-url
@app.route('/') 
@app.route('/blogs')
def blog():
    var1 = request.url
    r = requests.get(var1)
    print(r.status_code)
    # app.logger.warning('testing warning log')
    # app.logger.error('testing error log')
    # app.logger.info('testing info log')
    var1 = "fart"
    print(var1)
    now1 = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")

    print( now1 ," ", request.method," ",request.url)
    print(request.headers)

    print(request.method)              
    print(request.url)                  
    print(request.base_url)              
    print(request.url_charset)           
    print(request.url_root)            
    print(str(request.url_rule))        
    print(request.host_url)              
    print(request.host)                
    print(request.script_root)  
    print(request.path)                 
    print(request.full_path)  

    log = now1  + " " +  request.method +  " " +  request.url +  " " +  var1
    # Print things to the file 
    with open("server.log", "a") as fd:
        fd.write("\n")
        fd.writelines(log)

    data = {"some_key":"some_value"} # Your data in JSON-serializable type
    response = app.response_class(response=json.dumps(data),
                                  status=200,
                                  mimetype='application/json')
    print(response)
    return f"Welcome to the Blog"
 
if __name__ == "__main__":
    app.run()
