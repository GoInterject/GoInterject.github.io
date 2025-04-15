<#
.SYNOPSIS
    Searches for and prints registry keys and values related to the Interject product.

.DESCRIPTION
    Locates Interject-related registry entries by:
      - Checking known registry keys (Excel add-ins, VSTO security, Interject custom keys)
      - Searching Excel Options keys for OPEN* values (add-in loader DLLs)
      - Checking for specific values (LastUsedUser, LastUsedCompany, Addin Manager, Disabled Items)
      - Searching Interject Data Systems and HKEY_CLASSES_ROOT keys

.NOTES
    Run as Administrator if needed.

.EXAMPLE
    .\regkey_find.ps1
#>

# Set to $true for verbose output about missing keys/values
$VerboseOutput = $false

function Write-VerboseMessage {
    param($message)
    if ($VerboseOutput) {
        Write-Host "[VERBOSE] $message" -ForegroundColor DarkGray
    }
}

# Returns registry key properties if the key exists, otherwise $null
function Get-RegistryProperties {
    param(
        [Parameter(Mandatory = $true)]
        [string]$RegPath
    )
    if (Test-Path $RegPath) {
        try {
            return Get-ItemProperty -Path $RegPath -ErrorAction SilentlyContinue
        }
        catch {
            Write-VerboseMessage "Error accessing properties for $RegPath : $_"
        }
    }
    return $null
}

# Prints all properties of a registry key if it exists, with formatting
function SearchAndPrintKey {
    param(
        [Parameter(Mandatory = $true)]
        [string]$RegPath
    )
    if (Test-Path $RegPath) {
        Write-Host ""
        Write-Host "[$RegPath]" -ForegroundColor Green
        $props = Get-RegistryProperties -RegPath $RegPath
        if ($props) {
            $maxLen = ($props.PSObject.Properties | Where-Object { $_.Name -notin @("PSPath", "PSParentPath", "PSChildName", "PSDrive", "PSProvider") } | ForEach-Object { $_.Name.Length } | Measure-Object -Maximum).Maximum
            foreach ($prop in $props.PSObject.Properties) {
                if ($prop.Name -notin @("PSPath", "PSParentPath", "PSChildName", "PSDrive", "PSProvider")) {
                    $namePadded = $prop.Name.PadRight($maxLen)
                    Write-Host ("   {0} : {1}" -f $namePadded, $prop.Value) -ForegroundColor Yellow
                }
            }
        } else {
            Write-Host "   (No properties found)" -ForegroundColor DarkYellow
        }
        Write-Host ("".PadLeft(50,"-")) -ForegroundColor DarkCyan
    }
    else {
        Write-VerboseMessage "Key not found: $RegPath"
    }
}

# Prints a specific value from a registry key if it exists, with formatting
function Check-RegistryValue {
    param(
        [Parameter(Mandatory=$true)]
        [string]$RegPath,
        [Parameter(Mandatory=$true)]
        [string]$ValueName
    )
    if (Test-Path $RegPath) {
        $props = Get-RegistryProperties -RegPath $RegPath
        if ($props -and ($props.PSObject.Properties.Name -contains $ValueName)) {
            Write-Host ""
            Write-Host ("[{0}] '{1}'" -f $RegPath, $ValueName) -ForegroundColor Green
            Write-Host ("   {0} : {1}" -f $ValueName, $props.$ValueName) -ForegroundColor Yellow
            Write-Host ("".PadLeft(50,"-")) -ForegroundColor DarkCyan
        }
        else {
            Write-VerboseMessage "Value '$ValueName' not found in $RegPath"
        }
    }
    else {
        Write-VerboseMessage "Key $RegPath not found."
    }
}

Write-Host ""
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "   INTERJECT REGISTRY SEARCH STARTED" -ForegroundColor Magenta
Write-Host "==========================================" -ForegroundColor Cyan

# --- 1. Explicit Interject-related Registry Keys ---
Write-Host ""
Write-Host ">>> Explicit Interject Registry Keys <<<" -ForegroundColor Cyan
Write-Host "These keys control Interject Excel add-in registration, VSTO security, and Interject-specific settings." -ForegroundColor DarkGray
Write-Host "Includes both user and machine scope, and 32/64-bit registry views." -ForegroundColor DarkGray

$explicitRegistryPaths = @(
    # Excel Add-in keys (32-bit and 64-bit)
    "HKCU:\Software\Microsoft\Office\Excel\Addins\Interject.AddinModule",
    "HKCU:\Software\Wow6432Node\Microsoft\Office\Excel\Addins\Interject.AddinModule",
    "HKLM:\Software\Microsoft\Office\Excel\Addins\Interject.AddinModule",
    "HKLM:\Software\Wow6432Node\Microsoft\Office\Excel\Addins\Interject.AddinModule",
    # VSTO Security Inclusion keys
    "HKCU:\Software\Microsoft\Office\16.0\VSTO\Security\Inclusion",
    "HKCU:\Software\Wow6432Node\Microsoft\Office\16.0\VSTO\Security\Inclusion",
    "HKLM:\Software\Microsoft\Office\16.0\VSTO\Security\Inclusion",
    "HKLM:\Software\Wow6432Node\Microsoft\Office\16.0\VSTO\Security\Inclusion",
    # Custom Interject keys
    "HKCU:\Software\Interject",
    "HKCU:\Software\Wow6432Node\Interject",
    "HKLM:\Software\Interject",
    "HKLM:\Software\Wow6432Node\Interject"
)
foreach ($path in $explicitRegistryPaths) {
    SearchAndPrintKey -RegPath $path
}

