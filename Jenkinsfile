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
                // Create and activate a virtual environment
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install dependencies from requirements.txt
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Run tests using pytest
                sh '. venv/bin/activate && pytest test_ops.py'
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
