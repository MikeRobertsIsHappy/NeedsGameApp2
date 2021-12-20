
## Run Locally

1. Clone this repo.

   ```
   git clone https://github.com/MikeRobertsIsHappy/jacquelbot_cloud
   ```

2. Open a sample folder, create a virtualenv, install dependencies, and run the sample:

   ```
   cd <to directroy>
   virtualenv env  # for first time
   env\Scripts\activate.ps1
   pip install -r requirements.txt   OR    pip install --no-cache-dir -r requirements.txt    # for first time
   python main.py
   http://127.0.0.1:8080/
   ```

3. Visit the application at  http://127.0.0.1:8080/.


## Optional Deploying to Google

1. Use the [Google Developers Console](https://console.developer.google.com)  to create a project/app id. (App id and project id are identical)

2.  Watch this https://www.youtube.com/watch?v=F7R8dEin6ZY
    Setup the gcloud tool, if you haven't already. Then use gcloud to deploy your app
   ```
   gcloud init
   gcloud app deploy
   ```
3. Your application is now live at `your-app-id.appspot.com`<br>
   
## Should look like this
   
![image](static\images\image8.png)
   
