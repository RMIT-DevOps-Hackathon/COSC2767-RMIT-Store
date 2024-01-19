# Getting Started

## Setup resources

- Create a EKS cluster
  - use LabRole profile.
  - add EKD policies to LabRole profile (**Access** tab, see tutorial week 10).
  - Create node groups (**Compute** tab, 2 instances).
- Setup Kubectl
  - SSH to Kubectl_Server.
  - run connect-workers.sh script, enter the EKS cluster name and AWS region.
  - run `kubectl get nodes` and verify that Kubectl connected successfully to workers.

## Deployment

Deploy the cluster.

```bash
# COSC2767-RMIT-STORE/utilities/kubernetes/
kubectl create -f rmit-store-kube-deployment.yml
```

View information of the deployment.

```bash
kubectl get all
```

Get running pods in the cluster.

```bash
kubectl get pods
```

Trigger a restart deployment, latest images will be pulled and start on new containers. Old containers will be terminated once new containers successfully started.

```bash
kubectl rollout restart deployment
```
Delete all running resources in the cluster.

```bash
kubectl delete all --all --namespace=default
```
