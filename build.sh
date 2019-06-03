docker rmi sophia921025/ppdml_demon
docker build --no-cache -t sophia921025/ppdml_demon ./

printf "Upload to Docker Hub?\nOptions [Y/n]: "
read uploadChoice
if [ $uploadChoice != "n" ]; then
    docker push sophia921025/ppdml_demon
fi