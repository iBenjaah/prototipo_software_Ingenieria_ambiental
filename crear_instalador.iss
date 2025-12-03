; Script de Inno Setup para crear instalador
; Requiere Inno Setup: https://jrsoftware.org/isinfo.php

[Setup]
AppName=Sistema de Gestión Ambiental
AppVersion=1.0.0
AppPublisher=Equipo 2
AppPublisherURL=
DefaultDirName={autopf}\SistemaGestionAmbiental
DefaultGroupName=Sistema de Gestión Ambiental
DisableProgramGroupPage=yes
LicenseFile=
OutputDir=instalador
OutputBaseFilename=SistemaGestionAmbiental_Instalador
Compression=lzma
SolidCompression=yes
WizardStyle=modern
PrivilegesRequired=lowest

[Languages]
Name: "spanish"; MessagesFile: "compiler:Languages\Spanish.isl"

[Tasks]
Name: "desktopicon"; Description: "Crear icono en el escritorio"; GroupDescription: "Iconos adicionales:"
Name: "quicklaunchicon"; Description: "Crear icono en la barra de tareas"; GroupDescription: "Iconos adicionales:"

[Files]
Source: "distribucion\SistemaGestionAmbiental\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\Sistema de Gestión Ambiental"; Filename: "{app}\iniciar.bat"
Name: "{group}\Instalar Dependencias"; Filename: "{app}\instalar.bat"
Name: "{group}\Generar Datos de Ejemplo"; Filename: "{app}\generar_datos.bat"
Name: "{group}\Desinstalar"; Filename: "{uninstallexe}"
Name: "{autodesktop}\Sistema de Gestión Ambiental"; Filename: "{app}\iniciar.bat"; Tasks: desktopicon
Name: "{userappdata}\Microsoft\Internet Explorer\Quick Launch\Sistema de Gestión Ambiental"; Filename: "{app}\iniciar.bat"; Tasks: quicklaunchicon

[Run]
Filename: "{app}\instalar.bat"; Description: "Ejecutar instalación de dependencias ahora"; Flags: nowait postinstall skipifsilent

[Code]
procedure InitializeWizard;
begin
  WizardForm.LicenseLabel1.Caption := 'Sistema Informático de Gestión Ambiental' + #13#10 +
    'Para el seguimiento de variables críticas en la producción y ciclo de vida de baterías zinc-aire.' + #13#10#13#10 +
    'Requisitos:' + #13#10 +
    '- Python 3.8 o superior' + #13#10 +
    '- Navegador web moderno';
end;

