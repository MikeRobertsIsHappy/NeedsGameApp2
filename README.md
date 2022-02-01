

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

application might be disbaled to reduce billing costs.
enable the appilcation here https://console.cloud.google.com/appengine/settings?cloudshell=false&project=the-needs-game

2.  Watch this https://www.youtube.com/watch?v=F7R8dEin6ZY
    Setup the gcloud tool, if you haven't already. Then use gcloud to deploy your app
   ```
   gcloud init
   gcloud app deploy
   ```
3. Your application is now live at `your-app-id.appspot.com`<br>
   
## Should look like this
   
![image](static\images\image8.png)

Example Comand line

Welcome to Cloud Shell! Type "help" to get started.
Your Cloud Platform project in this session is set to jacquelbot.
Use “gcloud config set project [PROJECT_ID]” to change to a different project.
mikerobertsishappy@cloudshell:~ (jacquelbot)$ git clone https://github.com/MikeRobertsIsHappy/jacquelbot_cloud
Cloning into 'jacquelbot_cloud'...
remote: Enumerating objects: 102, done.
remote: Counting objects: 100% (102/102), done.
remote: Compressing objects: 100% (78/78), done.
remote: Total 102 (delta 28), reused 88 (delta 18), pack-reused 0
Receiving objects: 100% (102/102), 4.48 MiB | 26.98 MiB/s, done.
Resolving deltas: 100% (28/28), done.
mikerobertsishappy@cloudshell:~ (jacquelbot)$ ls
jacquelbot_cloud  NeedsGameApp  README-cloudshell.txt
mikerobertsishappy@cloudshell:~ (jacquelbot)$ cd NeedGameApp
-bash: cd: NeedGameApp: No such file or directory
mikerobertsishappy@cloudshell:~ (jacquelbot)$ cd needsgameapp
-bash: cd: needsgameapp: No such file or directory
mikerobertsishappy@cloudshell:~ (jacquelbot)$ cd NeedsGameApp
mikerobertsishappy@cloudshell:~/NeedsGameApp (jacquelbot)$ gcloud init
Welcome! This command will take you through the configuration of gcloud.

Settings from your current configuration [cloudshell-7861] are:
accessibility:
  screen_reader: 'True'
component_manager:
  disable_update_check: 'True'
compute:
  gce_metadata_read_timeout_sec: '30'
core:
  account: mikerobertsishappy@gmail.com
  disable_usage_reporting: 'True'
  project: jacquelbot
metrics:
  environment: devshell

Pick configuration to use:
 [1] Re-initialize this configuration [cloudshell-7861] with new settings
 [2] Create a new configuration
Please enter your numeric choice:  1

Your current configuration has been set to: [cloudshell-7861]

You can skip diagnostics next time by using the following flag:
  gcloud init --skip-diagnostics

Network diagnostic detects and fixes local network connection issues.
Checking network connection...done.
Reachability Check passed.
Network diagnostic passed (1/1 checks passed).

Choose the account you would like to use to perform operations for this configuration:
 [1] mikerobertsishappy@gmail.com
 [2] Log in with a new account
Please enter your numeric choice:  1

You are logged in as: [mikerobertsishappy@gmail.com].

Pick cloud project to use:
 [1] jacquelbot
 [2] the-needs-game
 [3] Create a new project
Please enter numeric choice or text value (must exactly match list item):  2

Your current project has been set to: [the-needs-game].

Do you want to configure a default Compute Region and Zone? (Y/n)?  Y

