pipeline{
    agent any
    stages{
        stage('test'){
            steps {
                sh "bash flask-app/test.sh"
            }
        }
    }
    post {
        always{
            archiveArtifacts artifacts: "htmlcov/*"
        }
    }
}