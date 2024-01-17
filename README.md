# tgcodetires_api

## Overview
The [TG-Tire API](https://tgtires-api-88167eb20fba.herokuapp.com/docs/) is a Django Rest Framework application designed to provide detailed information about tire sizes and rim specifications at the Swiss type code level. This API empowers users to find precisely matching rims and tires for their vehicles based on Swiss type codes.

<img width="586" alt="Screenshot 2024-01-17 215722" src="https://github.com/ricilandolt/tgcodetires_api/assets/103566118/f14f5b32-069c-4bd3-a7f3-f0e9938535c7">

## Features
Querying Data: Utilize the API to retrieve information about tires, rims, and type codes associated with Swiss vehicles.

Adding Missing Data: Beyond querying, the API allows users to contribute missing data for tires, rims, and type codes, enriching the database for a more comprehensive resource.

## Technologies Used
Django Rest Framework: The API is built using Django Rest Framework, offering a powerful and flexible toolkit for building Web APIs.

Concrete Views: Concrete views have been employed to streamline the API, providing efficient and specialized endpoints for querying and contributing data.

## Getting Started

Installation: Clone the repository and install the required dependencies using:
```
pip install -r requirements.txt
```

### Database Setup: Migrate the database to apply the necessary schema:
```
python manage.py migrate
```
### Run the Server: Start the development server:
```
python manage.py runserver
```

## Usage
### Querying Data
Use the relevant API endpoints to retrieve information about tires, rims, and type codes.

```
GET /api/tires/
GET /api/rims/
GET /api/tgcodes/
```

### Adding Missing Data
Contribute missing data to the API by making POST requests with the relevant information.



```
POST /api/tires/
POST /api/rims/
POST /api/tgcodes/
```
