pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from your version control system
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install dependencies from requirements.txt
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Run tests using pytest
                sh 'pytest test_ops.py'
            }
        }
    }

    post {
        always {
            // Archive test results
            junit '**/test-results/*.xml'
            // Clean up the workspace
            cleanWs()
        }
    }
}
