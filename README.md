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
