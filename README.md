### Using python to use a google sheets as an API
  - gcs -- select the project drop-down, select NEW PROJECT
  - name the project, click CREATE, then open it/make it the current project
  - in search bar search for 'drive api' -- or whatever...
  - verify the project in the dropdown and ENABLE the API
  - enable the 'sheets api' also
  - click on Credentials in sidebar, click '+ CREATE CREDENTIALS' at top, choose 'Service Account'
  - give the service account a name, click 'continue'/'Done' in 'Grant this service...' and 'Grant users access...' prompts
  - to the right of the service account email address, click the edit 'pencil', click KEYS tab
    - ADD KEY -> Create New Key -> JSON -> CREATE
    - download the JSON file, move it in the same folder as the script and rename to creds.json
  - copy the 'client_email' -> goto the 'Budg' sheet, click 'Share', paste the email address, keep 'Editor' role
  - Now the sheet is ready to use as and API. see 'getnext.py'





