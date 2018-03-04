from eve import Eve
import platform

settings={
	'MONGO_HOST': 'localhost',
	'MONGO_PORT': 27017,
	'DOMAIN': {}
}

app = Eve(settings=settings) 

@app.route('/processor')
def processor():
	name = platform.processor()
	return name + "\n"

if __name__ == '__main__':
	app.run()

