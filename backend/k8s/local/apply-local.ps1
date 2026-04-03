# Le o namespace do arquivo .local-namespace
$namespace = Get-Content .\.local-namespace -ErrorAction Stop

Write-Host "Usando namespace: $namespace"

# Cria o namespace se ainda nao existir
kubectl get namespace $namespace 2>$null
if ($LASTEXITCODE -ne 0) {
    Write-Host "Criando namespace $namespace..."
    kubectl create namespace $namespace
}

Write-Host "Aplicando PostgreSQL..."
kubectl apply -f .\postgres\ -n $namespace

Write-Host "Aplicando Redis..."
kubectl apply -f .\redis\ -n $namespace

Write-Host ""
Write-Host "Pronto! Aguarde os pods ficarem Running:"
Write-Host "kubectl get pods -n $namespace"