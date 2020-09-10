import dht22
import RPi.GPIO as GPIO
from flask import Flask, render_template, Response
from camera_pi import Camera
app = Flask(__name__)

GPIO.setmode(GPIO.BOARD)

#Define GPIO pins as output
GPIO.setup(16, GPIO.OUT) #green
GPIO.setup(18, GPIO.OUT) #red

#Switch GPIO pins off
GPIO.output(16, True)  #green
GPIO.output(18, True) #red

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

@app.route('/camera')
def gen(camera):
  #Video streaming generator function.
  while True:
    frame = camera.get_frame()
    yield (b'--frame\r\n'
           b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    #Video streaming route (Put in img src tag in HTML)
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port =80, debug=True, threaded=True)



