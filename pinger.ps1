
$year = 365 + 1

foreach ($day in $year) {
    # New-item -ItemType "file" -Path .\Standard_Log $(Get-Date).csv -Header "DEVICE", "NETWORK_IP", "STATUS", "LOG_TIME"
    Write-Host 'Starting log for' $(Get-Date)
    Write-Host '*************************************************************'

}


# for year in range(0, 365 + 1):
#   with open(f'Standard_Log_ { ctime() }.csv', 'a+') as log:
# print(f'Starting log for { ctime() }\n')
# log.write(f'Monitoring Log for { ctime() }\n')
# log.write('')
# log.write(f'DEVICE     , NETWORK IP     , STATUS     , LOG_TIME\n')
# for minutes in range(0, 1440):
# ping_devices(log)
# sleep(5)
# system('clear')



$devices = Import-Csv -path .\devices.csv -Header "Host", "IP" -delimiter ","
Foreach ($device in $devices) {
    $pingRequest = Test-Connection $device.IP -Count 1 -Quiet
    if ($PingRequest -eq $false) {
        Write-Host "Status for $device is DOWN | Log $(Get-Date)" 
        Write-Output @($device.Host, $device.IP, "DOWN", $(Get-Date)) | Out-file -Append -filepath ./Standard_Log.csv
    }
    else {
        Write-Host "Status for $device is UP | Log $(Get-Date)"
        Write-Output @($device.Host, $device.IP, "UP", $(Get-Date)) | Out-File -Append -filepath ./Standard_Log.csv 
    }
}