Which Google Compute Engine zone would you like to use as project default?
If you do not specify a zone via a command line flag while working with Compute Engine resources, the default is assumed.
 [1] us-east1-b
 [2] us-east1-c
 [3] us-east1-d
 [4] us-east4-c
 [5] us-east4-b
 [6] us-east4-a
 [7] us-central1-c
 [8] us-central1-a
 [9] us-central1-f
 [10] us-central1-b
 [11] us-west1-b
 [12] us-west1-c
 [13] us-west1-a
 [14] europe-west4-a
 [15] europe-west4-b
 [16] europe-west4-c
 [17] europe-west1-b
 [18] europe-west1-d
 [19] europe-west1-c
 [20] europe-west3-c
 [21] europe-west3-a
 [22] europe-west3-b
 [23] europe-west2-c
 [24] europe-west2-b
 [25] europe-west2-a
 [26] asia-east1-b
 [27] asia-east1-a
 [28] asia-east1-c
 [29] asia-southeast1-b
 [30] asia-southeast1-a
 [31] asia-southeast1-c
 [32] asia-northeast1-b
 [33] asia-northeast1-c
 [34] asia-northeast1-a
 [35] asia-south1-c
 [36] asia-south1-b
 [37] asia-south1-a
 [38] australia-southeast1-b
 [39] australia-southeast1-c
 [40] australia-southeast1-a
 [41] southamerica-east1-b
 [42] southamerica-east1-c
 [43] southamerica-east1-a
 [44] asia-east2-a
 [45] asia-east2-b
 [46] asia-east2-c
 [47] asia-northeast2-a
 [48] asia-northeast2-b
 [49] asia-northeast2-c
 [50] asia-northeast3-a
Did not print [39] options.
Too many options [89]. Enter "list" at prompt to print choices fully.
Please enter numeric choice or text value (must exactly match list item):  8

Your project default Compute Engine zone has been set to [us-central1-a].
You can change it by running [gcloud config set compute/zone NAME].

Your project default Compute Engine region has been set to [us-central1].
You can change it by running [gcloud config set compute/region NAME].

Your Google Cloud SDK is configured and ready to use!

* Commands that require authentication will use mikerobertsishappy@gmail.com by default
* Commands will reference project `the-needs-game` by default
* Compute Engine commands will use region `us-central1` by default
* Compute Engine commands will use zone `us-central1-a` by default

Run `gcloud help config` to learn how to change individual settings

This gcloud configuration is called [cloudshell-7861]. You can create additional configurations if you work with multiple accounts and/or projects.
Run `gcloud topic configurations` to learn more.

Some things to try next:

* Run `gcloud --help` to see the Cloud Platform services you can interact with. And run `gcloud help COMMAND` to get help on any gcloud command.
* Run `gcloud topic --help` to learn about advanced features of the SDK like arg files and output formatting
mikerobertsishappy@cloudshell:~/NeedsGameApp (the-needs-game)$ gcloud app deploy
ERROR: (gcloud.app.deploy) Unable to deploy to application [the-needs-game] with status [USER_DISABLED]: Deploying to stopped apps is not allowed.
mikerobertsishappy@cloudshell:~/NeedsGameApp (the-needs-game)$ ^C
mikerobertsishappy@cloudshell:~/NeedsGameApp (the-needs-game)$ gcloud app deploy
ERROR: (gcloud.app.deploy) Unable to deploy to application [the-needs-game] with status [USER_DISABLED]: Deploying to stopped apps is not allowed.
mikerobertsishappy@cloudshell:~/NeedsGameApp (the-needs-game)$ ^C
mikerobertsishappy@cloudshell:~/NeedsGameApp (the-needs-game)$ gcloud app deploy
ERROR: (gcloud.app.deploy) Unable to deploy to application [the-needs-game] with status [USER_DISABLED]: Deploying to stopped apps is not allowed.
mikerobertsishappy@cloudshell:~/NeedsGameApp (the-needs-game)$ gcloud app deploy
Services to deploy:

