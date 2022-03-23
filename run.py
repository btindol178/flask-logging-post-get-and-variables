from flask import Flask,request
#import logging
from datetime import datetime
#and the access its now method simpler
app = Flask(__name__)
 
#logging.basicConfig(filename='record.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

#https://stackoverflow.com/questions/15974730/how-do-i-get-the-different-parts-of-a-flask-requests-url
@app.route('/') 
@app.route('/blogs')
def blog():
    # app.logger.warning('testing warning log')
    # app.logger.error('testing error log')
    # app.logger.info('testing info log')
    var1 = "fart"
    print(var1)
    now1 = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")

    print( now1 ," ", request.method," ",request.url)

    log = now1  + " " +  request.method +  " " +  request.url +  " " +  var1
    # Print things to the file 
    with open("server.log", "a") as fd:
        fd.write("\n")
        fd.writelines(log)


    return f"Welcome to the Blog"
 
if __name__ == "__main__":
    app.run()
