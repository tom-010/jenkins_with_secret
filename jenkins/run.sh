docker build -t jenkins:jcasc . || exit 1
docker run --name jenkins --rm -p 80:8080 --env JENKINS_ADMIN_ID=admin --env JENKINS_ADMIN_PASSWORD=password jenkins:jcasc