descriptor:                  [/home/mikerobertsishappy/NeedsGameApp/app.yaml]
source:                      [/home/mikerobertsishappy/NeedsGameApp]
target project:              [the-needs-game]
target service:              [default]
target version:              [20220131t025614]
target url:                  [https://the-needs-game.uc.r.appspot.com]
target service account:      [App Engine default service account]


Do you want to continue (Y/n)?  ^C

Command killed by keyboard interrupt


mikerobertsishappy@cloudshell:~/NeedsGameApp (the-needs-game)$ gcloud app deploy
Services to deploy:

descriptor:                  [/home/mikerobertsishappy/NeedsGameApp/app.yaml]
source:                      [/home/mikerobertsishappy/NeedsGameApp]
target project:              [the-needs-game]
target service:              [default]
target version:              [20220131t025727]
target url:                  [https://the-needs-game.uc.r.appspot.com]
target service account:      [App Engine default service account]


Do you want to continue (Y/n)?  Y

Beginning deployment of service [default]...
Building and pushing image for service [default]
Started cloud build [908c3e1f-0130-4890-846f-eee4c6d9b9f6].
To see logs in the Cloud Console: https://console.cloud.google.com/cloud-build/builds/908c3e1f-0130-4890-846f-eee4c6d9b9f6?project=843711958892
----------------------------------------------------------------------------------------------- REMOTE BUILD OUTPUT ------------------------------------------------------------------------------------------------
starting build "908c3e1f-0130-4890-846f-eee4c6d9b9f6"

FETCHSOURCE
Fetching storage object: gs://staging.the-needs-game.appspot.com/us.gcr.io/the-needs-game/appengine/default.20220131t025727:latest#1643597856159311
Copying gs://staging.the-needs-game.appspot.com/us.gcr.io/the-needs-game/appengine/default.20220131t025727:latest#1643597856159311...
/ [1 files][  2.1 MiB/  2.1 MiB]
Operation completed over 1 objects/2.1 MiB.
BUILD
Starting Step #0
Step #0: Pulling image: gcr.io/gcp-runtimes/python/gen-dockerfile@sha256:ac444fc620f70ff80c19cde48d18242dbed63056e434f0039bf939433e7464aa
Step #0: gcr.io/gcp-runtimes/python/gen-dockerfile@sha256:ac444fc620f70ff80c19cde48d18242dbed63056e434f0039bf939433e7464aa: Pulling from gcp-runtimes/python/gen-dockerfile
Step #0: Digest: sha256:ac444fc620f70ff80c19cde48d18242dbed63056e434f0039bf939433e7464aa
Step #0: Status: Downloaded newer image for gcr.io/gcp-runtimes/python/gen-dockerfile@sha256:ac444fc620f70ff80c19cde48d18242dbed63056e434f0039bf939433e7464aa
Step #0: gcr.io/gcp-runtimes/python/gen-dockerfile@sha256:ac444fc620f70ff80c19cde48d18242dbed63056e434f0039bf939433e7464aa
Finished Step #0
Starting Step #1
Step #1: Pulling image: gcr.io/cloud-builders/docker@sha256:08c5443ff4f8ba85c2114576bb9167c4de0bf658818aea536d3456e8d0e134cd
Step #1: gcr.io/cloud-builders/docker@sha256:08c5443ff4f8ba85c2114576bb9167c4de0bf658818aea536d3456e8d0e134cd: Pulling from cloud-builders/docker
Step #1: 75f546e73d8b: Pulling fs layer
Step #1: 0f3bb76fc390: Pulling fs layer
Step #1: 3c2cba919283: Pulling fs layer
Step #1: 4d168e97939c: Pulling fs layer
Step #1: 4d168e97939c: Waiting
Step #1: 3c2cba919283: Verifying Checksum
Step #1: 3c2cba919283: Download complete
Step #1: 0f3bb76fc390: Verifying Checksum
Step #1: 0f3bb76fc390: Download complete
Step #1: 75f546e73d8b: Verifying Checksum
Step #1: 75f546e73d8b: Download complete
Step #1: 75f546e73d8b: Pull complete
Step #1: 4d168e97939c: Verifying Checksum
Step #1: 4d168e97939c: Download complete
Step #1: 0f3bb76fc390: Pull complete
Step #1: 3c2cba919283: Pull complete
Step #1: 4d168e97939c: Pull complete
Step #1: Digest: sha256:08c5443ff4f8ba85c2114576bb9167c4de0bf658818aea536d3456e8d0e134cd
Step #1: Status: Downloaded newer image for gcr.io/cloud-builders/docker@sha256:08c5443ff4f8ba85c2114576bb9167c4de0bf658818aea536d3456e8d0e134cd
Step #1: gcr.io/cloud-builders/docker@sha256:08c5443ff4f8ba85c2114576bb9167c4de0bf658818aea536d3456e8d0e134cd
Step #1: Sending build context to Docker daemon  2.456MB
Step #1: Step 1/9 : FROM gcr.io/google-appengine/python@sha256:c6480acd38ca4605e0b83f5196ab6fe8a8b59a0288a7b8216c42dbc45b5de8f6
Step #1: gcr.io/google-appengine/python@sha256:c6480acd38ca4605e0b83f5196ab6fe8a8b59a0288a7b8216c42dbc45b5de8f6: Pulling from google-appengine/python
Step #1: Digest: sha256:c6480acd38ca4605e0b83f5196ab6fe8a8b59a0288a7b8216c42dbc45b5de8f6
Step #1: Status: Downloaded newer image for gcr.io/google-appengine/python@sha256:c6480acd38ca4605e0b83f5196ab6fe8a8b59a0288a7b8216c42dbc45b5de8f6
Step #1:  ce284ab20159
Step #1: Step 2/9 : LABEL python_version=python3.6
Step #1:  Running in fcbdad3dac8b
Step #1: Removing intermediate container fcbdad3dac8b
Step #1:  8523ac141177
Step #1: Step 3/9 : RUN virtualenv --no-download /env -p python3.6
Step #1:  Running in 97d7aea0437c
Step #1: created virtual environment CPython3.6.10.final.0-64 in 1248ms
Step #1:   creator CPython3Posix(dest=/env, clear=False, global=False)
Step #1:   seeder FromAppData(download=False, pip=bundle, wheel=bundle, setuptools=bundle, via=copy, app_data_dir=/root/.local/share/virtualenv)
Step #1:     added seed packages: pip==20.2.2, setuptools==49.6.0, wheel==0.35.1
Step #1:   activators PythonActivator,FishActivator,XonshActivator,CShellActivator,PowerShellActivator,BashActivator
Step #1: Removing intermediate container 97d7aea0437c
Step #1:  6c96e352f196
Step #1: Step 4/9 : ENV VIRTUAL_ENV /env
Step #1:  Running in 211e051f4f61
Step #1: Removing intermediate container 211e051f4f61
Step #1:  0eadae9dfdd6
Step #1: Step 5/9 : ENV PATH /env/bin:$PATH
Step #1:  Running in 4c36a2529651
Step #1: Removing intermediate container 4c36a2529651
Step #1:  d93cdfbc17c6
Step #1: Step 6/9 : ADD requirements.txt /app/
Step #1:  72926e7fa7ee
Step #1: Step 7/9 : RUN pip install -r requirements.txt
Step #1:  Running in 42b973bbade2
Step #1: Collecting Flask==2.0.1
Step #1:   Downloading Flask-2.0.1-py3-none-any.whl (94 kB)
Step #1: Collecting gunicorn==20.1.0
Step #1:   Downloading gunicorn-20.1.0-py3-none-any.whl (79 kB)
Step #1: Collecting google-cloud-datastore==2.1.3
Step #1:   Downloading google_cloud_datastore-2.1.3-py2.py3-none-any.whl (127 kB)
Step #1: Collecting google-auth==1.31.0
Step #1:   Downloading google_auth-1.31.0-py2.py3-none-any.whl (147 kB)
Step #1: Collecting requests==2.25.1
Step #1:   Downloading requests-2.25.1-py2.py3-none-any.whl (61 kB)
Step #1: Collecting ChatterBot==1.0.0
Step #1:   Downloading ChatterBot-1.0.0-py2.py3-none-any.whl (65 kB)
Step #1: Collecting chatterbot-corpus==1.2.0
Step #1:   Downloading chatterbot_corpus-1.2.0-py2.py3-none-any.whl (117 kB)
Step #1: Collecting textblob==0.15.3
Step #1:   Downloading textblob-0.15.3-py2.py3-none-any.whl (636 kB)
Step #1: Collecting path==15.1.2
Step #1:   Downloading path-15.1.2-py3-none-any.whl (21 kB)
Step #1: Collecting pandas
Step #1:   Downloading pandas-1.1.5-cp36-cp36m-manylinux1_x86_64.whl (9.5 MB)
Step #1: Collecting twilio==6.53.0
Step #1:   Downloading twilio-6.53.0.tar.gz (470 kB)
Step #1: Collecting Jinja2>=3.0
Step #1:   Downloading Jinja2-3.0.3-py3-none-any.whl (133 kB)
Step #1: Collecting Werkzeug>=2.0
Step #1:   Downloading Werkzeug-2.0.2-py3-none-any.whl (288 kB)
Step #1: Collecting itsdangerous>=2.0
Step #1:   Downloading itsdangerous-2.0.1-py3-none-any.whl (18 kB)
Step #1: Collecting click>=7.1.2
Step #1:   Downloading click-8.0.3-py3-none-any.whl (97 kB)
Step #1: Requirement already satisfied: setuptools>=3.0 in /env/lib/python3.6/site-packages (from gunicorn==20.1.0->-r requirements.txt (line 2)) (49.6.0)
Step #1: Collecting google-cloud-core<2.0dev,>=1.4.0
Step #1:   Downloading google_cloud_core-1.7.2-py2.py3-none-any.whl (28 kB)
Step #1: Collecting google-api-core[grpc]<2.0.0dev,>=1.22.2
Step #1:   Downloading google_api_core-1.31.5-py2.py3-none-any.whl (93 kB)
Step #1: Collecting proto-plus>=1.4.0
Step #1:   Downloading proto_plus-1.19.9-py3-none-any.whl (45 kB)
Step #1: Collecting libcst>=0.2.5
Step #1:   Downloading libcst-0.4.1-cp36-cp36m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.7 MB)
Step #1: Collecting rsa<5,>=3.1.4; python_version >= "3.6"
Step #1:   Downloading rsa-4.8-py3-none-any.whl (39 kB)
Step #1: Collecting cachetools<5.0,>=2.0.0
Step #1:   Downloading cachetools-4.2.4-py3-none-any.whl (10 kB)
Step #1: Collecting six>=1.9.0
Step #1:   Using cached six-1.16.0-py2.py3-none-any.whl (11 kB)
Step #1: Collecting pyasn1-modules>=0.2.1
Step #1:   Downloading pyasn1_modules-0.2.8-py2.py3-none-any.whl (155 kB)
Step #1: Collecting certifi>=2017.4.17
Step #1:   Downloading certifi-2021.10.8-py2.py3-none-any.whl (149 kB)
Step #1: Collecting idna<3,>=2.5
Step #1:   Downloading idna-2.10-py2.py3-none-any.whl (58 kB)
Step #1: Collecting urllib3<1.27,>=1.21.1
Step #1:   Downloading urllib3-1.26.8-py2.py3-none-any.whl (138 kB)
Step #1: Collecting chardet<5,>=3.0.2
Step #1:   Downloading chardet-4.0.0-py2.py3-none-any.whl (178 kB)
Step #1: Collecting pint>=0.8.1
Step #1:   Downloading Pint-0.17-py2.py3-none-any.whl (204 kB)
Step #1: Collecting nltk<4.0,>=3.2
Step #1:   Downloading nltk-3.6.7-py3-none-any.whl (1.5 MB)
Step #1: Collecting sqlalchemy<1.3,>=1.2
Step #1:   Downloading SQLAlchemy-1.2.19.tar.gz (5.7 MB)
Step #1: Collecting python-dateutil<2.8,>=2.7
Step #1:   Downloading python_dateutil-2.7.5-py2.py3-none-any.whl (225 kB)
Step #1: Collecting pymongo<4.0,>=3.3
Step #1:   Downloading pymongo-3.12.3-cp36-cp36m-manylinux2014_x86_64.whl (524 kB)
Step #1: Collecting mathparse<0.2,>=0.1
Step #1:   Downloading mathparse-0.1.2-py3-none-any.whl (7.2 kB)
Step #1: Collecting PyYAML<4.0,>=3.12
Step #1:   Downloading PyYAML-3.13.tar.gz (270 kB)
Step #1: Collecting numpy>=1.15.4
Step #1:   Downloading numpy-1.19.5-cp36-cp36m-manylinux2010_x86_64.whl (14.8 MB)
Step #1: Collecting pytz>=2017.2
Step #1:   Downloading pytz-2021.3-py2.py3-none-any.whl (503 kB)
Step #1: Collecting PyJWT==1.7.1
Step #1:   Downloading PyJWT-1.7.1-py2.py3-none-any.whl (18 kB)
Step #1: Collecting MarkupSafe>=2.0
Step #1:   Downloading MarkupSafe-2.0.1-cp36-cp36m-manylinux2010_x86_64.whl (30 kB)
Step #1: Collecting dataclasses; python_version < "3.7"
Step #1:   Downloading dataclasses-0.8-py3-none-any.whl (19 kB)
Step #1: Collecting importlib-metadata; python_version < "3.8"
Step #1:   Downloading importlib_metadata-4.8.3-py3-none-any.whl (17 kB)
Step #1: Collecting googleapis-common-protos<2.0dev,>=1.6.0
Step #1:   Downloading googleapis_common_protos-1.54.0-py2.py3-none-any.whl (207 kB)
Step #1: Collecting packaging>=14.3
Step #1:   Downloading packaging-21.3-py3-none-any.whl (40 kB)
Step #1: Collecting protobuf>=3.12.0; python_version > "3"
Step #1:   Downloading protobuf-3.19.4-cp36-cp36m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.1 MB)
Step #1: Collecting grpcio<2.0dev,>=1.29.0; extra == "grpc"
Step #1:   Downloading grpcio-1.43.0-cp36-cp36m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (4.1 MB)
Step #1: Collecting typing-extensions>=3.7.4.2
Step #1:   Downloading typing_extensions-4.0.1-py3-none-any.whl (22 kB)
Step #1: Collecting typing-inspect>=0.4.0
Step #1:   Downloading typing_inspect-0.7.1-py3-none-any.whl (8.4 kB)
Step #1: Collecting pyasn1>=0.1.3
Step #1:   Downloading pyasn1-0.4.8-py2.py3-none-any.whl (77 kB)
Step #1: Collecting importlib-resources; python_version < "3.7"
Step #1:   Downloading importlib_resources-5.4.0-py3-none-any.whl (28 kB)
Step #1: Collecting joblib
Step #1:   Downloading joblib-1.1.0-py2.py3-none-any.whl (306 kB)
Step #1: Collecting regex>=2021.8.3
Step #1:   Downloading regex-2022.1.18-cp36-cp36m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (748 kB)
Step #1: Collecting tqdm
Step #1:   Downloading tqdm-4.62.3-py2.py3-none-any.whl (76 kB)
Step #1: Collecting zipp>=0.5
Step #1:   Downloading zipp-3.6.0-py3-none-any.whl (5.3 kB)
Step #1: Collecting pyparsing!=3.0.5,>=2.0.2
Step #1:   Downloading pyparsing-3.0.7-py3-none-any.whl (98 kB)
Step #1: Collecting mypy-extensions>=0.3.0
Step #1:   Downloading mypy_extensions-0.4.3-py2.py3-none-any.whl (4.5 kB)
Step #1: Building wheels for collected packages: twilio, sqlalchemy, PyYAML
Step #1:   Building wheel for twilio (setup.py): started
Step #1:   Building wheel for twilio (setup.py): finished with status 'done'
Step #1:   Created wheel for twilio: filename=twilio-6.53.0-py2.py3-none-any.whl size=1251199 sha256=5533e6d37c1e891f478e3ae51da363b9b826681c65ddad2dce072a8551c23582
Step #1:   Stored in directory: /root/.cache/pip/wheels/2a/4b/1e/2b8bc1a46e13739d6723589a2c0e9569e5f8c7ecdcdcea1a27
Step #1:   Building wheel for sqlalchemy (setup.py): started
Step #1:   Building wheel for sqlalchemy (setup.py): finished with status 'done'
Step #1:   Created wheel for sqlalchemy: filename=SQLAlchemy-1.2.19-cp36-cp36m-linux_x86_64.whl size=1138893 sha256=2ccac73c9130f57a926f05e1a9a4fac2cbfc595a0969b15a90c525d1293df7ee
Step #1:   Stored in directory: /root/.cache/pip/wheels/67/d8/2f/be2a676351d00822bd58d050a4e23d3142192dabeed4c5f1bd
Step #1:   Building wheel for PyYAML (setup.py): started
Step #1:   Building wheel for PyYAML (setup.py): finished with status 'done'
Step #1:   Created wheel for PyYAML: filename=PyYAML-3.13-cp36-cp36m-linux_x86_64.whl size=43085 sha256=ee469218a1ea45474943f7b10e313016b21f3218efa3e64f5eaefa8627191b6b
Step #1:   Stored in directory: /root/.cache/pip/wheels/ab/80/60/97eaebe423482bcf0963b19495b4cfe6c4caef59761a0c427d
Step #1: Successfully built twilio sqlalchemy PyYAML
Step #1: Installing collected packages: MarkupSafe, Jinja2, dataclasses, Werkzeug, itsdangerous, typing-extensions, zipp, importlib-metadata, click, Flask, gunicorn, six, protobuf, googleapis-common-protos, certifi, idna, urllib3, chardet, requests, pyparsing, packaging, pyasn1, rsa, cachetools, pyasn1-modules, google-auth, pytz, grpcio, google-api-core, google-cloud-core, proto-plus, PyYAML, mypy-extensions, typing-inspect, libcst, google-cloud-datastore, importlib-resources, pint, joblib, regex, tqdm, nltk, chatterbot-corpus, sqlalchemy, python-dateutil, pymongo, mathparse, ChatterBot, textblob, path, numpy, pandas, PyJWT, twilio
Step #1: ERROR: After October 2020 you may experience errors when installing or updating packages. This is because pip will change the way that it resolves dependency conflicts.
Step #1: 
Step #1: We recommend you use --use-feature=2020-resolver to test your packages with the new resolver before it becomes the default.
Step #1: 
Step #1: libcst 0.4.1 requires pyyaml>=5.2, but you'll have pyyaml 3.13 which is incompatible.
Step #1: Successfully installed ChatterBot-1.0.0 Flask-2.0.1 Jinja2-3.0.3 MarkupSafe-2.0.1 PyJWT-1.7.1 PyYAML-3.13 Werkzeug-2.0.2 cachetools-4.2.4 certifi-2021.10.8 chardet-4.0.0 chatterbot-corpus-1.2.0 click-8.0.3 dataclasses-0.8 google-api-core-1.31.5 google-auth-1.31.0 google-cloud-core-1.7.2 google-cloud-datastore-2.1.3 googleapis-common-protos-1.54.0 grpcio-1.43.0 gunicorn-20.1.0 idna-2.10 importlib-metadata-4.8.3 importlib-resources-5.4.0 itsdangerous-2.0.1 joblib-1.1.0 libcst-0.4.1 mathparse-0.1.2 mypy-extensions-0.4.3 nltk-3.6.7 numpy-1.19.5 packaging-21.3 pandas-1.1.5 path-15.1.2 pint-0.17 proto-plus-1.19.9 protobuf-3.19.4 pyasn1-0.4.8 pyasn1-modules-0.2.8 pymongo-3.12.3 pyparsing-3.0.7 python-dateutil-2.7.5 pytz-2021.3 regex-2022.1.18 requests-2.25.1 rsa-4.8 six-1.16.0 sqlalchemy-1.2.19 textblob-0.15.3 tqdm-4.62.3 twilio-6.53.0 typing-extensions-4.0.1 typing-inspect-0.7.1 urllib3-1.26.8 zipp-3.6.0
Step #1: WARNING: You are using pip version 20.2.2; however, version 21.3.1 is available.
Step #1: You should consider upgrading via the '/env/bin/python -m pip install --upgrade pip' command.
Step #1: Removing intermediate container 42b973bbade2
Step #1:  70d4cddeac22
Step #1: Step 8/9 : ADD . /app/
Step #1:  81ae6c2efc19
Step #1: Step 9/9 : CMD exec gunicorn -b :$PORT main:app
Step #1:  Running in 522d0e4e5749
Step #1: Removing intermediate container 522d0e4e5749
Step #1:  9a2e3b6ab890
Step #1: Successfully built 9a2e3b6ab890
Step #1: Successfully tagged us.gcr.io/the-needs-game/appengine/default.20220131t025727:latest
Finished Step #1
PUSH
Pushing us.gcr.io/the-needs-game/appengine/default.20220131t025727:latest
The push refers to repository [us.gcr.io/the-needs-game/appengine/default.20220131t025727]
103b1ee26571: Preparing
7906a00ff0cf: Preparing
169a0dfd086c: Preparing
0f6762c45cd9: Preparing
087d7553d285: Preparing
16919ab89eca: Preparing
74bcef7f7402: Preparing
bc9e931c388e: Preparing
20896f2c3dd8: Preparing
7b80c69caf34: Preparing
3bbec54fac0c: Preparing
4006ffa4c683: Preparing
844d958e8cbe: Preparing
84ff92691f90: Preparing
b49bce339f97: Preparing
dcb7197db903: Preparing
20896f2c3dd8: Waiting
7b80c69caf34: Waiting
3bbec54fac0c: Waiting
4006ffa4c683: Waiting
844d958e8cbe: Waiting
84ff92691f90: Waiting
b49bce339f97: Waiting
dcb7197db903: Waiting
16919ab89eca: Waiting
74bcef7f7402: Waiting
bc9e931c388e: Waiting
087d7553d285: Layer already exists
16919ab89eca: Layer already exists
74bcef7f7402: Layer already exists
bc9e931c388e: Layer already exists
20896f2c3dd8: Layer already exists
7b80c69caf34: Layer already exists
3bbec54fac0c: Layer already exists
4006ffa4c683: Layer already exists
844d958e8cbe: Layer already exists
84ff92691f90: Layer already exists
169a0dfd086c: Pushed
b49bce339f97: Layer already exists
dcb7197db903: Layer already exists
103b1ee26571: Pushed
0f6762c45cd9: Pushed
7906a00ff0cf: Pushed
latest: digest: sha256:b9cf598dc3bce784289e7188bc12e139ec95c0f0c80c27a4450fef305e28274e size: 3674
DONE
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Updating service [default] (this may take several minutes)...done.     
Setting traffic split for service [default]...done.     
Stopping version [the-needs-game/default/20211220t010655].
Sent request to stop version [the-needs-game/default/20211220t010655]. This operation may take some time to complete. If you would like to verify that it succeeded, run:
  $ gcloud app versions describe -s default 20211220t010655
until it shows that the version has stopped.
Deployed service [default] to [https://the-needs-game.uc.r.appspot.com]

You can stream logs from the command line by running:
  $ gcloud app logs tail -s default

To view your application in the web browser run:
  $ gcloud app browse
mikerobertsishappy@cloudshell:~/NeedsGameApp (the-needs-game)$ ^C
mikerobertsishappy@cloudshell:~/NeedsGameApp (the-needs-game)$ ^C
mikerobertsishappy@cloudshell:~/NeedsGameApp (the-needs-game)$ gcloud app browse
Did not detect your browser. Go to this link to view your app:
https://the-needs-game.uc.r.appspot.com
   