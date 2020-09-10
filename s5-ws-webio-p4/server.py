import dht22
import RPi.GPIO as GPIO
from flask import Flask, render_template
app = Flask(__name__)

GPIO.setmode(GPIO.BOARD)

#Define GPIO pins as output
GPIO.setup(16, GPIO.OUT) #green
GPIO.setup(18, GPIO.OUT) #red

#Switch GPIO pins off
GPIO.output(16, False)  #green
GPIO.output(18, False) #red

@app.route('/') 
def index():
  #DHT22
  dht22.uploadSensorData()
  
  #Get LED status and store to send to HTML
  tempData = {
    'stsLedGr' : GPIO.input(16),
    'stsLedRed' : GPIO.input(18) 
  }
  return render_template('index.html', **tempData)

@app.route('/<button>/<action>')
def ledAction(button, action):
  #Assign buttons (HTML) to GPIO pin
  if button == 'buttonGr':
    ledPin = 16 
  if button == 'buttonRed':
    ledPin = 18

  #Switch LED on/off depending on ‘action'
  if action == 'on':
     GPIO.output(ledPin, True)
  if action == 'off':
     GPIO.output(ledPin, False)

  #Read LED status and store to send to HTML
  ledSts = {
    'stsLedGr' : GPIO.input(16),
    'stsLedRed' : GPIO.input(18)  
  }
  return render_template('index.html', **ledSts)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port =80, debug=True)



