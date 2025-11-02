Write-Host "==============================="
Write-Host " Python Script Downloader"
Write-Host "==============================="
Write-Host ""

Write-Host "1. Download linear-regression.py"
Write-Host "2. Download naive-bayes.py"
Write-Host "3. Download svm.py"
Write-Host "4. Download kmeans.py"
Write-Host "5. Download random-forest.py"
Write-Host "6. Download boosting.py"
Write-Host "7. Download taxi-problem.py"
Write-Host "8. Download tic-tac-toe.py"
Write-Host ""

$choice = Read-Host "Enter your choice (1-3)"

switch ($choice) {
    1 { $file = "taxi-problem.py"}
    2 { $file = "naive-bayes.py" }
    3 { $file = "svm.py" }
    4 { $file = "kmeans.py" }
    5 { $file = "random-forest.py" }
    6 { $file = "boosting.py" }
    7 { $file = "taxi-problem.py" }
    8 { $file = "tic-tac-toe.py" }
    default {
        Write-Host "Invalid choice!"
        exit
    }
}

$url = "https://raw.githubusercontent.com/ashleyxdev/my-scripts/master/$file"

Write-Host "`nDownloading $file..."
Invoke-WebRequest -Uri $url -OutFile $file
Write-Host "Download complete!"
