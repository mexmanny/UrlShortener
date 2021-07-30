1. Pass in the following to clone the repo to your local:
    `git clone https://github.com/mexmanny/urlshortenerservice.git`

2. Change directory to `urlshortenerservice` by passing:
    `cd urlshortenerservice`

4. Create virtual environment by passing the following:
    `python -m venv testenv` (you can change *testenv* to any other name you would want to use for your virtual environment)

5. Activate virtual environment by passing:
    `source .venv/bin/activate`

6. Validate that environment is now activated by confirming that you are seeing something similar to this in output.
   `(testing) manny@Manuels-MBP urlshortenerservice`

7. Navigate to the config directory by passing:
    `cd config`
8. Pass in the following command to install required packages for this service:
    `pip install -r requirements.txt`

9. Run the following command to start your server:
    `python manage.py runserver`
10. Validate that the url is up by going to:
    `http://localhost:8000/shortener/`
    
    If you see something like the image below you are good to go and use the service:
    
    ![Screenshot] (/screenshots/Shortener_View.png)
    Format: ![Alt Text](url)

11. Enter the url you would need to shorten and click the shorten button to receive a shortened url

Hours spent on this have been three.

