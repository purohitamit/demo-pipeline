pipeline{
    agent any
    stages{
        stage('test'){
            steps {
                sh "bash tests/test_app.py"
            }
        }
    }
    post {
        always{
            archiveArtifacts artifacts: "htmlcov/*"
        }
    }
}