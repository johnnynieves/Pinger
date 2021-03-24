
#Variables
$year = 365 + 1
$day = 1440 +1
$devices = Import-Csv -path .\devices.csv -Header "Host", "IP" -delimiter ","

#Start Basic WhatsupGold

For($day=0;$day -le $year; $day++) {
    clear
    Write-Host "Starting log for" $(Get-Date -f yyyy/MM/dd)
    Write-Host "*************************************************************"
    Set-Content .\Standard_Log.csv "DEVICE & IP,STATUS, LOG_TIME"
    For($minute=0;$minute -le $day; $day++){
        Foreach ($device in $devices) {
            $PingRequest = Test-Connection $device.IP -Count 1 -Quiet
            if ($PingRequest -eq $false) {
                Write-Host "Status for $device is  DOWN | Log $(Get-Date)" -ForegroundColor Red
                $list = "$device,DOWN,$(Get-Date)"
                Write-Output $list | Out-file -Append -filepath .\Standard_Log.csv
                msg console /server:localhost $list
            }
            else {
                Write-Host "Status for $device is UP | Log $(Get-Date)" -ForegroundColor Green
                $list = "$device,UP,$(Get-Date)"
                Write-Output $list | Out-File -Append -filepath .\Standard_Log.csv
            }
        }
        Start-Sleep -Seconds 300  #Every 5 Minutes
    }
}

