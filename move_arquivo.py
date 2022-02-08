import os, shutil, glob, datetime, time

diretorio_fonte = r"\\Principalnew\koch\Bradesco\Remessa"; ## Edit this

diretorio_destino = r"\\Principalnew\koch\Bradesco\Remessa\Enviados"; ## Edit this

##try:
##  os.makedirs(dst_fldr); ## it creates the destination folder
##except:
##  print "Folder already exist or some error";

print('*'*50)
print('Movendo os arquivos de boletos do dia anterior:')
print(f'Diretório de origem: {diretorio_fonte}')
print(f'Diretório de destino: {diretorio_destino}')
print()
print('Arquivos movidos:')
for rem_file in glob.glob(diretorio_fonte+"\\*.REM"):
#    if os.path.getctime(rem_file) < datetime.date.today():
#    if time.ctime(os.path.getctime(rem_file)) < datetime.date.today():
    t = os.path.getmtime(rem_file)
    #t_data = datetime.datetime.fromtimestamp(t)
    t_data = datetime.date.fromtimestamp(t)
    hoje = datetime.date.today()
    ontem = hoje - datetime.timedelta(days=1)
    if t_data < ontem:
        #shutil.copy2(rem_file, diretorio_destino);
        shutil.move(rem_file, diretorio_destino);
        print(rem_file)
