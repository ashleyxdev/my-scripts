Write-Host "==============================="
Write-Host "   Jupyter Notebook Downloader"
Write-Host "==============================="
Write-Host ""

# === Define file lists and dependencies ===
$repoBase = "https://raw.githubusercontent.com/ashleyxdev/my-scripts/master"

# Map notebooks to their required CSV files
$files = @(
    @{ id = 1; name = "linear-regression.ipynb"; csv = "" },
    @{ id = 2; name = "naive-bayes.ipynb"; csv = "document.csv" },
    @{ id = 3; name = "svm.ipynb"; csv = "emails.csv" },
    @{ id = 4; name = "kmeans.ipynb"; csv = "" },
    @{ id = 5; name = "random-forest.ipynb"; csv = "" },
    @{ id = 6; name = "boosting.ipynb"; csv = "" },
    @{ id = 7; name = "taxi-problem.ipynb"; csv = "" },
    @{ id = 8; name = "tic-tac-toe.ipynb"; csv = "" }
)

# === Display all notebook options ===
Write-Host "Available Jupyter Notebooks:`n"
foreach ($f in $files) {
    if ($f.csv -ne "") {
        Write-Host "$($f.id). $($f.name) (requires: $($f.csv))"
    } else {
        Write-Host "$($f.id). $($f.name)"
    }
}

Write-Host ""
$choice = Read-Host "Enter your choice (1-$($files.Count))"

$selected = $files | Where-Object { $_.id -eq [int]$choice }

if (-not $selected) {
    Write-Host "Invalid choice! Exiting."
    exit
}

# === Download selected notebook ===
$notebookUrl = "$repoBase/$($selected.name)"
Write-Host "`nDownloading $($selected.name)..."
Invoke-WebRequest -Uri $notebookUrl -OutFile $selected.name
Write-Host "Notebook download complete!"

# === Ask for CSV file ===
if ($selected.csv -ne "") {
    Write-Host "`nThis notebook uses a dataset: $($selected.csv)"
    $downloadCsv = Read-Host "Do you want to download this CSV file now? (Y/n)"
    if ($downloadCsv -eq "" -or $downloadCsv -match "^[Yy]$") {
        $csvUrl = "$repoBase/$($selected.csv)"
        Write-Host "`nDownloading $($selected.csv)..."
        Invoke-WebRequest -Uri $csvUrl -OutFile $selected.csv
        Write-Host "CSV download complete!"
    } else {
        Write-Host "Skipped CSV download."
    }
} else {
    Write-Host "`nThis notebook does not require any CSV file."
}

Write-Host "`nAll done!"

