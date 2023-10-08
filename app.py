from flask import Flask, render_template



app=Flask(__name__)

JOBS=[
  {'id':1, 
  'title': 'Software developer',
'experience':'2 years'}
]

@app.route('/')
def home():
  return render_template('home.html', jobs=JOBS, person="Shafiul Alam")


if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)
