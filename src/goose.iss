[Setup]
AppName=Goose
AppVersion=1.0
DefaultDirName={commonpf}\Goose
DefaultGroupName=Goose
OutputBaseFilename=GooseSetup
Compression=lzma
SolidCompression=yes
WizardStyle=modern
SetupIconFile=C:\Users\khare\Desktop\goose\src\goose-icon.ico

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Files]
Source: dist\goose.exe; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\Goose"; Filename: "{app}\goose.exe"

[Registry]
Root: HKLM; Subkey: "SYSTEM\CurrentControlSet\Control\Session Manager\Environment"; ValueType: expandsz; ValueName: "Path"; ValueData: "{olddata};{app}"; Flags: createvalueifdoesntexist uninsdeletevalue
