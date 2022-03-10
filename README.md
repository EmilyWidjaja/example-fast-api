# API 

## Development

Requirements:

- Python 3.9.2
- MongoDB 

Setting up a Python environment:

```bash
python --version
  Python 3.9.2
```

```bash
pip install virtualenv
virtualenv venv
source ./venv/bin/activate
pip install -r requirements.txt
```

Start a development instance:

```bash
source ./venv/bin/activate
uvicorn app.main:app --reload --port 3000
```


## Testing APIs

Access all the APIs through http://localhost:3000/docs


## Project Structure

```
app
├── controllers                   /* Folder: All API entry points */
│   ├── __init__.py         
│   ├── image_controller.py
│   ├── model_controller.py
│   └── token_controller.py
├── core                         /* Folder: schemas, configurations etc. */
│   ├── config.py
│   ├── logging.py
│   ├── ml_model.py
│   ├── settings.py
│   ├── token_data_model.py
│   └── token_model.py
├── __init__.py
├── main.py                     /* Server entry point */
├── services                    /* Folder: services files to query external database */
│   ├── __init__.py
│   ├── mongodb_service.py
└── utils                       /* Folder: additional utility programs, e.g., security */
    ├── __init__.py
    ├── jwt_service.py
```


# Notes

- Used MongoDB Atlas free managed database for development and testing.
- Screenshot of the API testing panel http://localhost:3000/docs


<img src="docs/example-swagger-screenshot.png" alt="drawing" width="800"/>
