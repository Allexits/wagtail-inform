## Created admin panel with headless cms - Wagtail

## Uses GraphQl

### Endpoint for request
#### https://wagtail-inform.onrender.com/api/graphql/
#### Request
    query{
      pages{
        title
        url
      }
    }
#### Response
    {
        "data": {
            "pages": [
            {
                "title": "Inform Front Page.",
                "url": "/"
            },
            {
                "title": "Videos",
                "url": "/videos/"
            },
            {
                "title": "Topics",
                "url": "/topics/"
            },
        ]
      }
    }
