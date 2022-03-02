def branch_name = "${BRANCH_NAME}"

pipeline {
    agent any

    stages {
        stage('Run unit tests') {
            // Run unit tests on feature branches
            when { not { anyOf { branch 'main'; branch 'release'; branch 'develop' } } }
            steps {
                bat 'docker build . -t "web"'
                bat 'docker run --entrypoint "pytest test_unit.py" web'
            }
        }

        stage('Stress test') {
            // Stress test on develop branch
            when { branch 'develop' }
            steps {
                bat 'docker build . -t "web"'
                bat 'docker run --entrypoint "pytest test_stress.py" web'
            }
        }

        stage('Integration test') {
            // Integration test on develop branch
            when { branch 'develop' }
            steps {
                bat 'docker run --entrypoint "pytest test_integration.py" web'
            }
        }

        stage('End to end tests') {
            // End to end tests on develop branch
            when { branch 'develop' }
            steps {
                bat 'docker compose -f docker-compose-e2e-testing.yaml build'
                bat 'docker compose -f docker-compose-e2e-testing.yaml up --abort-on-container-exit'
            }
        }

        stage('Push to release') {
            // Push to the release branch on develop
            when { branch 'develop' }
            steps {
                sshagent(credentials: ['github_credentials']) {
                    bat 'git checkout release || git checkout -b release'
                    bat 'git rebase origin/develop'
                    bat 'git push origin release'
                }
            }
        }

        // On release, wait for user input before pushing to main
        stage('Push to main') {
            when { branch 'release' }
            steps {
                input {
                    message "Push to main?"
                    ok "Yes."
                }
                steps {
                    sshagent(credentials: ['github_credentials']) {
                        bat 'git checkout main || git checkout -b main'
                        bat 'git rebase origin/release'
                        bat 'git push origin main'
                    }
                }
            }
        }

        // On main branch, build & deploy
        stage('Build docker image') {
            when { branch 'main' }
            steps {
                bat 'docker compose build'
            }
        }
        stage('Deploy') {
            when { branch 'main' }
            steps {
                bat 'echo "Deployement..."'
                bat 'echo "Deployement succeeded."'
            }
        }

        // Display success on any branch
        stage('success') {
            steps {
                bat 'echo SUCCESS'
            }
        }
    }
}