Steps and Process

1. Installing minikube - setting the context of kubectl to include minikube

2. Creating the DB - it needs a pvc to store data across containers, needs a service to recieve traffic, and a secrets to load env default admin credentials from env variables
3. Opportunity for improvement: db secrets are plain text, use a secure secret manager integration for secure deployment

4. Creating the backend - flask python app (AI generated) with a health and db check endpoint
5. dockerfile to create the app image - start with a slim python image and use pip to install dependencies, then add a health check (redundant since kubernetes health checks are independent, but still helped verify that the dockerfile was accurate), then the cmd to start the backend service. 
6. Adding backend to Minikube node - create a deployment to tell minikube how to configure the backend pods (how many pods + env variables etc + health checks)
6.1 Issue where couldn't find the image file that was built, I'm not exactly sure what the issue was, but building it and adding it to minikube then setting imagePullPolicy = never fixed it
6.2 added a backend service config to let the backend app recieve traffic within the node

7. Creating the front end (AI generated nginx webpage), html to display a webpage, nginx to serve the webpage and proxy the backend(i am not too famaliar with this). By the project reqs, using a configmap to load the files as data, but a better approach might be to use makefiles to create images with the scripts loaded into them?

Notes: the backend check: test-backend had a crashloopbackoff status, this is because I was testing that it worked. It's not part of the final web app

---

Assignment Description 
        |
        V
---

Kubernetes Assignment: Deploy a Multi-Tier Web Application

---

Objective: To understand and implement the core Kubernetes components by deploying a simple multi-tier application (frontend, backend, and database) on a Kubernetes cluster.

---

Learning Outcomes:

· Understand and define Kubernetes resources using YAML manifests

· Deploy and manage Pods, Deployments, Services, ConfigMaps, Secrets, and PVCs

· Build and deploy a Dockerized backend service

· Expose applications using NodePort

---

Application Architecture:

· Frontend: Nginx serving static content

· Backend: Flask-based Python application that connects to a MySQL database

· Database: MySQL with PersistentVolumeClaim

---

Tasks:

1. Cluster Setup

o Set up a local Kubernetes cluster using Minikube or Kind

o Verify with kubectl get nodes

2. Database Deployment (MySQL)

o Use a Deployment with a PVC for /var/lib/mysql

o Store DB credentials using Secrets

o Use a ClusterIP Service for internal communication

3. Backend Deployment (Flask App)

o Build a Docker image for a Python Flask app

o Configure the app to read DB credentials from environment variables

o Store DB credentials in Secrets

o Use a ClusterIP Service for internal access

4. Frontend Deployment (Nginx)

o Deploy a static HTML page served via Nginx

o Use a ConfigMap to inject the HTML file

o Expose using NodePort Service to access in browser

5. Testing

o Validate the frontend loads in browser

o Ensure backend connects to MySQL and returns a success message

---

Deliverables (A GITHUB REPO):

· Containing 3 folders, frontend, backend, db [each containing source codes and respective YAML files and Dockerfile (if applicable)]

· A folder containing screenshots of:

o Pods and Services running

o Frontend accessed in browser

· A brief README summarizing your steps

---

Submission Deadline: Tuesday, 17th June. EOD.

Evaluation Criteria:

· Correctness of configurations and deployment

· Ability to troubleshoot and test inter-service communication

· Clean, organized manifests and folder structure

---

Reach out in case of issues with kubectl, Docker image build, or service exposure.
