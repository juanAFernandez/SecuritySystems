echo -e "\n\033[31m 1. Downloading Google App Engine SDK (v.1.9.30) \033[0m\n"
curl -O https://storage.googleapis.com/appengine-sdks/featured/google_appengine_1.9.30.zip
echo -e "\n\033[31m 2. Unzip SDK \033[0m\n"
unzip google_appengine_1.9.30.zip
echo -e "\n\033[31m 3. Deleting .zip \033[0m\n"
rm google_appengine_1.9.30.zip
