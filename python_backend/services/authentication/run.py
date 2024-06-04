import os
from app import create_app

app = create_app()

if __name__ == '__main__':
	if not (PORT := os.environ.get('PORT')):
		PORT = 5100

	app.run(debug=True, threaded=True, port=PORT, host='0.0.0.0')