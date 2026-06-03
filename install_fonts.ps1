# install_fonts.ps1 — Installer les polices Noto/Twemoji pour l'utilisateur actuel (sans privilège Admin requis)
# Dossier source : C:\Users\salib\Desktop\Tor Browser\Browser\fonts

$SourceFolder = "C:\Users\salib\Desktop\Tor Browser\Browser\fonts"
$TargetFolder = "$env:LOCALAPPDATA\Microsoft\Windows\Fonts"
$RegistryPath = "HKCU:\Software\Microsoft\Windows NT\CurrentVersion\Fonts"

# S'assurer que le dossier cible de l'utilisateur existe
if (-not (Test-Path $TargetFolder)) {
    New-Item -Path $TargetFolder -ItemType Directory -Force | Out-Null
}

Write-Host "=========================================================="
Write-Host "Installation des polices d'écriture pour l'utilisateur..."
Write-Host "Dossier source : $SourceFolder"
Write-Host "Dossier cible  : $TargetFolder"
Write-Host "=========================================================="

# Récupérer tous les fichiers TTF et OTF
$FontFiles = Get-ChildItem -Path $SourceFolder -Filter "*.ttf" -Recurse

$installedCount = 0
$skippedCount = 0

foreach ($File in $FontFiles) {
    $DestFile = Join-Path $TargetFolder $File.Name
    $FontName = $File.BaseName
    
    # Si la police n'est pas déjà installée, on la copie et l'enregistre
    if (-not (Test-Path $DestFile)) {
        try {
            Copy-Item -Path $File.FullName -Destination $DestFile -Force
            # Enregistrement dans le registre utilisateur (HKCU)
            New-ItemProperty -Path $RegistryPath -Name "$FontName (TrueType)" -Value $File.Name -PropertyType String -Force | Out-Null
            Write-Host "[+] Installée : $($File.Name)"
            $installedCount++
        } catch {
            Write-Host "[-] Échec de l'installation de $($File.Name) : $_"
        }
    } else {
        # Déjà installé
        $skippedCount++
    }
}

Write-Host "----------------------------------------------------------"
Write-Host "[OK] Fin de l'installation."
Write-Host "  • Polices nouvellement installées : $installedCount"
Write-Host "  • Polices déjà présentes (passées) : $skippedCount"
Write-Host "=========================================================="