# --- 2. Excel Options Keys for Loader Values (OPEN*) ---
Write-Host ""
Write-Host ">>> Excel Options Keys (OPEN* values) <<<" -ForegroundColor Cyan
Write-Host "These keys contain Excel startup options, including OPEN/OPEN1/OPEN2, which may load Interject add-in DLLs automatically." -ForegroundColor DarkGray
Write-Host "Checking for any loader values that reference Interject components." -ForegroundColor DarkGray

$ExcelVersions = @("11.0", "12.0", "14.0", "15.0", "16.0", "17.0", "18.0", "19.0", "20.0")
foreach ($version in $ExcelVersions) {
    $optionsKey = "HKCU:\Software\Microsoft\Office\$version\Excel\Options"
    if (Test-Path $optionsKey) {
        Write-Host ""
        Write-Host "[$optionsKey] (Excel $version)" -ForegroundColor Green
        $props = Get-RegistryProperties -RegPath $optionsKey
        if ($props) {
            $openProps = $props.PSObject.Properties | Where-Object { $_.Name -match "^OPEN" }
            if ($openProps) {
                $maxLen = ($openProps | ForEach-Object { $_.Name.Length } | Measure-Object -Maximum).Maximum
                foreach ($prop in $openProps) {
                    $namePadded = $prop.Name.PadRight($maxLen)
                    Write-Host ("   {0} : {1}" -f $namePadded, $prop.Value) -ForegroundColor Yellow
                }
            } else {
                Write-Host "   (No OPEN* values found)" -ForegroundColor DarkYellow
            }
        }
        Write-Host ("".PadLeft(50,"-")) -ForegroundColor DarkCyan
    }
    else {
        Write-VerboseMessage "Excel Options key not found for version $version : $optionsKey"
    }
}

# --- 3. Additional Explicit Checks ---
Write-Host ""
Write-Host ">>> Additional Explicit Registry Checks <<<" -ForegroundColor Cyan
Write-Host "These checks look for Interject user/company info, auto-start entries, and Excel's disabled add-in records." -ForegroundColor DarkGray
Write-Host "Useful for troubleshooting user-specific issues and startup behavior." -ForegroundColor DarkGray

# LastUsedUser and LastUsedCompany
$interjectKey = "HKCU:\Software\Interject"
Check-RegistryValue -RegPath $interjectKey -ValueName "LastUsedUser"
Check-RegistryValue -RegPath $interjectKey -ValueName "LastUsedCompany"

# Interject Addin Manager in Run key
$runKey = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run"
Check-RegistryValue -RegPath $runKey -ValueName "Interject Addin Manager"

# Excel Disabled Items for value "1B5391AA"
$disabledItemsKey = "HKCU:\Software\Microsoft\Office\16.0\Excel\Resiliency\DisabledItems"
Check-RegistryValue -RegPath $disabledItemsKey -ValueName "1B5391AA"

# --- 4. Interject Data Systems registry keys ---
Write-Host ""
Write-Host ">>> Interject Data Systems Registry Keys <<<" -ForegroundColor Cyan
Write-Host "These keys store configuration for the Interject Excel Add-in, such as licensing and environment details." -ForegroundColor DarkGray

$interjectDataSystemsKey = "HKCU:\Software\Interject Data Systems\Interject Excel Add-in"
SearchAndPrintKey -RegPath $interjectDataSystemsKey

# --- 5. HKEY_CLASSES_ROOT Interject modules and CLSID values ---
Write-Host ""
Write-Host ">>> HKEY_CLASSES_ROOT Interject Module Keys <<<" -ForegroundColor Cyan
Write-Host "These keys define COM registration for Interject modules, enabling Excel and Windows to locate and load the add-in." -ForegroundColor DarkGray

$classesRootPaths = @(
    "Registry::HKEY_CLASSES_ROOT\Interject.AddinModule",
    "Registry::HKEY_CLASSES_ROOT\Interject.IjXLLModule"
)
foreach ($path in $classesRootPaths) {
    SearchAndPrintKey -RegPath $path
}

# Specific CLSID registry paths
Write-Host ""
Write-Host ">>> Specific CLSID Registry Keys <<<" -ForegroundColor Cyan
Write-Host "These keys map Interject COM classes to their unique identifiers and installer types." -ForegroundColor DarkGray
Write-Host "Important for troubleshooting registration and installation issues." -ForegroundColor DarkGray

$clsidPaths = @(
    "HKCU:\Software\Classes\Interject.IjXLLModule\CLSID",
    "Registry::HKEY_CLASSES_ROOT\Interject.IjXLLModule\CLSID",
    "HKCU:\Software\Classes\Interject.AddinModule\CLSID",
    "Registry::HKEY_CLASSES_ROOT\Interject.AddinModule\CLSID"
)
foreach ($path in $clsidPaths) {
    SearchAndPrintKey -RegPath $path
}

# InstallerTypeGuid values
Check-RegistryValue -RegPath "HKCU:\Software\Classes\Interject.AddinModule\CLSID" -ValueName "InstallerTypeGuid"
Check-RegistryValue -RegPath "Registry::HKEY_CLASSES_ROOT\Interject.AddinModule\CLSID" -ValueName "InstallerTypeGuid"

Write-Host ""
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "   INTERJECT REGISTRY SEARCH COMPLETED" -ForegroundColor Magenta
Write-Host "==========================================" -ForegroundColor Cyan
