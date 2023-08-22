# # install dotnet first =========================================================================
# # https://learn.microsoft.com/en-us/dotnet/core/install/linux-scripted-manual#scripted-install
# wget https://dot.net/v1/dotnet-install.sh -O dotnet-install.sh
# chmod +x ./dotnet-install.sh
# ./dotnet-install.sh --version latest

# # for powershell core
# ./dotnet-install.sh --version latest --runtime aspnetcore
# ./dotnet-install.sh --channel 7.0

# # ==============================================================================================
# # installing dot net core using dotnet installer commands
# sudo apt  install dotnet-host-7.0

# sudo rm /etc/apt/sources.list.d/microsoft-prod.list
# sudo apt update
# sudo apt install dotnet-sdk-6.0 -y

# dotnet tool install --global PowerShell 


# ==============================================================================================
# use `pwsh` for starting powershell
