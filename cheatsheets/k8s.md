### Switch kubeconfig

`kubectl config use-context kind-argocd`

### Get secret value

`kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d; echo`

