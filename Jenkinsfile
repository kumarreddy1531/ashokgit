pipeline {
    agent any
    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/kumarreddy1531/ashokgit.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build('myflaskapp')
                }
            }
        }
        stage('Run Container') {
            steps {
                script {
                    // Stop and remove any running container
                    sh 'docker rm -f myflaskapp || true'
                    // Run the new container
                    sh 'docker run -d --name myflaskapp -p 5000:5000 myflaskapp'
                }
            }
        }
    }
}
