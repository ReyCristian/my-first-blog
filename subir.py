import os
print("se va a subir al servidor\n");
os.system("git status");
os.system("git add --all");
os.system("git status");
commit=input("ingrese el commit:");
comando ="git commit -m \"" + commit + "\"";
os.system(comando);
os.system("git status");
ok=input("todo esta bien");
if ok[0]=='s':
	os.system("git push");

