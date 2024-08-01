pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from your version control system
                checkout scm
            }
        }

        stage('Set Up Virtual Environment') {
            steps {
                // Create a virtual environment
                sh 'python3 -m venv venv'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install dependencies from requirements.txt
                sh 'venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Run Ops Script') {
            steps {
                // Run the ops.py script
                sh 'venv/bin/python ops.py'
            }
        }

        stage('Run Tests') {
            steps {
                // Run tests using pytest
                sh 'venv/bin/pytest --junitxml=test-results/results.xml test_ops.py'
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
