from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import io
import os
from flask import Flask, render_template, send_file, make_response, request, abort, url_for, Markup
import sqlite3


def getdata(c):
	c.execute("SELECT * FROM data")
	data = c.fetchall()
	date = []
	d1 = []
	d2 = []
	d3 = []
	d4 = []
	d5 = []
	for row in data:
		date.append(row[0] + " " + row[1])
		d1.append(row[2])
		d2.append(row[3])
		d3.append(row[4])
		d4.append(row[5])
		d5.append(row[6])
	return date, d1, d2, d3, d4, d5


app = Flask(__name__)

# Default Entry (index.html)
@app.route('/')
def index():
	f = open("whitelist.txt")
	ret = ""
	for device in f.readlines():
		device = device.rstrip()
		s = "<a href=\"device_%s.html\">%s</a><br>" % (device, device)
		ret = ret + Markup(s)
	return render_template("index.html", text=ret)

# Dynamic access to each device 
@app.route('/device_<name>.html')
def device(name):
	return render_template("device.html",device=name)

# Plotting Data 1 for Device 
@app.route('/plot/<name>_d<int:num>')
def plot_data(name,num):
	cdir = os.getcwd()
	try:
		f = cdir + "/%s.db" % name
	except:
		abort(404)
	con = sqlite3.connect(f)
	c = con.cursor()
	date, d1, d2, d3, d4, d5 = getdata(c)
	con.close()

	if num == 1:
		ys = d1
	elif num == 2:
		ys = d2
	elif num == 3:
		ys = d3
	elif num == 4:
		ys = d4
	else:
		ys = d5

	fig = Figure()
	axis = fig.add_subplot(1, 1, 1)
	axis.set_title("Data %d for %s" % (num,name))
	axis.set_xlabel("Date")
	axis.grid(True)
	xs = range(len(date))
	axis.plot_date(date,ys)
	fig.autofmt_xdate()
	canvas = FigureCanvas(fig)
	output = io.BytesIO()
	canvas.print_png(output)
	response = make_response(output.getvalue())
	response.mimetype = 'image/png'
	return response

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
