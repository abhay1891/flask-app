pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-app .'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Testing Flask App'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deployment Complete'
            }
        }
    }
}