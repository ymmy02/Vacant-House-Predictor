# Web Application to Predict the Image of the House is whether OCCUPIED or VACANT

## Back-end
Django Rest Framework

## Front-end
React.js

## Run on local environment

### Back-end

1. Install the required python libraries by `pip3` command.
```
pip3 install -r requirements.txt
```

2. Make directory named `mlmodels` under `backend/prediction`, and put the Keras learned model there.
```
mkdir backend/prediction/mlmodels
cp [Keras Model] backend/prediction/mlmodels/cnn_keras.h5
```

3. Migrate and run server localy.
```
python3 manage.py migrate
python3 manage.py runserver
```

### Front-end

1. Install `node` version 10.16.0

2. Change directory to frontend and install the required node modules.
```
cd frontend
npm install
```

3. Start the application and access http://localhost:3000/ on the web browser.
```
npm start
```
