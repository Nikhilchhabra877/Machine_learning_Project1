# Machine_learning_Project1

End to end project requirements(dummy project):

''''
1. Creating conda enviornment
conda create -p venv python==3.9 -y
2. Create a requirement.txt file
pip install -r requirement.txt
          or
conda install flask
3. commit the changes and push to github 

git commit <file_name> -m "message"
git push origin main

4. connect github to heroku
Heroku_email : nikhilchhabra877@gmail.com
API_key : 45312f9a-56df-4b65-95f0-c158c5c4d1ab
app_name : ml-regression877
5. BUILD DOCKER IMAGE
docker build -t <image_name>:<tag_name> .
Name of the image should be in small letters
6. Check the docker image
docker images
7. Run the docker image
docker run -p 5000:5000 -e PORT=5000 4c865f54466e
8. check and stop the container
docker ps
docker step <container_id>



