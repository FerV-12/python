import os
from flask import Flask,request,render_template,redirect

app= Flask("__name__")
app.config['UPLOAD_FOLDER'] = 'static/uploads'

@app.route("/")
def showText():
    return render_template('index.html')
  
#/profile/username?age=22
@app.route("/profile")
def showProfile():
    username=request.args.get('username')
    age=request.args.get('age')
    return f"This is currrent profile{username} and is {age}"

# transfer data through routes
# path variable / query parameter

# /profile/ferjhon 
@app.route("/profile/<username>/<myage>")
def showProfile2(username,myage):
    return f"This is currrent profile of{username} and he is {myage}"
  
# path variable / ferjhon lopena
@app.route("/profile/<username>")
def showProfile3(username):
    return f"This is currrent profile of{username}"

@app.route("/profile")
def showProfile4(username):
    username=request.args.get("username")
    return f"This is currrent profile{username}"
  
 # contactus/ user01/kkk@gmail.com  
@app.route("/contactus/<username><email>")
def showContacts(username,email):
    myhobbies={'diving','playing','Sitting','Eating','Hays'}
    userdata={
      'firstname':'SA WAKAS NAPAGANA KO NA NAG UUPDATE NA SIYA DOUBLE CHECK KO ULIT PAG ETO LUMABAS IBIG SABIHIN NAGANA NA SIYA',
      'lastname':'lopena',
      'age':21,
      'email':email,
      'username':username,
    }
    return render_template('contacts.html',myhobbies,userdata=userdata)
  
  
@app.route("/register")
def showregister():
    return render_template('register.html')
  
@app.route("/process/form",methods=['POST'])
def processRegister():
  theusername=request.form['username']
  theemail=request.form['email']
  return render_template('display.html',theusername=theusername,theemail=theemail)

# for the second form 
@app.route("/register2")
def showregister2():
    return render_template('registration.html')
  
@app.route("/register2/form", methods=['POST'])
def processRegister2():
    theusername = request.form['username']
    theage = int(request.form['age'])
    thepass = request.form['password']
    therepass = request.form['repass']
    thetypeuser = request.form['typeuser']
    thepicture = request.files.get('picture') 

    if len(theusername) < 10:
        return redirect('/register2')  
    if thepass != therepass or len(thepass) < 8:
        return redirect('/register2')  
    
     # Save the uploaded picture
    picture_path = None
    if thepicture:
        picture_filename = thepicture.filename
        picture_path = os.path.join(app.config['UPLOAD_FOLDER'], picture_filename)
        thepicture.save(picture_path)

    # Mask the password for admin and client
    if len(thepass) > 10:
        admin_masked_pass = '*' * (len(thepass) - 3) + thepass[-3:]
        client_masked_pass = thepass[:3] + '*' * (len(thepass) - 3)
    else:
        admin_masked_pass = '*' * (len(thepass) - 2) + thepass[-2:]
        client_masked_pass = thepass[:2] + '*' * (len(thepass) - 2)

    if theage < 18:
        if thetypeuser == "admin":
            return render_template('admin.html', theusername=theusername, theage="Minor", thepass=admin_masked_pass,thepicture=picture_path)
        elif thetypeuser == "client":
            return render_template("client.html", theusername=theusername, theage="Minor", thepass=client_masked_pass,thepicture=picture_path)
    else:
        if thetypeuser == "admin":
            return render_template("admin.html", theusername=theusername, theage="Adult", thepass=admin_masked_pass,thepicture=picture_path)
        elif thetypeuser == "client":
            return render_template("client.html", theusername=theusername, theage="Adult", thepass=client_masked_pass,thepicture=picture_path)

    return redirect('/register2')
        
        

if __name__=="__main__":
    app.run(debug=True)