; Script gerado pelo Inno Setup Script Wizard.
; Personalizado para incluir banco de dados JSON e configurações adicionais.

#define MyAppName "Registrar Incidentes"
#define MyAppVersion "1.0"
#define MyAppPublisher "mdsl1"
#define MyAppURL "https://github.com/mdsl1/Python_Projects"
#define MyAppExeName "mainV3.exe"

[Setup]
AppId={{1DA92AC9-2C44-41B6-8350-4AD1374076E3}}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\{#MyAppName}
DefaultGroupName={#MyAppName}
UninstallDisplayIcon={app}\{#MyAppExeName}
ArchitecturesAllowed=x64
ArchitecturesInstallIn64BitMode=x64
Compression=lzma
SolidCompression=yes
OutputBaseFilename=Registrar_Incidentes_Installer
WizardStyle=modern
DisableProgramGroupPage=yes
ChangesAssociations=yes

[Languages]
Name: "brazilianportuguese"; MessagesFile: "compiler:Languages\BrazilianPortuguese.isl"

[Tasks]
Name: "desktopicon"; Description: "Criar atalho na área de trabalho"; GroupDescription: "Atalhos adicionais"; Flags: unchecked

[Files]
Source: "C:\Users\Marcos Daniel\Desktop\Projects\Python_Projects\dist\mainV3.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Marcos Daniel\Desktop\Projects\Python_Projects\dados.json"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "Executar {#MyAppName}"; Flags: nowait postinstall skipifsilent