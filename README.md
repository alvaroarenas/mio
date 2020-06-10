You can se a live demo for this app at [https://mio-app.herokuapp.com](https://mio-app.herokuapp.com/)

## Intalling

`pip install requirements.txt`
`python manage.py migrate`
`python manage.py createsuperuser`
`yarn build`
`python mange.py runserver`

Open [http://localhost:8000](http://localhost:8000) to view it in the browser.
You will need to add some data. For that use http://localhost:8000/admin/
You will need to configure a S3 Amazon bucket to store your images

## Testing
#### Front
`yarn test`

#### Back
`coverage run --source='.' --omit='mio-venv/*' manage.py test`
