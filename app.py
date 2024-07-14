from flask import Flask, render_template

app = Flask(__name__)

BEDDESIGNS = [
  {
    'Serial No': 1,
    'Bed': 'Double Bed',
    'Wood':'Trek',
    'Color': 'Light Blue',
    'Price': '£150'
  },
  {
    'Serial No': 2,
    'Bed': 'Double Bed',
    'Wood':'Bom',
    'Color': 'Orange',
    'Price': '£250'
  },
  {
    'Serial No': 3,
    'Bed': 'Single Bed',
    'Wood':'Trek',
    'Color': 'Light Purple',
    'Price': '£50'
  }
  
]

@app.route("/")
def hello_world():
  return render_template('home.html', beddesigns=BEDDESIGNS )


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug = True)
