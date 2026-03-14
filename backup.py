import os
import shutil
import configparser
import hashlib
from pathlib import Path

def load_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['backup']

def get_file_hash(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            sha256.update(chunk)
    return sha256.hexdigest()

def get_files_to_backup(source, exclude_patterns):
    files = []
    source_path = Path(source)
    for item in source_path.rglob('*'):
        if item.is_file():
            if not any(item.match(pattern) for pattern in exclude_patterns):
                files.append(item)
    return files

def copy_file(file, source, destination):
    relative_path = file.relative_to(source)
    dest_path = Path(destination) / relative_path
    
    if dest_path.exists():
        if get_file_hash(file) == get_file_hash(dest_path):
            return 'ignored', None
    
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(file, dest_path)
    
    if dest_path.exists():
        return 'modified', dest_path
    return 'added', dest_path

def main():
    config = load_config()
    source = config['source']
    destination = config['destination']
    exclude = config.get('exclude', '').split(',')
    exclude = [p.strip() for p in exclude if p.strip()]
    
    print(f"Iniciando backup de '{source}' para '{destination}'")
    
    if not os.path.exists(source):
        print(f"Erro: Pasta de origem '{source}' não existe!")
        return
    
    files = get_files_to_backup(source, exclude)
    print(f"Encontrados {len(files)} arquivos para backup\n")
    
    added = []
    modified = []
    ignored = []
    
    for file in files:
        status, result = copy_file(file, source, destination)
        if status == 'added':
            added.append(result)
        elif status == 'modified':
            modified.append(result)
        else:
            ignored.append(file.relative_to(source))
    
    print("=" * 50)
    print("RESUMO DO BACKUP")
    print("=" * 50)
    
    print(f"\n[{len(added)}] ARQUIVOS ADICIONADOS:")
    for a in added:
        print(f"  + {a}")
    
    print(f"\n[{len(modified)}] ARQUIVOS MODIFICADOS:")
    for m in modified:
        print(f"  ~ {m}")
    
    print(f"\n[{len(ignored)}] ARQUIVOS IGNORADOS")
    
    print(f"\nTotal: {len(added)} adicionados, {len(modified)} modificados, {len(ignored)} ignorados.")

if __name__ == '__main__':
    main()
