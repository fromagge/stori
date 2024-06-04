import os
from authentication.app import create_app

app = create_app()

if __name__ == '__main__':
	if not (PORT := os.environ.get('PORT')):
		PORT = 5000

	app.run(debug=True, threaded=True, port=PORT)