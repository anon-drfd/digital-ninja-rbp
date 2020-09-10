from flask import Flask, render_template
import commentary as comm
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
      return render_template('index.html', title = 'Digital Ninja', 
                            user = comm.user, comments = comm.comments) 

if __name__ == '__main__':
 app.run(host='0.0.0.0', port = 80, debug =True)
