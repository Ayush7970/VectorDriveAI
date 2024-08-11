from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

def authenticate_google_drive():
    SCOPES = ['https://www.googleapis.com/auth/drive']
    CLIENT_SECRET_FILE = '/Users/ayushbhardwaj/Downloads/research/client_secret.json'
    
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
    creds = flow.run_local_server(port=0)
    service = build('drive', 'v3', credentials=creds)
    
    # Assuming 'web' application type for client config
    client_config = {
        "web": {
            "client_id": creds.client_id,
            "project_id": "your-project-id",
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_secret": creds.client_secret,
            "redirect_uris": ["urn:ietf:wg:oauth:2.0:oob", "http://localhost"]
        }
    }
    
    return service, client_config["web"]
