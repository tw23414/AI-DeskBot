
#define MyAppName "AI-DeskBot"
#define MyAppVersion "0.7.0"
#define MyAppPublisher "AI-DeskBot"

[Setup]
AppId={{A3D7C921-8F42-4B51-AF20-123456789ABC}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
DefaultDirName={autopf}\AI-DeskBot
DefaultGroupName=AI-DeskBot
OutputDir=output
OutputBaseFilename=AI-DeskBot-Setup-v0.7.0
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Files]
Source: "..\assistant\main.py"; DestDir: "{app}\assistant"
Source: "..\brain\__init__.py"; DestDir: "{app}\brain"
Source: "..\brain\ai_brain.py"; DestDir: "{app}\brain"
Source: "..\memory\memory.py"; DestDir: "{app}\memory"
Source: "..\memory\memory_detector.py"; DestDir: "{app}\memory"
Source: "..\memory\memory_retrieval.py"; DestDir: "{app}\memory"
Source: "..\personality\personality.py"; DestDir: "{app}\personality"

[Icons]
Name: "{autoprograms}\AI-DeskBot"; Filename: "{cmd}"; Parameters: "/c cd /d ""{app}"" && python -m assistant.main"; WorkingDir: "{app}"; IconFilename: "{sys}\shell32.dll"; IconIndex: 13
